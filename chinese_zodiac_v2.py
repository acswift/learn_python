# 序列表示有序排列
# 通过下标的偏移量访问到它的一个或几个成员
# 字符串 "abcd"
# 列表 [0, 'abcd']
# 元组 ("abc", "def")
# 字符串、列表、元组三种类型都属于序列

# 记录生肖，根据年份判断生肖
chinese_zodiac = "猴鸡狗猪鼠牛虎兔龙蛇马羊"

year = int(input('请用户输入出生年份: '))

print(chinese_zodiac[year % 12])

if chinese_zodiac[year % 12] == '狗':
    print('狗年运势大吉大利')

# for 循环
for cz in chinese_zodiac:
    print(cz)

for i in range(1, 13):
    print(i)

for year in range(2000, 2019):
    print('%s 年的生肖是 %s' % (year, chinese_zodiac[year % 12]))


# while 循环
import time
num = 5
while True:
    num = num + 1

    if num > 10:
        break

    print(num)
    time.sleep(1)