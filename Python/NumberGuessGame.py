#Guessing random number game---
import random  
print("Python Number Guessing Game!!")
print("Enter numbers b/w 1 and 100 only!!")
number = random.randint(1,100)               
usernum = int(input("Guess Number:"))
chance = 10                     #not mendetory
while chance!=0:
    if usernum == number:
        print("Right guess , You Win!")
        break
    else:
        if usernum > number:
            print("Hint: Think smaller number!")
        else:
            print("Hint: Think Larger number!")
    chance = chance - 1
    print(f"Chance remaining : {chance}")        
    usernum = int(input("Guess Again:"))

if(chance == 0):
    print("You Lose (chance remaining = 0)")