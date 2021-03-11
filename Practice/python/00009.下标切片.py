# 单、双引号时换行不生效
a = "a"\
    "b"
print(a)
# 三引号内支持换行输入&输出
b = """aaa
bbb
ccc"""
print(b)
str1 = "abcdefg"
print(str1[0:2:1])
str2 = "012345678"
print(str2[0:5:2]) #024
print(str2[:]) #012345678
print(str2[:5]) # 01234
print(str2[-4:-1]) # 567
print(str2[-4:-1:-1]) # 無結果
print(str2[-1:-4:-1]) # 876
print(str2[::-1]) # 876543210
print(str2[8:5:-1]) # 876

# [下标:下标:步长]