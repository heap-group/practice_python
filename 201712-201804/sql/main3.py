import sqlite3

sqlpath = './main.db'

connection = sqlite3.connect(sqlpath)

c = connection.cursor()

try:

    while True:
        id = int(input('番号を入力してください>>>'))
        name = input("名前を入力してください>>>")
        age = int(input("年齢を入力してください>>>"))
        job = input("職業を入力してください>>>")

        register = int(input("データベースに保存する場合は: 1  保存しない場合は: 2>>>"))

        if register == 1:
            sql = 'INSERT INTO login VALUES(?,?,?,?)'
            data = (id, name, age, job)

            c.execute(sql, data)

        else:
            break

        c.commit()

        view = int(input("データを確認しますか？ YES: 1  NO: 2>>>"))

        if view == 1:
                where = f'SELECT * FROM login WHERE name = "{name}";'
                print(c.execute(where))
        else:
            continue

except sqlite3.Error as e:
    print('エラー:', e.args[0])
    c.close()