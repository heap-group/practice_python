sample = 'a,b,c,d,e'
#splitを使うと分割されて配列扱いになる
sample_array = sample.split(',')

print(sample_array)

#####半角スペースで分割して一括表示
num_string = '100 200 300 400 500'

nums = num_string.split(' ')

for x in nums:
    print(x)