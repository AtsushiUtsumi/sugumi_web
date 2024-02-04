# SUGUMI-WEB自身のインフラストラクチャ層
# 作成中のアプリのプロパティとかテーブル的なものを保存して

# 事前に「pg_config.exe」(Postgresqlをインストールしたフォルダ内の「bin」の中にある)のPATHを通しておくこと

# 帰ったらこれをメソッド化すること

import psycopg2

# PostgreSQLに接続

def execute(query: str):
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

execute(create_table_query)

# Repository実装
from sugumi_domain import ProjectInfo, ProjectInfoRepository
class SqliteProjectInfoRepository(ProjectInfoRepository):
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
        rs.append(ProjectInfo(5555))# とりあえず適当なIDのものを取得して返却
        rs.append(ProjectInfo(7777))# とりあえず適当なIDのものを取得して返却
        print('実装通っている')
        print(rs[0].id)
        print(rs[1].id)
        return rs