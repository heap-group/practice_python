# INSERT文を実行
import sqlite3
sqlite_path = './main.db'
connection = sqlite3.connect(sqlite_path)
cursor = connection.cursor()

try:
    # セットアップ
    #テーブル削除
    #cursor.execute("DROP TABLE IF EXISTS sampledb")
    #テーブル作成
    #cursor.execute("CREATE TABLE IF NOT EXISTS sample (id INTEGER PRIMARY KEY, name TEXT)")
    
    cursor.execute("INSERT INTO sample VALUES (1, '佐藤')")
    cursor.execute("INSERT INTO sample VALUES (?, ?)", (2, '田中'))
    
    datas = [
        (3, '伊藤'),
        (4, '渡辺'),
        (5, '湯本')
    ]
    
    cursor.executemany("INSERT INTO sample VALUES (?, ?)", datas)
    
    connection.commit()
    
except sqlite3.Error as e:
    print('sqlite3.Error occurred:', e.args[0])

# 動作確認
cursor.execute('SELECT * FROM sample')
print(cursor.fetchall())

connection.close()
