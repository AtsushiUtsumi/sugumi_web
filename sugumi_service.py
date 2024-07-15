# このモジュールはsugumiの中ではアプリケーション層にあたる。
# メソッド数が少ないので1モジュールで済ませている

# 仮の1モジュールのsugumiあとで本物のsugumiかxuanzhuanに交換する
import os
from pathlib import Path

from injector import Injector, Module, inject

from sugumi_domain import ClassInfoRepository, ColumnInfoRepository, ProjectInfo, ProjectInfoRepository
from sugumi_infrastructure import PostgresqlProjectInfoRepository, SqliteProjectInfoRepository

def createPresentation(file_name, content):
    print(file_name + 'を作成')
    file = open(f'output/{file_name}', 'w')
    for row in content:
        file.write(str(row) + '<br>\n')
    file.close()

def create_application_file(file_name, content):# このメソッドはファイル単位で作るのか?
    print(file_name + 'を作成')
    file = open(f'output/{file_name}', 'w', encoding='UTF8')
    for row in content:
        file.write(str(row) + '<br>\n')
    file.close()
    return

from dotenv import load_dotenv
load_dotenv()

from xuanzhuan.layer.application.use_case import UseCase
def create_application(src_root_path: Path, test_root_path: Path, use_case_list: list[UseCase]):
    from xuanzhuan.layer.application.java import ApplicationJava
    app = ApplicationJava(os.environ['PACKAGE_NAME'], src_root_path, test_root_path)
    for use_case in use_case_list:
        app.add_use_case(use_case=use_case)

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
    column_list: list[Column]

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
    #postgresql_execute('CREATE TABLE IF NOT EXISTS ' + table.name + '(' + ', '.join(tmp) + ')')

#build_create_table_query(Table('売上伝票', '"table_info"', [Column('ユーザー名', 'user_name', 'VARCHAR(20)', 'UNIQUE', 'userName', 'String')]))




# RepositoryにどっちをDIするかを選択(TODO:あとで設定に移す)
class SqliteDiModule(Module):
    def configure(self, binder):
        binder.bind(ProjectInfoRepository, to=SqliteProjectInfoRepository)

class PostgresqlDiModule(Module):
    def configure(self, binder):
        binder.bind(ProjectInfoRepository, to=PostgresqlProjectInfoRepository)

class ProjectInfoService:
    @inject
    def __init__(self, repository: ProjectInfoRepository) -> None:
        self.repository = repository
        self.repository.create_table()# ここで何がインジェクションされているか
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

class ClassInfoService:
    @inject
    def __init__(self, repository: ClassInfoRepository) -> None:
        self.repository = repository
        self.repository.create_table()# ここで何がインジェクションされているか
        injector = Injector([SqliteDiModule()])# 「Sqlite」使いたければこっち
        # injector = Injector([PostgresqlDiModule()])# 「Postgresql」使いたければこっち
        self.projectInfoRepository = injector.get(ClassInfoRepository)# この代入はシングルトン
        print('DI完了')

class ColumnInfoService:
    def __init__(self, repository: ColumnInfoRepository) -> None:
        self.repository = repository
        print('DI完了')
    
    def create_crud(self, project_id: int):
        from sugumi_injector import injector
        pir: ProjectInfoRepository = injector.get(ProjectInfoRepository)
        pi = pir.find(id=project_id)
        print(pi)
        from xuanzhuan.layer.presentation.spring import PresentationSpring
        spring: PresentationSpring = PresentationSpring(os.environ['OUTPUT_ROOT_PATH'], pi.project_name, pi.group_id)# Springアプリケーション出力
        # TODO: プロジェクト情報から取得するように変更する
        column_info_list = self.repository.find_by_project_id(project_id=project_id)
        table_list = []
        table_name_set = set()
        for column_info in column_info_list:
            table_name_set.add(column_info.table_name)
        for table_name in table_name_set:
            if table_name == '':
                continue
            table = dict()
            table["name"] = table_name
            table["tableName"] = table_name
            table["columnList"] = []
            tmp = [c for c in column_info_list if c.table_name == table_name]# テーブル名毎にカラムリスト作成
            for c in tmp:
                table["columnList"].append({
                    "langType": "LocalDate",
                    "langName": c.variable_name,
                    "dbType": "Timestamp",
                    "dbName": c.column_name
                })
            table_list.append(table)
            # 今はテーブル名とカラム名を出力するのみ
        for table in table_list:
            spring.add_table(table=table)
        return
