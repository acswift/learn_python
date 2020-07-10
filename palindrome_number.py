# 回文数 “回文”是指正读反读都能读通的句子，它是古今中外都有的一种修辞方式和文字游戏，如“我为人人，人人为我”等。
# 在数学中也有这样一类数字有这样的特征，成为回文数（palindrome number）。
# 设 n 是一任意自然数。若将 n 的各位数字反向排列所得自然数 n1 与 n 相等，则称 n 为一回文数。
# 例如，若 n=1234321，则称 n 为一回文数；但若 n=1234567，则n不是回文数。
# 注意:
# 1.偶数个的数字也有回文数124421
# 2.小数没有回文数

# 判断一个数是否是回文数
def is_palindrome(num):
    
    temp = num
    total = 0

    while temp > 0:
        total = total * 10 + temp % 10
        temp //= 10

    return total == num

print("123321 is a palindrome? %r" % is_palindrome(123321))
print("123322 is a palindrome? %r" % is_palindrome(123322))
