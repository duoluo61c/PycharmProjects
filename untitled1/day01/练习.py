# str = input("请输入:")
# print("哈哈哈")
# print(type(str))

# varA = 123;
# if (varA == 123):
#     print("等于")
# elif(varA != 123 ):
#     print("不等于")

# str = "123456"
# for i in str:
#     print(i)
#
# sum = 0
# for i in range(10):
#     sum += i
# print(sum)

#找出100以内所有的偶数
# sumA = 0
# sumB = 0
# for i in range(101):
#     if i % 2 == 0 :
#         print(str(i)+":为偶数")
#         sumA = sumA+1
#     else:
#         print(str(i)+":为奇数")
#         sumB = sumB+1
#
# print("偶数的个数:"+str(sumA))
# print("奇数的个数:"+str(sumB))

#break continue
#
# for i in range(10):
#     if i == 5 :
#         # print("我break了")
#         # break
#         print("我continue了")
#         continue
#     print(i)

# a = 2
# b = 3
# c = 4
#
# if a == b or b != c:
#     print("通过")
# else:
#     print("不通过")

# print(1,2,3,4,sep="!")
# print(1,2,3,4,end="")
# 占位符

# numA =456
# numB = "123"
# print("这是A的值:%d  这是B的值:%s" %(numA,numB))

# str = "123456789"
# print(str[0:])
# print(str[0::2])
# print(str[:0:-1])
# print(len(str))
# print(str.find("2"))
# print(str.index("1"))
# print(str.center(20,"@"))
# print(str.split("3"))
# print(str.replace("1","@"))

#集合set不可重复 自动去重 无序
# set = {1,2,3,"12312"}
# set1 = () #空集合
# print(set)  #打印
# set.add(444)
# print(set)
#
# set2 = {1,2,3,5,6}
# set.update(set2)
# print(set)
#
# set.remove(2)
# print(set)
#
# set.discard(99)
# print(set)
#
# set.clear()
# print(set)

#列表 list 有序可重复可切片
# list = [1,2,3,6,7,"1232"]
# list.remove(1)
# print(list)
# list.append(1)
# print(list)
# list.insert(0,1)
# print(list)
#
# list1 = [2.3,5,8,65,8,9,5]
# print(max(list1))
# print(min(list1))
# list.extend(list1)
# print(list)
#
# list.remove(2)
# print(list)
# numA = list.pop()
# print(list,numA)
# # list.clear()
# # print(list)
#
# list[3] =  "更改的内容"
# print(list)
#
# #升序
# list1.sort()
# print(list1)
# #降序
# list1.reverse()
# print(list1)


#元祖 不可改 增删改都是非法  有序可切片
# tu = (1,2,3,5,6,6)
# # print(tu[1:6])
# # print(tu.count(2))
# for i in range(0,len(tu)):
#     print(tu[i])

#字典 dict
dict1 = {} #空字典
print(dict1)
dict = {"key1":"value1"}
# print(dict["key1"])
# print(dict)
# print(dict.get("key1"))
#
# dict["key2"] = "value2"
# print(dict["key2"])
# dict["key2"] = "key2修改后的值"
# print(dict["key2"])
#遍历
for i in dict:
    print(dict[i])

print(dict.items())

for i,j in dict.items():
    print("key:"+i,"  value:0"+ j)