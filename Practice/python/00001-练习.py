"""
# 非布尔值的逻辑运算
result1 = True or True
result2 = 1 or 2
result3 = 1 and 2
# 若第一个是 False 直接返回第二个值
result4 = False or 0
result5 = False and 1
result6 = 1 and False
print(result1,"\n",result2,"\n",result3,"\n",result4,"\n",result5,"\n",result6)
"""


"""
# 通过条件运算符获取三个值中的最大值
a = 9
b = 2
c = 0
max = a if a>b and a>c else b 
max = max if max>c else c
print(max)
"""
a = 9
b = 2
c = 20
max = a if (a>b and a>c) else (b if b>c else c)
print(max)
max1 = a if b<a>c else b if a<b>c else c
print(max1)
test