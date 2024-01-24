# 仮の1モジュールのsugumiあとで本物のsugumiかxuanzhuanに交換する

def createPresentation(file_name, content):
    print(file_name + 'を作成')
    file = open(f'output/{file_name}', 'w')
    for row in content:
        file.write(str(row) + '<br>\n')
    file.close()