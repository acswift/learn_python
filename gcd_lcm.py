# (a, b) 表示 a 和 b 的最大公约数
# [a, b] 表示 a 和 b 的最小公倍数
# 有这样的定理: (a, b) * [a, b] == a * b

def gcd(x, y):
    """求最大公约数"""
    (x, y) = (y, x) if x > y else (x, y)
    
    for factor in range(x, 0, -1):
        if x % factor == 0 and y % factor == 0:
            return factor

def lcm(x, y):
    """求最小公倍数"""
    return x * y // gcd(x, y)

result_gcd = gcd(22, 10)
print("22 and 10's gcd is %d" % result_gcd)

result_lcm = lcm(22, 10)
print("22 and 10's lcm is %d" % result_lcm)