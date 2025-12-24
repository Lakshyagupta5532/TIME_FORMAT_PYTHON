#String(Collection of characters)
str1 = "This is a string"
str2 = 'This is also a string'
str3 = """Yeh bi \n string hai"""       # \n for next line
print(str1)
print(str2)
print(str3)
print(str1+" "+str2)
print(len(str2))       #Return no. of characters in a given strings
str4 = "a"      #It is not a character it is also a string in PYTHON

#Indexing--   starting from 0 index
#using indexing we can only ascess character not modifying IT
print(str1[3])   #s

#Slicing--  Taken a some part of string
# Syntax --   str[starting_index:ending_index]   (ending_index is excluded)
print(str2[0:4])  #This
print(str1[:4])   #str1[0:4]
print(str1[5:])   #str1[5:len(str)]
#If we read from last(right to left) it start with -1,-2,...so,on

#Conditional Statements
#if-elif-else
#SYNTAX 
    # """
    # if(condition):
    #     statement 1
    # elif(condition2):
    #     statement 2
    # else:
    #     statement 3
    # """

#Nested If ---- if-if-if