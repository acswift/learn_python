# 序列表示有序排列
# 通过下标的偏移量访问到它的一个或几个成员
# 字符串 "abcd"
# 列表 [0, 'abcd']
# 元组 ("abc", "def")
# 字符串、列表、元组三种类型都属于序列

# 记录生肖，根据年份判断生肖
chinese_zodiac = "猴鸡狗猪鼠牛虎兔龙蛇马羊"
# print(chinese_zodiac[0:4])
# print(chinese_zodiac[-1])
year = 2018
print(year % 12)
print(chinese_zodiac[year % 12])

# 成员关系操作符 in, not in
print('狗' not in chinese_zodiac)

# 连接操作
print(chinese_zodiac + 'abcd')
print(chinese_zodiac * 3)