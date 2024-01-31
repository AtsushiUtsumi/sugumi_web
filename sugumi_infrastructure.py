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
