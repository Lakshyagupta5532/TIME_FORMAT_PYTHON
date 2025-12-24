#OOPS IN PYTHON
class student:
    collage_name = "IMSEC"
    def __init__(self,name,age,add):
        self.name = name
        self.age = age
        self.add = add

s1 = student("Lakshya",19,"Mbd")
s2 = student("Aman",19,"bijnor")
s3 = student("Harsh",21,"bihar")
print(s1.name)
print(s2.age)
print(s3.add)
print(s1.collage_name)
print(s2.collage_name)

