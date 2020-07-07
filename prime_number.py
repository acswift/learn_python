# 质数大于等于 2 不能被它本身和 1 以外的数整除。
# 在一般领域，对正整数 n，如果用 2 到 sqrt(n) 之间的所有整数去除，均无法整除，则 n 为质数。

import math

def is_prime(n):
    
    if n == 1:
        return False
    
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    
    return True

for num in range(2, 101):
    
    if is_prime(num):
        print('%d is a prime number' % num)
