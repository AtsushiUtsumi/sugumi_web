# 単体のスクリプトで確認する

import sqlite3
conn = sqlite3.connect('sugumi.db')
c = conn.cursor()
for a in c.execute("select name from sqlite_master where type='table'"):
    print(a)

c.execute("CREATE TABLE IF NOT EXISTS column_info (project_id INT, table_name TEXT, column_name TEXT, constraints TEXT, class_name TEXT, package_name TEXT, PRIMARY KEY (project_id, table_name, column_name))")
c.execute("INSERT INTO column_info VALUES(1, 'テーブル名', 'カラム名', '制約', 'クラス名', 'パッケージ名')")
c.execute("INSERT INTO column_info VALUES(1, 'user', 'id', '', 'User', 'user')")
c.execute("INSERT INTO column_info VALUES(1, 'user', 'name', '', 'User', 'user')")
c.execute("INSERT INTO column_info VALUES(1, 'user', 'age', '', 'User', 'user')")
c.execute("INSERT INTO column_info VALUES(1, 'user', 'email', '', 'User', 'user')")

c.execute("CREATE TABLE IF NOT EXISTS internationalization (id TEXT NOT NULL, ja TEXT NOT NULL, en TEXT NOT NULL, PRIMARY KEY (id))")
c.execute("CREATE TABLE IF NOT EXISTS presentation_info (url TEXT, screen_name TEXT, class_name TEXT, action TEXT)")
c.execute("CREATE TABLE IF NOT EXISTS project_info (id INT, project_name TEXT, output_path TEXT, group_id TEXT, framework TEXT, language TEXT, PRIMARY KEY (id))")
c.execute("CREATE TABLE IF NOT EXISTS table_info (table_id INT, table_name TEXT, project_id INT,  columns_info TEXT, PRIMARY KEY (table_id))")
conn.commit()
conn.close()
