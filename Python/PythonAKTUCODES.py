"""UNIT 02"""

"""WAP to check the largest among three numbers?"""
# a = int(input("Enter the first number:"))
# b = int(input("Enter the second number:"))
# c = int(input("Enter the third number:"))
# if a>b and a>c:
#     print(f"{a} is greatest")
# elif b>a and b>c:
#     print(f"{b} is greatest")
# else:
#     print(f"{c} is greatest")

"""WAP to check given year is leap year or not"""
# year = int(input("Enter the year:"))
# if ((year%4==0 and year%100!=0) or (year%400==0)):
#     print(f"{year} is a leap year")
# else:
#     print(f"{year} is not a leap year")
        
"""WAP to display fiboacci sequance for n terms"""
# n = int(input("Enter the number of terms:"))
# a = 0
# b = 1
# for i in range(1,n+1):
#     print(a , end="\t")
#     sum = a+b
#     a = b
#     b = sum

"""WAP to print
* 
* * 
* * * 
* * * * 
* * * * * 
* * * * 
* * * 
* * 
* 
"""
# n =5
# for i in range(1,n+1):
#     for j in range(1,i+1):
#         print("*",end=" ")
#     print()
# for i in range(n-1,0,-1):
#     for j in range(1,i+1):
#         print("*",end=" ")
#     print()

"""WAP to print all prime numbers in given range"""
# lower_value = int(input("Enter the lower range value:"))
# upper_value = int(input("Enter the upper range value:"))
# for num in range(lower_value,upper_value+1):
#     if num>1:
#         for i in range(2,num):
#             if(num%i==0):
#                 break
#             else:
#                 print(f"{num}\t")
#                 break

"""WAP to convert time for 12-hour to 24-hour format!!"""
def convert_time(str1):
    if str1[-2:] == "AM" and str1[:2]=="12":
        return "00" + str1[2:-2]
    elif str1[-2:] =="AM":
        return str1[:-2]
    elif str1[-2:] == "PM" and str1[:2]=="12":
        return str1[:-2]
    else:
        return (str((int(str1[:2])+12))+str1[2:8])
    
print(convert_time("01:05:45AM"))