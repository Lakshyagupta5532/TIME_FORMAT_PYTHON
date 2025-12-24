#List (mutable) And Tuple(immutable)
print("-----LIST-----")
marks = [94.4 , 23, 43, 54 ,"hello",55]
marks[3] = 12345
print(marks[3])
print(marks)
print(type(marks))
print(len(marks))
print(marks[2:6])       #Slicing
#marks.append(34)  #add one element at the end
#marks.sort() #sorting in acending order
#marks.sort(reverse=True) #decending order
#marks.reverse()   #reverse all elements
# marks.insert(1,233)
# print(marks)
#marks.remove(23)  #remove first occurrence of element
#marks.pop(index)  #removes element at given index

print("----TUPLE----")
tup = (23,4,3,1,54,22,33,"hello","kii haal",3.34)
print(tup[1])
print(type(tup))
tup1 = (1,)
print(type(tup1))
#tup[2] = 222   #not allowed
print(len(tup))


# movies =[]
# movies.append(input("Enter your first fav movie:"))
# movies.append(input("Enter your second fav movie:"))
# movies.append(input("Enter your Third fav movie:"))
# print(movies)

list1 = [12,21,21,12]
list2 = list1.copy()
list2.reverse()
if(list1 == list2 ):
    print("YEs")
else:
    print("no")