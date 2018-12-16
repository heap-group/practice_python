from datetime import datetime

#今の日付と時間と秒数を変数に代入する
ima = datetime.now()

#年月日時間を全て表示する
print(ima)
print('\n')

#年月日を分けて表示させる
print(str(ima.year) + '年')
print(str(ima.month) + '月')
print(str(ima.day) + '日')
print('\n')

#時分秒を分けて表示させる
print(str(ima.hour) + '時')
print(str(ima.minute) + '分')
print(str(ima.second) + '秒')
print('\n')

#分割して出力
print(f'{str(ima.year)}年{str(ima.month)}月{str(ima.day)}日{str(ima.hour)}時{str(ima.minute)}分{str(ima.second)}秒')
print('\n')