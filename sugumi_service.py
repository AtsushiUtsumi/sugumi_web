# このモジュールはsugumiの中ではアプリケーション層にあたる。
# メソッド数が少ないので1モジュールで済ませている

# 仮の1モジュールのsugumiあとで本物のsugumiかxuanzhuanに交換する
from pathlib import Path

def createPresentation(file_name, content):
    print(file_name + 'を作成')
    file = open(f'output/{file_name}', 'w')
    for row in content:
        file.write(str(row) + '<br>\n')
    file.close()

def createApplication(file_name, content):
    print(file_name + 'を作成')
    file = open(f'output/{file_name}', 'w')
    for row in content:
        file.write(str(row) + '<br>\n')
    file.close()
    from xuanzhuan.layer.application.java import ApplicationJava
    app = ApplicationJava('fuga', Path('E:\Desktop\main'), Path('E:\Desktop\test'))
    from xuanzhuan.layer.application.use_case import UseCase
    tmp = UseCase('ユーザー登録処理', 'registerUser')
    app.add_use_case(tmp)
    tmp = UseCase('ユーザー更新処理', 'updateUser')
    app.add_use_case(tmp)

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
    column_list: list[Column] = []

def createInfrastructure(file_name, content):
    print(file_name + 'を作成')
    file = open(f'output/{file_name}', 'w')
    for row in content:
        file.write(str(row) + '<br>\n')
    file.close()
    from xuanzhuan.layer.application.java import ApplicationJava
    app = ApplicationJava('fuga', Path('E:\Desktop\main'), Path('E:\Desktop\test'))
    Table('ほげ','hoge',Column('ユーザー名', 'user_name', 'VARCHAR(20)', 'UNIQUE', 'userName', 'String'))
    tmp = {'package': 'hoge', }