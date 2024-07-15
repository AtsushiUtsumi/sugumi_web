# 単体のスクリプトで確認する

import sqlite3
conn = sqlite3.connect('sugumi.db')
c = conn.cursor()
print('テーブル一覧')
for a in c.execute("select name from sqlite_master where type='table'"):
    print(a[0])
c.execute("DROP TABLE IF EXISTS column_info")
c.execute("CREATE TABLE IF NOT EXISTS column_info (project_id INT, table_name TEXT, column_name TEXT, constraints TEXT, package_name TEXT, class_name TEXT, variable_name TEXT, PRIMARY KEY (project_id, table_name, column_name))")
#c.execute("INSERT INTO column_info VALUES(1, 'テーブル名', 'カラム名', '制約', 'パッケージ名', 'クラス名', '変数名')")
c.execute("INSERT INTO column_info VALUES(1, 'user', 'id', '', 'user', 'user', 'id')")
c.execute("INSERT INTO column_info VALUES(1, 'user', 'name', '', 'user', 'user', 'name')")
c.execute("INSERT INTO column_info VALUES(1, 'user', 'age', '', 'user', 'user', 'age')")
c.execute("INSERT INTO column_info VALUES(1, 'user', 'email', '', 'user', 'user', 'email')")

c.execute("INSERT INTO column_info VALUES(1, 'call', 'ninniku', '', 'call', 'call', 'ninniku')")
c.execute("INSERT INTO column_info VALUES(1, 'call', 'yasai', '', 'call', 'call', 'yasai')")
c.execute("INSERT INTO column_info VALUES(1, 'call', 'abura', '', 'call', 'call', 'abura')")
c.execute("INSERT INTO column_info VALUES(1, 'call', 'karame', '', 'call', 'call', 'karame')")

c.execute("CREATE TABLE IF NOT EXISTS internationalization (id TEXT NOT NULL, ja TEXT NOT NULL, en TEXT NOT NULL, PRIMARY KEY (id))")
c.execute("CREATE TABLE IF NOT EXISTS presentation_info (url TEXT, screen_name TEXT, class_name TEXT, action TEXT)")

c.execute("DROP TABLE IF EXISTS project_info")
c.execute("CREATE TABLE IF NOT EXISTS project_info (id INT, project_name TEXT, output_path TEXT, group_id TEXT, framework TEXT, language TEXT, PRIMARY KEY (id))")
c.execute("INSERT INTO project_info VALUES(1, 'jiro', '', 'com.au', 'spring', 'java')")

c.execute("CREATE TABLE IF NOT EXISTS table_info (table_id INT, table_name TEXT, project_id INT,  columns_info TEXT, PRIMARY KEY (table_id))")
conn.commit()
conn.close()
