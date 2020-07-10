# 判断一个数是否是素数

def is_prime(num):

    for factor in range(2, int(num ** 0.5) + 1):
        if num % factor == 0:
            return False
    
    return True if num != 1 else False

print("91 is a prime? %r" % is_prime(91))
print("17 is a prime? %r" % is_prime(17))
