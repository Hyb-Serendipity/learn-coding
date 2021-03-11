"""
# replace
a = "sdk and ufna and ksdnnsjadnlnfka "
b = a.replace("n","000")
print(b)
c = a.replace("a","11",100)
print(c)
# split
list1 = a.split("and",4)
print(list1)
# join
a = ["aa","54","sa"]
b = " and ".join(a)
print(b)

a = "hello"
print(a.ljust(8,"-"))
print(a.center(10,"-"))
print(a.rjust(10))

a = "hihihi python"
print(a.startswith("h",3,10))
"""
a = " "
print(a.isspace())