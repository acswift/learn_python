"""
输入 M 和 N 计算 C(M,N)
"""

def fac(num):
    """求阶乘"""
    result = 1
    for n in range(1, num + 1):
        result *= n
    return result

m = int(input('m = '))
n = int(input('n = '))

print(fac(m) // fac(n) // fac(m - n))

#  Python 的 math 模块中其实已经有一个名为 factorial 函数实现了阶乘运算，事实上求阶乘并不用自己定义函数。
