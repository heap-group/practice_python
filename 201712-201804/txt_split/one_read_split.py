with open('input.csv', encoding='utf-8') as f:
    for row in f:
        columns = row.rstrip().split(',')
        name = columns[0]
        price = columns[1]
        print(name + 'は' + str(price) + '円です。')