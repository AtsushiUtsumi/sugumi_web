# 単体のスクリプトで確認する

import sqlite3
conn = sqlite3.connect('sugumi.db')
c = conn.cursor()
for a in c.execute("select name from sqlite_master where type='table'"):
    print(a)
conn.close()
