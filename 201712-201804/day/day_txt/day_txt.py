from datetime import datetime

#日時を指定する
now = datetime(2018, 11, 14)
#日時を文字列に変換する
print_now = now.strftime('%Y-%m-%d')
#出力
print(print_now)