# 単体のスクリプトで確認する

import sqlite3
conn = sqlite3.connect('sugumi.db')
c = conn.cursor()
for a in c.execute("select name from sqlite_master where type='table'"):
    print(a)

c.execute("CREATE TABLE IF NOT EXISTS column_info (project_id INT, table_name TEXT, column_name TEXT, constraints TEXT, class_name TEXT, package_name TEXT)")
c.execute("INSERT INTO column_info VALUES(1, 'a', 'b', 'c', 'd', 'e')")
c.execute("INSERT INTO column_info VALUES(2, 'aa', 'bb', 'cc', 'dd', 'ee')")

c.execute("CREATE TABLE IF NOT EXISTS internationalization (id TEXT NOT NULL, ja TEXT NOT NULL, en TEXT NOT NULL, PRIMARY KEY (id))")
c.execute("CREATE TABLE IF NOT EXISTS presentation_info (url TEXT, screen_name TEXT, class_name TEXT, action TEXT)")
c.execute("CREATE TABLE IF NOT EXISTS project_info (id INT, project_name TEXT, output_path TEXT, group_id TEXT, framework TEXT, language TEXT, PRIMARY KEY (id))")
c.execute("CREATE TABLE IF NOT EXISTS table_info (table_id INT, table_name TEXT, project_id INT,  columns_info TEXT, PRIMARY KEY (table_id))")
#c.execute("INSERT INTO table_info VALUES(2, 'infrastructure2', 1, 'Integer:id INT(3), String:type_name VARCHAR(50), String:table_name VARCHAR(50)')")

# for a in c.execute("select * from table_info"):
#     print(a)
conn.commit()
conn.close()
