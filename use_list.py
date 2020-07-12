list1 = [1, 3, 5, 7, 100]
print(list1)

for index in range(len(list1)):
    print(list1[index])

for elem in list1:
    print(elem)

# 通过 enumerate 函数处理列表之后再遍历可以同时获得元素索引和值
for index, elem in enumerate(list1):
    print(index, elem)

# 添加元素
list1.append(200)
list1.insert(1, 400)

# 合并两个列表
# list1.extend([1000, 2000])
list1 += [1000, 2000]
print(list1)
print(len(list1))

# 先通过成员运算判断元素是否在列表中，如果存在就删除该元素
if 3 in list1:
    list1.remove(3)
if 1234 in list1:
    list1.remove(1234)
print(list1)

# 从指定位置删除元素
list1.pop(0)
list1.pop(len(list1) - 1)
print(list1)

# 清空列表元素
list1.clear()
print(list1)

# 对列表排序
list1 = ['orange', 'apple', 'zoo', 'internationalization', 'blueberry']
# sorted 函数返回列表排序后的 copy 不会修改传入的列表
# 函数的设计就应该像 sorted 函数一样尽量可能不产生副作用
list2 = sorted(list1)
list3 = sorted(list1, reverse=True)
# 通过 key 关键字参数指定根据字符串长度进行排序而不是默认的字母表顺序
list4 = sorted(list1, key=len)
print(list1)
print(list2)
print(list3)
print(list4)
# 给列表对象发出排序消息直接在列表对象上进行排序
list1.sort(reverse=True)
print(list1)