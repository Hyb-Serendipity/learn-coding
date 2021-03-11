age = 18
name = "a"
weight = 75.5
stu_id = 1
# 年龄是 x 岁
print("My age is %d" % age)
# 名字是
print("My name is %s" % name)
# 体重是
print("My weight is %.2f" % weight)
# 学号是
print("My ID is %03u" % stu_id)
# 我的名字是 x, 今年 x 岁
print("My name is %s, I'm %d years old" % (name, age))
# 我的名字是 x, 明年 x 岁
print("My name is %s, I will be %d years old next year" % (name, age + 1))
# 全用字符串
print("My name is %s, I will be %s years old next year" % (name, age + 1))
# f 格式化
print(f"My name is {name}, I will be {age+1} years old next year")
print(f"{name} 的年龄是 {age} 岁")
print("%s 的年龄是 %d 岁" % (name, age))