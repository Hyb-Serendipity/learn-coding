"""
while 三要素：初始化表达式、条件表达式、更新表达式
"""
"""
# 100 以内基数之和
i = 0
result = 0
sum = 0
while i < 100:
    i += 1
    if i % 2 != 0:
        result += i
print(result)
"""
"""
# 求 100 以内所有 7 的倍数之和以及个数
i=7
result = 0
count = 0
while i < 100:
    result += i
    count += 1
    i += 7
print("100 以内所有 7 的倍数之和为",result)
print("100 以内有 ",count," 个 7 的倍数")
"""
"""
# 求 1000 以内所有的水仙花数
# 水仙花数：https://zh.wikipedia.org/zh-cn/%E6%B0%B4%E4%BB%99%E8%8A%B1%E6%95%B0
i = 100
while i < 1000:
    a = i // 100
    b = (i - a * 100) // 10
    c = (i - a * 100 - b * 10)
    if a**3 + b**3 + c**3  == i:
        print(i)
    i += 1
"""
"""
# 判断是否为质数，即一个大于1的自然数，除了1和它自身外，不能被其他自然数整除
num = int(input("Please input an integer greater than 1: "))
i = 2
a1 = " is a prime number."
a2 = " isn't a prime number, it's a composite number is a prime number."
flag = True
while i < num:
    if num % i == 0:
        flag = False
        break
    i += 1
if flag == True:
    print(num, a1)
else:
    print(num, a2)

"""
"""
# 打印 5*5 的 *
# 第一种方法
i = 1
while i <= 5:
    print("*****")
    i += 1


# 第二种方法，嵌套
i1 = 1
while i1 <= 5:
    i2 = 1
    while i2 <=5:
        print("*",end = "")
        i2 += 1
    print()
    i1 += 1
# 打印逐渐增多的 *
i1 = 1
while i1 <= 5:
    i2 = 1
    while i2 <= i1:
        print("*",end = "")
        i2 += 1
    print()
    i1 += 1
"""
"""
# 99乘法表
i1 = 1 
while i1 <= 9:
    i2 = 1 
    while i1 >= i2 <= 9:
        print(i2,"*",i1,"=",i1*i2,"  ",end = "")
        i2 += 1
    print("\n")
    i1 += 1
"""
