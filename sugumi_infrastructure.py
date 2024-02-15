# SUGUMI-WEB自身のインフラストラクチャ層
# 作成中のアプリのプロパティとかテーブル的なものを保存して

# 事前に「pg_config.exe」(Postgresqlをインストールしたフォルダ内の「bin」の中にある)のPATHを通しておくこと

import sqlite3

def sqlite_execute(query: str):
    con = sqlite3.connect("sugumi.db")
    cur = con.cursor()
    CREATE_TABLE = "CREATE TABLE IF NOT EXISTS akari (t1 TEXT, t2 NUMERIC, t3 INTEGER, t4 REAL, t5 BLOB);"
    SELECT_NAME_FROM_MASTER = "SELECT name FROM sqlite_master;"
    cur.execute(CREATE_TABLE)
    res = cur.execute(SELECT_NAME_FROM_MASTER)

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
from sugumi_domain import ProjectInfo, ProjectInfoRepository
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