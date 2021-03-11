""" 
# 单个数据的元祖,必须加一个逗号
t1=(1,)
# 多个数据的元祖
t2=(10,20,30)

t3=("a")
print(type(t1))
print(type(t2))
print(type(t3))
"""
t1 = ("aa","bb","cc","dd")

print(t1[2])
print(t1.index("aa"))
print(t1.count("a"))
print(len(t1))