#First program
print("Hello World","Kese ho")
print(3,5,5+9)

#Variables
name = "Lakshya gupta"  #string
age = 19                #integer or 19.22 = floating
print("My name is",name,"and age is",age)
print(f"My name is {name} and age is {age}")

#Data Types
Integers = 34    #int - numbers
String = "name"  #str - collection of characters
Float = 45.34    #float - decimal
Boolean = True   #bool - True/False
name = None      #none - nothing
print(type(Integers) , type(String) , type(Float) , type(Boolean) , type(name))

#Types of Operators

#1.)Arithmetic Operators +,-,/,*,%,power(a to the power b)=**
# a,b=4,2
# print(a+b,"\t",a-b,"\t",a*b,"\t",a/b,"\t",a%b,"\t",a**b) 
#Division Operator Always gave floating output in python
#To get int value use Floor division or Ceiling division

#2.)Relational/Comparision Operators ==,!=,<,>,<=,>=
# Return - True/False  

#3.)Assignment Operators =,+=,-=,*=,/=
#assign the value of right operand to left operand

#4.)Logical Operators not,and,or
#and - false(dominent)
#or - true(dominent)
#not - work on single operator  T->F and F->T

# #INPUT in Python
# a = int(input("Enter number:"))
# b = input("Enter your name:")     #By default = string
# print(type(a))
# print(type(b))

########################## E N D ######################### 


# Initializing list 
list1 = [ 1, [2, 3] , 4 ] 
print("list 1 before modification:\n", list1) 
# all changes are reflected 
list2 = list1 
# shallow copy - changes to 
# nested list is reflected, 
# same as copy.copy(), slicing 
list3 = list1.copy() 
# deep copy - no change is reflected 
 
list1.append(5) 
list1[1][1] = 999 
print("list 1 after modification:\n", list1) 
print("list 2 after modification:\n", list2) 
print("list 3 after modification:\n", list3) 
 