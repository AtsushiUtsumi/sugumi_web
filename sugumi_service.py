# このモジュールはsugumiの中ではアプリケーション層にあたる。
# メソッド数が少ないので1モジュールで済ませている

# 仮の1モジュールのsugumiあとで本物のsugumiかxuanzhuanに交換する
from pathlib import Path

from injector import Injector, Module

from sugumi_domain import ProjectInfo, ProjectInfoRepository
from sugumi_infrastructure import PostgresqlProjectInfoRepository, SqliteProjectInfoRepository

def createPresentation(file_name, content):
    print(file_name + 'を作成')
    file = open(f'output/{file_name}', 'w')
    for row in content:
        file.write(str(row) + '<br>\n')
    file.close()

def createApplication(file_name, content):
    print(file_name + 'を作成')
    file = open(f'output/{file_name}', 'w')
    for row in content:
        file.write(str(row) + '<br>\n')
    file.close()
    from xuanzhuan.layer.application.java import ApplicationJava
    app = ApplicationJava('fuga', Path('E:\\Desktop\\main'), Path('E:\\Desktop\\test'))
    from xuanzhuan.layer.application.use_case import UseCase
    tmp = UseCase('ユーザー登録処理', 'registerUser')
    app.add_use_case(tmp)
    tmp = UseCase('ユーザー更新処理', 'updateUser')
    app.add_use_case(tmp)

from dataclasses import dataclass
@dataclass
class Column:
    description: str
    name: str
    datatype: str
    constraint: str = ''
    lang_name: str = ''
    lang_type: str = ''

@dataclass
class Table:
    description: str
    name: str
    column_list: []

def createInfrastructure(file_name, content):
    print(file_name + 'を作成')
    file = open(f'output/{file_name}', 'w')
    for row in content:
        file.write(str(row) + '<br>\n')
    file.close()
    from xuanzhuan.layer.application.java import ApplicationJava
    project_name = 'dao'
    application_root = Path(f'E:\\Desktop\\{project_name}\\app\\src\\main\\java\\dao')
    application_root_test = Path(f'E:\\Desktop\\{project_name}\\app\\src\\test\\java\\dao')
    app = ApplicationJava(project_name, application_root, application_root_test)
    from xuanzhuan.layer.application.use_case import UseCase
    use_case = UseCase('ユーザー登録機能', 'registerUser', [], [], True)# これだと1機能につき1クラスしか作成できないがいいのか
    app.add_use_case(use_case)
    use_case = UseCase('ユーザー検索機能', 'searchUser', [], [], True)# これだと1機能につき1クラスしか作成できないがいいのか
    app.add_use_case(use_case)
    use_case = UseCase('ユーザー更新機能', 'updateUser', [], [], True)# これだと1機能につき1クラスしか作成できないがいいのか
    app.add_use_case(use_case)
    use_case = UseCase('ユーザー削除機能', 'deleteUser', [], [], True)# これだと1機能につき1クラスしか作成できないがいいのか
    app.add_use_case(use_case)

create_table_query = '''
CREATE TABLE IF NOT EXISTS sample_table (
    screen_name VARCHAR(255),
    url VARCHAR(255),
    class_name VARCHAR(255),
    function VARCHAR(255)
)
'''

def build_create_table_query(table: Table):
    tmp = []
    from sugumi_infrastructure import postgresql_execute
    for i in table.column_list:
        tmp.append(i.name + ' ' + i.datatype)
    postgresql_execute('CREATE TABLE IF NOT EXISTS ' + table.name + '(' + ', '.join(tmp) + ')')

build_create_table_query(Table('売上伝票', '"table_info"', [Column('ユーザー名', 'user_name', 'VARCHAR(20)', 'UNIQUE', 'userName', 'String')]))




# RepositoryにどっちをDIするかを選択(TODO:あとで設定に移す)
class SqliteDiModule(Module):
    def configure(self, binder):
        binder.bind(ProjectInfoRepository, to=SqliteProjectInfoRepository)

class PostgresqlDiModule(Module):
    def configure(self, binder):
        binder.bind(ProjectInfoRepository, to=PostgresqlProjectInfoRepository)

class ProjectInfoService:
    def __init__(self) -> None:
        injector = Injector([SqliteDiModule()])# 「Sqlite」使いたければこっち
        # injector = Injector([PostgresqlDiModule()])# 「Postgresql」使いたければこっち
        self.projectInfoRepository = injector.get(ProjectInfoRepository)# この代入はシングルトン
        print('DI完了')
    def create_table(self):
        self.projectInfoRepository.create_table()
        return
    def insert(self, entity: ProjectInfo):
        self.projectInfoRepository.insert(entity)
        return
    def updete(self, entity: ProjectInfo):
        self.projectInfoRepository.insert(entity)
        return
    def delete(self, id: int):
        self.projectInfoRepository.delete(id)
        return
    def find(self, id: int) -> ProjectInfo:
        return self.projectInfoRepository.find(id)
    def find_all(self) -> list[ProjectInfo]:
        return self.projectInfoRepository.find_all()