"""
Pattern-01
* * * * *
* * * * *
* * * * *
* * * * *
* * * * *
"""
# for i in range(1,6):
#     for j in range(1,6):
#         print("*" , end = " ")
#     print()
# print("DONE 01")


"""
Pattern-02
* 
* * 
* * * 
* * * * 
* * * * *
"""
# for i in range(1,6):
#     for j in range(1,i+1):
#         print("*" , end=" ")
#     print()
# print("DONE 02")


"""
Pattern-03
* * * * *
* * * *
* * *
* *
*
"""
# n = 5
# for i in range(1,n+1):
#     for j in range(1,n-i+2):
#         print("*",end=" ")
#     print()
# print("DONE 03")
"""OR"""
# n = 5
# for i in range(n,0,-1):
#     for j in range(1,i+1):
#         print("*",end=" ")
#     print()
# print("DONE 03 Alternative code")


"""
Pattern-04
1
1 2
1 2 3
1 2 3 4
1 2 3 4 5
"""
# n = 5
# for i in range(1,n+1):
#     for j in range(1,i+1):
#         print(j,end=" ")
#     print()
# print("DONE 04")


"""
Pattern-05
5 4 3 2 1
5 4 3 2
5 4 3
5 4
5
"""
# n = 5
# for i in range(n,0,-1):
#     for j in range(1,i+1):
#         print(n+1-j,end=" ")
#     print()
# print("DONE 05")


"""
Pattern-06
5 4 3 2 1
4 3 2 1
3 2 1
2 1
1
"""
# n = 5
# for i in range(n,0,-1):
#     a = i
#     for j in range(1,i+1):
#         print(a,end=" ")
#         a -=1
#     print()
# print("DONE 06")


"""
Pattern-07
* 
* * * 
* * * * *
* * * * * * *
* * * * * * * * *
"""
# n =5
# for i in range(1,n+1):
#     for j in range(1,2*i):
#         print("*",end=" ")
#     print()
# print("DONE 07")


"""
Pattern-08
        * 
      * * * 
    * * * * *
  * * * * * * *
* * * * * * * * *
"""
# n = 5
# for i in range(1,n+1):
#     print(" "*(n-i) , end = " ")
#     for j in range(1,2*i):
#         print("*", end=" ")
#     print()
# print("DONE 08")


"""
Pattern-09
    *
   ***
  *****
 *******
*********
"""
# n = 5
# for i in range(1,n+1):
#     print(" "*(n-i) , end = "")
#     for j in range(1,2*i):
#         print("*", end="")
#     print()
# print("DONE 09 (Same pyramid pattern without spacing)")


"""
Pattern-10
* * * * * * * * *
  * * * * * * *
    * * * * *
      * * *
        * 
"""
# n = 5
# for i in range(5,0,-1):
#     print(" "*(n-i) , end="")
#     for j in range(1,2*i):
#         print("*",end="")
#     print()
# print("DONE 10")


"""
Pattern-11
*********
 *******
  *****
   ***
    *
"""
# n = 5
# for i in range(5,0,-1):
#     print(" "*(n-i) , end="")
#     for j in range(1,2*i):
#         print("*",end="")
#     print()
# print("DONE 11 (Inverse pyramid without spacing)")


"""
Pattern-12
        * 
      * * * 
    * * * * *
  * * * * * * *
* * * * * * * * *
  * * * * * * *
    * * * * *
      * * *
        * 
"""
# n = 5
# for i in range(1,n+1):
#     print(" "*(n-i) , end="")
#     for j in range(1,2*i):
#         print("*" , end="")
#     print()
# for i in range(n-1,0,-1):
#     print(" "*(n-i),end="")
#     for j in range(1,2*i):
#         print("*",end="")
#     print()
# print("DONE 12")


"""
Pattern-13
*
***
*****
*******
*********
*******
*****
***
*
"""
# n = 5
# for i in range(1,n+1):
#     # print(" "*(n-i) , end="")
#     for j in range(1,2*i):
#         print("*" , end="")
#     print()
# for i in range(n-1,0,-1):
#     # print(" "*(n-i),end="")
#     for j in range(1,2*i):
#         print("*",end="")
#     print()
# print("DONE 13")


"""
Pattern-14
*
**
***
****
*****
****
***
**
*
"""
# n = 5
# for i in range(1,n+1):
#     for j in range(1,i+1):
#         print("*",end="")
#     print()
# for i in range(n-1,0,-1):
#     for j in range(1,i+1):
#         print("*",end="")
#     print()
# print("DONE 14")

