# このモジュールはsugumiの中ではプレゼンテーション層にあたる。
# メソッド数が少ないので1モジュールで済ませている

# モジュールを追加
import os
from pathlib import Path
from flask import Flask, render_template, request
from injector import Injector, Module
from sugumi_domain import ProjectInfo, ProjectInfoRepository
from sugumi_infrastructure import PostgresqlProjectInfoRepository, SqliteProjectInfoRepository

from sugumi_service import ProjectInfoService

app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret_key'# CSRFに必要かも


class SqliteDiModule(Module):
    def configure(self, binder):
        binder.bind(ProjectInfoRepository, to=SqliteProjectInfoRepository)

class PostgresqlDiModule(Module):
    def configure(self, binder):
        binder.bind(ProjectInfoRepository, to=PostgresqlProjectInfoRepository)

injector = Injector([SqliteDiModule()])

@app.route('/')
def menu():
    projectInfoService = injector.get(ProjectInfoRepository)
    print(projectInfoService)
    rs = projectInfoService.find_all()
    print(rs[0].id)
    projectInfoService.create_table()
    projectInfoService.insert(ProjectInfo(1234))
    return render_template('menu.html')

@app.route('/env', methods=["GET", "POST"])
def env():
    if request.method == "POST":
        rows = request.form["rows"]
        print(rows)
        import json
        from sugumi_service import createInfrastructure
        for i in json.loads(rows):
            print(i[0])
            file_name = f'{i[1]}Repository.java'
            createInfrastructure(file_name, json.loads(rows))
        return render_template('env.html', rows=rows)
    return render_template('env.html', rows="""[
                ['ENV_DEV', '1', '', ''],
                ['ENV_TEST', '', '1', ''],
                ['ENV_PROD', '', '', '1'],
                ['DB_HOST', 'sqliteUser', 'testUser', 'prodUser'],
                ['DB_USER', 'devUser', 'testUser', 'prodUser'],
                ['DB_PASSWORD', 'devPass', 'testPass', 'prodPass']
            ]""".replace("'", "\""))

@app.route('/presentation', methods=["GET", "POST"])
def presentation():
    if request.method == "POST":
        rows = request.form["rows"]
        import json
        from sugumi_service import createPresentation
        print(json.loads(rows))
        for i in json.loads(rows):
            print(i[0])
            file_name = f'{i[2]}.html'
            createPresentation(file_name, json.loads(rows))
            createPresentation(f'{i[2]}Form.java', i[3])
            createPresentation(f'{i[2]}Controller.java', i[3])
        return render_template('presentation.html', rows=rows)
    return render_template('presentation.html', rows="""[
                ['ログイン', '/login', 'Login',''],
                ['メニュー', '/menu', 'Menu',''],
                ['ユーザー一覧', '/user/list', 'UserList',''],
                ['ユーザー登録', '/user/register', 'UserRegister',''],
                ['ユーザー詳細', '/user/detail/<id>', 'UserDetail',''],
                ['ディーラー一覧', '/user/list', 'UserList',''],
                ['ディーラー登録', '/user/register', 'UserRegister',''],
                ['ディーラー詳細', '/user/detail/<id>', 'UserDetail',''],
                ['プレゼンテーション層生成', '/presentation', 'Presentation','クラスファイル作成:createHtmlFormController, ER図作成:createEr'],
                ['アプリケーション層生成', '/application', 'Application','クラスファイル作成:createService, ER図作成:createEr'],
                ['インフラストラクチャ層生成', '/infrastructure', 'Infrastructure','クラスファイル作成:createRepository, ER図作成:createEr']
            ]""".replace("'", "\""))

from dotenv import load_dotenv
load_dotenv()

@app.route('/application', methods=["GET", "POST"])
def  application():
    if request.method == "POST":
        rows = request.form["rows"]
        src_root_path = Path(request.form["src_root_path"])
        test_root_path = Path(request.form["test_root_path"])
        import json
        print(json.loads(rows))

        # 受け取った内容を元にアプリケーション層作成
        from sugumi_service import create_application
        create_application(src_root_path=src_root_path, test_root_path=test_root_path)

        # ページを返却
        print(request.form)
        return render_template('application.html',form=request.form, rows=rows)
    form = {
        'src_root_path': os.environ['SRC_ROOT_PATH'],
        'test_root_path': os.environ['TEST_ROOT_PATH']
    }# こんなふうにformを辞書で作成してもいいしオブジェクトで渡してもいい。これは便利!
    return render_template('application.html', form = form, rows="""[
                ['機能登録', 'User', 'register', '1'],
                ['機能更新', 'User', 'update', '2'],
                ['機能削除', 'User', 'delete', '3']
            ]""".replace("'", "\""))

@app.route('/infrastructure', methods=["GET", "POST"])
def infrastructure():
    if request.method == "POST":
        rows = request.form["rows"]
        print(rows)
        import json
        from sugumi_service import createInfrastructure
        for i in json.loads(rows):
            print(i[0])
            file_name = f'{i[1]}Repository.java'
            createInfrastructure(file_name, json.loads(rows))
        return render_template('infrastructure.html', rows=rows)
    return render_template('infrastructure.html', rows="""[
                ['infrastructure', 'infrastructure', 'Infrastructure', 'Integer:id INT(3), String:type_name VARCHAR(50), String:table_name VARCHAR(50)'],
                ['presentation', 'presentation', 'Presentation', 'Integer:id INT(3), String:screen_name VARCHAR(50)'],
                ['application', 'application', 'Application', 'Integer:id INT(3), String:function_name VARCHAR(50)']
            ]""".replace("'", "\""))

@app.route('/screen/', methods=["GET"])
def screen():
    form = Form()
    return render_template('screen.html', form=form)

from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, ValidationError

class Form(FlaskForm):
    user_name = StringField('文字列')
    email = TextAreaField('テキスト')
    rows = StringField('文字列')
    
    def validate_user_name(self, user_name):
        '''
        - 未入力 禁止
        - 文字数9文字以上 禁止
        - 「-」 禁止
        '''
        if user_name.data == '':
            raise ValidationError('値を入力してください。')
        
        if len(user_name.data) > 8:
            raise ValidationError('値を8文字以内で入力してください。')
        
        if '-' in user_name.data:
            raise ValidationError('「-」の入力は禁止されています。')
    
    def validate_email(self, email):
        '''
        - 未入力 禁止
        - 文字数20文字未満 禁止
        '''
        if email.data == '':
            raise ValidationError('値を入力してください。')
        
        if len(email.data) < 20:
            raise ValidationError('値を20文字以上入力してください。')

@app.route('/screen', methods=["POST"])
def create():
    form = Form()
    #form.email = 'ここで代入
    ok = form.validate_on_submit()
    if ok:
        title = 'バリデーションを通過しました'
        return render_template('screen.html', form=form, title=title)
    else:
        title = 'バリデーションを通過できませんでした'
        return render_template('screen.html', form=form, title=title)

if __name__=='__main__':
    app.run(debug=True)
