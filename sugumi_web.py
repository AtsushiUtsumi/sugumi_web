# このモジュールはsugumiの中ではプレゼンテーション層にあたる。
# メソッド数が少ないので1モジュールで済ませている

# モジュールを追加
import json
import os
from pathlib import Path
from flask import Flask, redirect, render_template, request
from injector import Injector, Module
from sugumi_domain import PresentationInfo, PresentationInfoRepository, ProjectInfo, ProjectInfoRepository, TableInfo, TableInfoRepository
from sugumi_infrastructure import PostgresqlPresentationInfoRepository, PostgresqlProjectInfoRepository, PostgresqlTableInfoRepository, SqlitePresentationInfoRepository, SqliteProjectInfoRepository, SqliteTableInfoRepository

from sugumi_service import ProjectInfoService

app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret_key'# CSRFに必要かも

# 以下別モジュールに移すか
class SqliteDiModule(Module):
    def configure(self, binder):
        binder.bind(ProjectInfoRepository, to=SqliteProjectInfoRepository)
        binder.bind(PresentationInfoRepository, to=SqlitePresentationInfoRepository)
        binder.bind(TableInfoRepository, to=SqliteTableInfoRepository)

class PostgresqlDiModule(Module):
    def configure(self, binder):
        binder.bind(ProjectInfoRepository, to=PostgresqlProjectInfoRepository)
        binder.bind(PresentationInfoRepository, to=PostgresqlPresentationInfoRepository)
        binder.bind(TableInfoRepository, to=PostgresqlTableInfoRepository)
        

injector = Injector([SqliteDiModule()])
# injector = Injector([PostgresqlDiModule()])

@app.route('/')
def menu():
    projectInfoService = injector.get(ProjectInfoRepository)# TODO: ここ名前を変更が必要では?
    # print(projectInfoService)
    rs = projectInfoService.find_all()
    # print(rs[0].id)
    projectInfoService.create_table()
    projectInfoService.insert(ProjectInfo(1234))
    return render_template('menu.html')

@app.route('/env', methods=["GET", "POST"])
def env():
    if request.method == "POST":
        rows = request.form["rows"]
        # print(rows)
        import json
        from sugumi_service import createInfrastructure
        for i in json.loads(rows):
            # print(i[0])
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
        # print(json.loads(rows))
        repository = injector.get(PresentationInfoRepository)
        repository.create_table()# テーブル作成
        for i in json.loads(rows):# データを永続化
            entity = PresentationInfo(i[0], i [1], i[2], i[3])
            repository.insert(entity=entity)
            file_name = f'{i[2]}.html'
            #createPresentation(file_name, json.loads(rows))
            #createPresentation(f'{i[2]}Form.java', i[3])
            #createPresentation(f'{i[2]}Controller.java', i[3])
        return render_template('presentation.html', form = request.form, rows = rows)
    form = {
        'src_root_path': os.environ['SRC_ROOT_PATH'],
        'test_root_path': os.environ['TEST_ROOT_PATH']
    }
    return render_template('presentation.html', form = form, rows="""[
                ['ログイン', '/login', 'Login',''],
                ['メニュー', '/menu', 'Menu',''],
                ['ユーザー一覧', '/user/list', 'UserList',''],
                ['ユーザー登録', '/user/register', 'UserRegister',''],
                ['ユーザー詳細', '/user/detail/<id>', 'UserDetail',''],
                ['ディーラー一覧', '/user/list', 'UserList',''],
                ['ディーラー登録', '/user/register', 'UserRegister',''],
                ['ディーラー詳細', '/user/detail/<id>', 'UserDetail',''],
                ['プロジェクト一覧', '/project', '',''],
                ['プロジェクト新規作成', '/project/register', '',''],
                ['プロジェクト詳細', '/project/<project_id>', '',''],
                ['プレゼンテーション層生成', '/project/<project_id>/presentation', 'Presentation','クラスファイル作成:createHtmlFormController'],
                ['アプリケーション層生成', '/project/<project_id>/application', 'Application','クラスファイル作成:createService'],
                ['インフラストラクチャ層生成', '/project/<project_id>/infrastructure', 'Infrastructure','クラスファイル作成:createRepository, ER図作成:createEr'],
                ['ドメイン層生成', '/project/<project_id>/domain', 'Domain','クラスファイル作成:createValue, ER図作成:createEr']
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
        # print(json.loads(rows))

        # 受け取った内容を元にアプリケーション層作成
        from sugumi_service import create_application
        create_application(src_root_path=src_root_path, test_root_path=test_root_path)

        # ページを返却
        # print(request.form)
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
        # print(rows)
        import json
        from sugumi_service import createInfrastructure
        for i in json.loads(rows):
            # print(i[0])
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


@app.route('/project/<int:id>')
def project_detail(id):
    repository: ProjectInfoRepository = injector.get(ProjectInfoRepository)
    entity = ProjectInfo(id)
    entity = repository.find(id=id)
    # print(entity.project_name + 'プロジェクトを開きます')
    return render_template('project/detail.html', entity=entity)

# パスパラメータでプロジェクトの機能一覧を開く
@app.route('/project/<int:id>/application')
def project_service(id):
    repository: ProjectInfoRepository = injector.get(ProjectInfoRepository)
    entity = ProjectInfo(id)
    entity = repository.find(id=id)
    # print(entity.project_name + 'の機能一覧を開きます')
    if request.method == "POST":
        rows = request.form["rows"]
        src_root_path = Path(request.form["src_root_path"])
        test_root_path = Path(request.form["test_root_path"])
        import json
        # print(json.loads(rows))

        # 受け取った内容を元にアプリケーション層作成
        from sugumi_service import create_application
        create_application(src_root_path=src_root_path, test_root_path=test_root_path)

        # ページを返却
        # print(request.form)
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

class ProjectForm:
    def __init__(self) -> None:# TODO : リモートリポジトリを追加する
        self.id = ''
        self.project_name = 'プロジェクト名(仮)'
        self.output_path = ''
        self.group_id = ''
        self.framework = 'フレームワーク(仮)'
        self.language = 'java'
        pass

@app.route('/project', methods=["GET", "POST"])
def project():
    return render_template('project/list.html', form = ProjectForm())

@app.route('/project/register', methods=["GET", "POST"])
def project_register():
    if request.method == "GET":
        return render_template('project/register.html', form = ProjectForm())
    form = request.form
    # print('選択された言語の拡張子は[' + request.form['language'] + ']です')
    # print('プロジェクト名は[' + request.form['project_name'] + ']です')
    # print('フレームワークは[' + request.form['framework'] + ']です')
    # 登録処理
    repository: ProjectInfoRepository = injector.get(ProjectInfoRepository)
    repository.create_table()
    id = 0# TODO : 発番処理
    while repository.find(id) != None:
        id += 1
    entity = ProjectInfo(id)
    entity.language = form['language']
    entity.framework = form['framework']
    entity.project_name = form['project_name']
    repository.insert(entity=entity)
    # 作成したプロジェクトを即開く
    return redirect(f'/project/{id}')

# ドメイン層作成
@app.route('/project/<int:project_id>/domain', methods=["GET", "POST"])
def domain(project_id):
    if request.method == "POST":
        rows = request.form["rows"]
        src_root_path = Path(request.form["src_root_path"])
        test_root_path = Path(request.form["test_root_path"])
        import json
        # print(json.loads(rows))

        # 受け取った内容を元にアプリケーション層作成
        from sugumi_service import create_application
        create_application(src_root_path=src_root_path, test_root_path=test_root_path)

        # ページを返却
        # print(request.form)
        return render_template('application.html',form=request.form, rows=rows)
    form = {
        'src_root_path': os.environ['SRC_ROOT_PATH'],
        'test_root_path': os.environ['TEST_ROOT_PATH']
    }# こんなふうにformを辞書で作成してもいいしオブジェクトで渡してもいい。これは便利!
    return render_template('domain.html', form = form, rows="""[
                ['プロジェクト情報', 'ProjectInto', 'register', '1'],
                ['テーブル情報', 'User', 'update', '2'],
                ['画面情報', '', 'delete', '3']
            ]""".replace("'", "\""))

# プロジェクト個別のインフラストラクチャ層を開く
@app.route('/project/<int:project_id>/infrastructure', methods=["GET", "POST"])
def project_infrastructure(project_id: int):
    if request.method == "POST":
        rows = request.form["rows"]
        # print(rows)
        import json
        from sugumi_service import createInfrastructure
        for i in json.loads(rows):
            # print(i[0])
            file_name = f'{i[1]}Repository.java'
            createInfrastructure(file_name, json.loads(rows))
        return render_template('infrastructure.html', rows=rows)
    return render_template('infrastructure.html', rows="""[
                ['infrastructure', 'infrastructure', 'Infrastructure', 'Integer:id INT(3), String:type_name VARCHAR(50), String:table_name VARCHAR(50)'],
                ['presentation', 'presentation', 'Presentation', 'Integer:id INT(3), String:screen_name VARCHAR(50)'],
                ['application', 'application', 'Application', 'Integer:id INT(3), String:function_name VARCHAR(50)']
            ]""".replace("'", "\""))


# ここからがマスタ
@app.route('/project/<int:project_id>/screen', methods=["GET", "POST"])
def project_screen(project_id: int):
    template_file = 'screen.html'
    if request.method == "POST":
        rows = request.form["rows"]
        return render_template(template_file, rows=rows, project_id=project_id)
    return render_template(template_file, rows="""[
                ['ログイン', '/login', 'Login',''],
                ['メニュー', '/menu', 'Menu',''],
                ['ユーザー一覧', '/user/list', 'UserList',''],
                ['ユーザー登録', '/user/register', 'UserRegister',''],
                ['ユーザー詳細', '/user/detail/<id>', 'UserDetail',''],
                ['ディーラー一覧', '/user/list', 'UserList',''],
                ['ディーラー登録', '/user/register', 'UserRegister',''],
                ['ディーラー詳細', '/user/detail/<id>', 'UserDetail',''],
                ['プロジェクト一覧', '/project', '',''],
                ['プロジェクト新規作成', '/project/register', '',''],
                ['プロジェクト詳細', '/project/<project_id>', '',''],
                ['プレゼンテーション層生成', '/project/<project_id>/presentation', 'Presentation','クラスファイル作成:createHtmlFormController'],
                ['アプリケーション層生成', '/project/<project_id>/application', 'Application','クラスファイル作成:createService'],
                ['インフラストラクチャ層生成', '/project/<project_id>/infrastructure', 'Infrastructure','クラスファイル作成:createRepository, ER図作成:createEr'],
                ['ドメイン層生成', '/project/<project_id>/domain', 'Domain','クラスファイル作成:createValue, ER図作成:createEr']
            ]""".replace("'", "\""), project_id=project_id)

@app.route('/project/<int:project_id>/screen/delete', methods=["POST"])
def project_screen_delete(project_id: int):
    template_file = 'screen.html'
    rows = request.form["rows"]
    return render_template(template_file, rows=rows, project_id=project_id)

@app.route('/project/<int:project_id>/screen/export', methods=["POST"])
def project_screen_export(project_id: int):
    template_file = 'screen.html'
    rows = request.form["rows"]
    return render_template(template_file, rows=rows, project_id=project_id)

@app.route('/project/<int:project_id>/database', methods=["GET", "POST"])
def project_database(project_id: int):
    template_file = 'database.html'
    repository = injector.get(TableInfoRepository)
    if request.method == "POST":
        rows = request.form["rows"]
        repository.delete_by_project_id(project_id)
        for row in json.loads(rows):
            entity = TableInfo(project_id, row[0])
            entity.columns_info = row[1]
            repository.insert(entity)#TODO: バルクインサートに修正する
        return render_template(template_file, rows=rows, project_id=project_id)
    entity_list = repository.find_all()# TODO: by_project_idに修正する
    rows = list()
    for entity in entity_list:
        rows.append([entity.table_name, entity.columns_info])
    return render_template(template_file, rows=str(rows).replace("'", "\""), project_id=project_id)
if __name__=='__main__':
    app.run(debug=True)

# 帰ったら「新規プロジェクト登録」と「プロジェクトを開く」を実装したい。株価チェックも
# 画面とテーブルのマスタ