# SUGUMI-WEB自身のインフラストラクチャ層
# 作成中のアプリのプロパティとかテーブル的なものを保存して

# 事前に「pg_config.exe」(Postgresqlをインストールしたフォルダ内の「bin」の中にある)のPATHを通しておくこと

import sqlite3

def sqlite_execute(query: str):
    con = sqlite3.connect("sugumi.db")
    cur = con.cursor()
    cur.execute(query)
    con.commit()
    cur.close()
    con.close()

import psycopg2

# PostgreSQLに接続

def postgresql_execute(query: str):
    connection = psycopg2.connect('postgresql://postgres:password@localhost:5432/sugumi')
    cursor = connection.cursor()
    cursor.execute(query)
    connection.commit()
    cursor.close()
    connection.close()

create_table_query = '''
CREATE TABLE IF NOT EXISTS sample_table (
    screen_name VARCHAR(255),
    url VARCHAR(255),
    class_name VARCHAR(255),
    function VARCHAR(255)
)
'''

#postgresql_execute(create_table_query)

# Repository実装
from sugumi_domain import PresentationInfo, PresentationInfoRepository, ProjectInfo, ProjectInfoRepository
class SqliteProjectInfoRepository(ProjectInfoRepository):
    def create_table(self):
        print('テーブル(Sqlite)')
        sqlite_execute(create_table_query)
        return
    def insert(self, entity: ProjectInfo):
        return
    def updete(self, entity: ProjectInfo):
        return
    def delete(self, id: int):
        return
    def find(self, id: int) -> ProjectInfo:
        return
    def find_all(self) -> list[ProjectInfo]:
        rs = list()
        rs.append(ProjectInfo(555))# とりあえず適当なIDのものを取得して返却
        rs.append(ProjectInfo(777))# とりあえず適当なIDのものを取得して返却
        print('実装通っている')
        print(rs[0].id)
        print(rs[1].id)
        return rs

class PostgresqlProjectInfoRepository(ProjectInfoRepository):
    def create_table(self):
        print('テーブル(Postgresql)')
        create_table_query = '''
CREATE TABLE IF NOT EXISTS project_info (
    id INT,
    project_name VARCHAR(255),
    output_path  VARCHAR(255),
    group_id VARCHAR(255),
    framework VARCHAR(255),
    language VARCHAR(20)
)
'''
        print(create_table_query)
        postgresql_execute(create_table_query)
        return
    def insert(self, entity: ProjectInfo):
        # TODO: 今はIDのみ登録している
        insert_table_query = f'INSERT INTO project_info (id) VALUES ({entity.id})'
        print(insert_table_query)
        postgresql_execute(insert_table_query)
        return
    def updete(self, entity: ProjectInfo):
        return
    def delete(self, id: int):
        return
    def find(self, id: int) -> ProjectInfo:
        return
    def find_all(self) -> list[ProjectInfo]:
        rs = list()
        rs.append(ProjectInfo(5555))# とりあえず適当なIDのものを取得して返却
        rs.append(ProjectInfo(7777))# とりあえず適当なIDのものを取得して返却
        print('実装通っている')
        print(rs[0].id)
        print(rs[1].id)
        return rs
    




create_table_query = '''
CREATE TABLE IF NOT EXISTS sample_table (
    screen_name VARCHAR(255),
    url VARCHAR(255),
    class_name VARCHAR(255),
    function VARCHAR(255)
)
'''

#postgresql_execute(create_table_query)

# Repository実装
from sugumi_domain import ClassInfo, ClassInfoRepository
class SqliteClassInfoRepository(ClassInfoRepository):
    def create_table(self):
        print('テーブル(Sqlite)')
        create_table_query = '''
CREATE TABLE IF NOT EXISTS CLASS_INFO (
    id INT,
    Class_name VARCHAR(255),
    output_path  VARCHAR(255),
    group_id VARCHAR(255),
    framework VARCHAR(255),
    language VARCHAR(20)
)
'''
        sqlite_execute(create_table_query)
        return
    def insert(self, entity: ClassInfo):
        return
    def updete(self, entity: ClassInfo):
        return
    def delete(self, id: int):
        return
    def find(self, id: int) -> ClassInfo:
        return
    def find_all(self) -> list[ClassInfo]:
        rs = list()
        rs.append(ClassInfo(555))# とりあえず適当なIDのものを取得して返却
        rs.append(ClassInfo(777))# とりあえず適当なIDのものを取得して返却
        print('実装通っている')
        print(rs[0].id)
        print(rs[1].id)
        return rs

class PostgresqlClassInfoRepository(ClassInfoRepository):
    def create_table(self):
        print('テーブル(Postgresql)')
        create_table_query = '''
CREATE TABLE IF NOT EXISTS CLASS_INFO (
    id INT,
    Class_name VARCHAR(255),
    output_path  VARCHAR(255),
    group_id VARCHAR(255),
    framework VARCHAR(255),
    language VARCHAR(20)
)
'''
        print(create_table_query)
        postgresql_execute(create_table_query)
        return
    def insert(self, entity: ClassInfo):
        # TODO: 今はIDのみ登録している
        insert_table_query = f'INSERT INTO Class_info (id) VALUES ({entity.id})'
        print(insert_table_query)
        postgresql_execute(insert_table_query)
        return
    def updete(self, entity: ClassInfo):
        return
    def delete(self, id: int):
        return
    def find(self, id: int) -> ClassInfo:
        return
    def find_all(self) -> list[ClassInfo]:
        rs = list()
        rs.append(ClassInfo(5555))# とりあえず適当なIDのものを取得して返却
        rs.append(ClassInfo(7777))# とりあえず適当なIDのものを取得して返却
        print('実装通っている')
        print(rs[0].id)
        print(rs[1].id)
        return rs
    



















class SqlitePresentationInfoRepository(PresentationInfoRepository):
    def create_table(self):
        print('テーブル作成(Sqlite)')
        create_table_query = '''
CREATE TABLE IF NOT EXISTS PRESENTATION_INFO (
    url TEXT,
    screen_name TEXT,
    class_name TEXT,
    action TEXT
)
'''
        sqlite_execute(create_table_query)
        return
    def insert(self, entity: PresentationInfo):
        # TODO: 今は画面名のみ登録している
        insert_table_query = f'INSERT INTO PRESENTATION_INFO (screen_name, url, class_name, action) VALUES (\'{entity.screen_name}\',\'{entity.url}\',\'{entity.class_name}\',\'{entity.action}\')'
        print(insert_table_query)
        sqlite_execute(insert_table_query)
        return
    def updete(self, entity: PresentationInfo):
        return
    def delete(self, id: int):
        return
    def find(self, id: int) -> PresentationInfo:
        return
    def find_all(self) -> list[PresentationInfo]:
        rs = list()
        rs.append(PresentationInfo('','','',''))
        print('実装通っている')
        print(rs[0].id)
        print(rs[1].id)
        return rs

class PostgresqlPresentationInfoRepository(PresentationInfoRepository):
    def create_table(self):
        print('テーブル(Postgresql)')
        create_table_query = '''
CREATE TABLE IF NOT EXISTS PRESENTATION_INFO (
    url VARCHAR(255),
    screen_name VARCHAR(255),
    class_name VARCHAR(255),
    action VARCHAR(255)
)
'''
        print(create_table_query)
        postgresql_execute(create_table_query)
        return
    def insert(self, entity: PresentationInfo):
        # TODO: 今はIDのみ登録している
        insert_table_query = f'INSERT INTO PRESENTATION_INFO (id) VALUES ({entity.url})'
        print(insert_table_query)
        postgresql_execute(insert_table_query)
        return
    def updete(self, entity: PresentationInfo):
        return
    def delete(self, id: int):
        return
    def find(self, id: int) -> PresentationInfo:
        return
    def find_all(self) -> list[PresentationInfo]:
        rs = list()
        rs.append(PresentationInfo('','','',''))
        print('実装通っている')
        print(rs[0].id)
        print(rs[1].id)
        return rs