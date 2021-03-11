"""
简化
i = 1
while i <= 5:
    if i == 3:
        print("有虫子,不吃了")
        i += 1
        continue
    print(f"吃了第{i}个")
    i += 1
"""

"""
复杂
i = 1
while i <= 5:
    if i == 3:
        print("有虫子,不吃了")
        i += 1
        continue
    else:
        print(f"吃了第{i}个")
        i += 1
"""

j = 0
i = 0
while j < 3:
    while i < 3:
        print("haha",i)
        i += 1
    j += 1
print("结束",i)