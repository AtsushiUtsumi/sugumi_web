# 単体のスクリプトで確認する

import sqlite3
conn = sqlite3.connect('sugumi.db')
c = conn.cursor()
for a in c.execute("select name from sqlite_master where type='table'"):
    print(a)
c.execute("create table IF NOT EXISTS internationalization (id TEXT NOT NULL, ja TEXT NOT NULL, en TEXT NOT NULL, PRIMARY KEY (id))")
conn.close()
