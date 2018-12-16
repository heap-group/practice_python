from datetime import datetime
from datetime import timedelta

#日付を設定
str_date = '2018-11-14'

#文字列から日付へ変換
base_date = datetime.strptime(str_date, '%Y-%m-%d')

#30日前の日付を計算
before = base_date - timedelta(days=10)

#日付から文字列に変換
print_date = before.strftime('%Y-%m-%d')

#出力
print(print_date)