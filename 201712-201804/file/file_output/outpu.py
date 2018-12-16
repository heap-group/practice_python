with open('input.csv', encoding='utf-8') as f:
    with open('output.csv', 'w', encoding='utf-8') as wf:
        for row in f:
            columns = row.rstrip().split(',')
            item = columns[0]
            price = columns[1]
            wf.write(item + 'は' + str(price) + '円です\n')