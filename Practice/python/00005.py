# 1 到 100 的偶数之和
# 第一种方法

i = 0
result = 0
while i <= 100:
    if i % 2 == 0:
        result += i
    else:
        pass
    i += 1

print(result)

# 第二种方法
"""
i = 0
result = 0
while i <= 100:
    result += i
    i += 2

print(result)
"""


"""
求个 1 ~ 100 的奇数和
i = 0
result = 0
while i <= 100:
    if i % 2 == 1:
        result += i
    i += 1
print(result)
"""