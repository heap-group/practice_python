import sqlite3
cnct = sqlite3.connect('./main.db')

c = cnct.cursor()

sql = "select * from sample;"

c.execute(sql)

for row in c:
    print(str(row[0]) + "|" + row[1])

c.close()