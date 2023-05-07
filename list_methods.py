list1= ["A","B",1,1,2,"#","*","$"]
print("list:original",list1)
list1.append(12)
print("list:append 12",list1)
list2 =list1.copy()
print("list2:copy",list2)
list1.remove("B")
print("list1:remove B",list1)
print("list2:",list2)

list3 =["hello","hi","*","how are you","get well soon"]
list1.extend(list3)
print("list1:list3 extend",list1)
print("1 s count",list1.count("1"))
list1.insert(7,"be happy")
print("list1:insert happy at 7th index",list1)
print("print index of value 2",list1.index(2,3,7))
list1.pop(3)
print("list1:pop 3rd index",list1)
list1.reverse()
print("list1:reverse",list1)
list1.sort()
print("list1:sort",list1)
list1.clear()
print("list1:clear",list1)
#list1.remove("$")


