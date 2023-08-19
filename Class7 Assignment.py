#################ASSIGNMENT 3

# #Task 9

# l1= [1,6,8,3,5,6,66626,232,63,3]
# print(len(l1))

# #Task 10

# l2=["asfsdf",2,"fasdf",3,"apple",10]
# sum=0
# for i in l2:
#     if type(i) == int:
#         sum+=i

# print("Sum of all Number is",sum)


# #Task 11
# l3 = [35,5,4,66,313,388,33,00,88,9,6]
# largest=0
# for i in l3:
#     if largest<i:
#             largest=i
# print("Largest Number is",largest)

# #Task 12
# a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
# print("Numbers that are less then 5")
# for i in a:
#     if i<5:
#         print(i)

#################ASSIGNMENT 4

#Task 2
# l4=["asfsdf",2,"fasdf",3,"apple",10]
# for i in l4:
#     if type(i) == int:
#         print("Yes, List contains Numeric Value")
#         break

#Task 3

# dic={
#     "name": "Sumaira",
#     "class": "BSIT",
#     "Semester":8
# }

# keyy = input("Enter a key: ")
# value = input("Enter a Value: ")
 
# dic[keyy]=value

# print(dic)

#Task 4
# l5={
#     "a":1,
#     "b":2,
#     "c":3
# }
# sum=0
# for i in l5.values():
#     if type(i) == int:
#         sum+=i
# print("Sum of Numeric item in List is ",sum)

#Task 5

# l6 = [1,4,5,5,5,3]
# dup =0
# for i in l6:
#     sum = 0
#     for j in l6:
#         if j == i:
#             sum += 1
#     if sum>1:
#         dup+=1
# print("There are",dup,"Duplicate Values")


#Task 6

def dup_Key(K):
    dic = {
        "name": "Sumaira",
        "class": "BSIT",
        "Semester":8
    }


    for i in dic.keys():
        if i == K:
            print("Yess! Given key already exists in the Dictionary")

v = input("Enter a Key: ")
dup_Key(v)