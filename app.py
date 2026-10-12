# QUESTION NO 02
# with open("text.txt") as f:
#     read = f.read()
#     print(read)


# QUESTION NO 03
# line_add = "learning file handling in python \n"
# with open("text.txt","a") as f:
#     write = f.write(line_add)


# QUESTION NO 04
# with open ("numbers.txt","a") as f:
#     num = 0
#     for i in range(1,6):
#         num = f"{i}\n" 
#         data = f.write(num)   


# QUESTION NO 05
# cal = 0
# with open("numbers.txt") as f :
#     for line in f:
#         line = line.strip()
#         if line:
#             numbers = int(line)
#             cal += numbers
# print(f"cal sum :{cal}")     


# QUESTION NO 06
# with open("numbers.txt") as f:
#     lines = f.readlines()
#     print(f"total lines :{len(lines)}")


# QUESTION NO 07
# with open("text.txt") as f:
#     data = f.read()
#     print(data)

# sir with open ka use ham is leye karti hai ki file ko closed karna nahi parta    


# QUESTION NO 08
# with open("text.txt") as f:
#     data = f.readlines()
#     print(data)


# QUESTION NO 09
# with open("text.txt") as f:
#     data = f.read()
# with open("copy.txt", "w") as f:
#     f.write(data)    


# QUESTION NO 10
# import os
# if os.path.exists("text2.txt"):
#     os.remove("text2.txt")
#     print("file deleted")
# else:
#     print("file not found")


# QUESTION NO 11
# try:
#     result = 10/0
#     print(result)
# except ZeroDivisionError:
#     print("Error 0 se divide nahi o sakta.")    


# QUESTION NO 12
# try:
#     user = int(input("Enter number only :"))
#     print(f"your number {user}")
# except ValueError:    
#    print("Value error!")


# QUESTION NO 13
# try:
#     with open("name.txt") as f:
#         f.read()
# except FileNotFoundError:
#     print("Error :file not exist")    


# QUESTION NO 14
# try:
#     result = 10/0
#     print(result)
# except ZeroDivisionError:
#     print("Error 0 se divide nahi o sakta.")
# finally:
#     print("task completed.")   # hamesha chaliga chai error ho ya na ho.     


# QUESTION NO 15
# nums = [29,12,41,23]
# try:
#     print(nums[5])
# except IndexError:
#     print("index not found.")   


# QUESTION NO 16
# student = {
#     "name" :"Hammad ashraf",
#     "age" : 20
# }

# try:
#     print(student["fname"])
# except KeyError:
#     print("Error : Key not found.")    


# QUESTION NO 17
# try:
#     num = int(input("Enter number :"))
#     div = 10 / num
#     print(div)
# except ZeroDivisionError:
#     print("Error : 0 se divide nahi kar sakti.")
# except ValueError:
#     print("Error : only number can allow.")    


# QUESTION NO 18
# try:
#     num = int(input("enter number :"))
# except ValueError:
#     print("Error : number only.")
# else:
#     print(f"ap ne \"{num}\" enter kiya hai.")   


# QUESTION NO 19
# def check_age(age):
#     if age < 18:
#         raise ValueError("Age must be 18 or greater.")
#     else:
#         print("Age is valid")
# try:
#     check_age("add")
# except ValueError as e:
#     print(f"Error : {e}")     


# QUESTION NO 20
# try:
#     with open("text2.txt") as f:
#         data = f.read()
#         print(data)
# except FileNotFoundError:
#     print("Error : file nahi mille!")
# finally:
#     print("file handling completed.")            
    





    

