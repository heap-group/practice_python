from datetime import datetime
#日時を指定する
now = '2018/11/14'
#文字列を日時に変換する
print_now = datetime.strptime(now, '%Y/%m/%d')
#出力
print(print_now)