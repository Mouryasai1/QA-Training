# with open('mess.txt', 'r') as file:
    
#     lines = file.readlines()
# reversed = [line.strip()[::-1] for line in lines]
# with open('mess.txt','w')as writer:
#   for reversed in reversed:
#     print(reversed)
#----------------------------------------------------------
# with open('mess.txt', 'r') as file:
#     a=file.readlines()
#     reversed(a)

# with open('mess.txt','w')as writer:
#     for i in reversed(a):
#         writer.write(i)
#         print(i.strip())
# --------------------------------------------------------
# import csv

# with open('mess.csv', 'r') as file:
#     reader=csv.reader(file)
#     for row in reader:
#         print(row)
#-----------------------------------------------------------
# import csv
# with open('mess.csv', 'r') as file:
#     rea=list(csv.reader(file))
#     reversed(rea)

# with open('mess.csv','w')as writer:
#     for i in reversed(rea):
#         writer.write(i)
#         print(i.strip())
# ---------------------------------------------------
# a = "I am training on python to automate web app"

# words = a.split()
# print(len(a))
# even = [word for word in words if len(word) % 2 == 0]
# print("Words - ", even)

# if len(a) % 2 != 0:
#     a += " "  

# print("String with even length:", a)
# ------------------------------------------------------------------
# def prime(num):
#     if num <= 1:
#         return False
#     for i in range(2, num):
#         if num % i == 0:
#             return False
#     return True

# count = 0
# num = 2
# while count < 20:
#     if prime(num):
#         print(num)
#         count += 1
#     num += 1
# ----------------------------------
# # a = [1,1,2,3,4,5,5,3,7,8,8,9]
# # duplicates = []


# # for i in range(1, len(a)):
# #     if a[i] == a[i-1]:
# #         if a[i] not in duplicates:
# #             duplicates.append(a[i])
# # print("Dupli :", duplicates)
# -----------------------------------

# a = [-4, 3, -2, 7, 1, 0, 8, -3]

# # positive = [num for num in a if num < 0]
# # print(positive)
# # ---------------------------------

# # b=[]
# # for i in (a):
# #     if(i<0):
# #         b.append(i)
# # print(b)

# # a = {'Banglore', 'chennai','hyderabad','coimbatore'}
# # b = {'pune','kerala','up'}

# # a.update(b)
# # print(a)
# # a.union(b)
# # print(a)
# # ==================
# # a = {"Name": "Sunil", "work": "Training"}
# # b = {"Role": "Director", "sal": "350000"}

# # c = a | b

# # print(c)
# # -------------------------

# a = int(input("1"))
# b = int(input("2"))
# c = int(input("3"))

# if a >= b and a >= c:
#     print("greatest: {1}")
# elif b >= a and b >= c:
#     print(" greatest: {2}")
# else:
#     print(f"greatest : {3}")

# def is_palindrome(string):
#     return string == string[::-1]

# ab = input("Enter a string ")

# if is_palindrome(ab):
#     print(f'"{ab}" is a palindrome!')
# else:
#     print(f'"{ab}" is not a palindrome.')
