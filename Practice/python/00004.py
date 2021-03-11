# 判断能否进入网吧
age = int(input("输入您的年龄: "))
if age > 18:
    print(f"您的年龄是{age},可以上网")
else:
    print("未成年不允许出入网吧")