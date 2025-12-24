# yes = True
# while(yes):
#     email = input("Enter your email:")
#     if "@gmail.com" in email:
#         print("Valid email")
#     else:
#         print("Invalid email (keep syntax as xxxx@gmail.com)")
#     opt = input(("You Wanna enter again?(y/n):"))
#     if opt == "n":
#         yes = False
#         print("exit")
        
# from copy import copy
# list = [1,2,3,4,5]
# copy_list = copy(list)
# print(copy_list)

# def sentence(s):
#     d = {"Upper_case":0, "Lower_case":0 , "Digits":0}
#     for i in s:
#         if i.isupper():
#             d["Upper_case"] +=1
#         elif i.islower():
#             d["Lower_case"] +=1
#         elif i.isdigit():
#             d["Digits"] +=1
#         else:
#             pass
#     print("Original string:",s)
#     print(f"No. of Upper case characters: {d['Upper_case']}")
#     print(f"No. of Lower case characters: {d['Lower_case']}")
#     print(f"No. of Digits :{d['Digits']}")

# s = input("Enter sentence:")
# sentence(s)
