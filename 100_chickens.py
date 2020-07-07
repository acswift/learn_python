"""
《百钱白鸡》问题
"""

for x in range(0, 20):
    for y in range(0, 33):
        z = 100 - x - y
        
        if 5 * x + 3 * y + z / 3 == 100:
            print("公鸡 %d 只, 母鸡 %d 只, 小鸡 %d 只" % (x, y , z))
