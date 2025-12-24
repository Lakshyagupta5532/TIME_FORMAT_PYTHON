import random

options = ("rock","paper" , "Scissor")
yes = True
print("Welcome to Rock Paper Scissor Game!!")
while(yes):
    computer = random.choice(options)
    player = input("Choose (rock/paper/scissor):")
    if(player == "rock" or player == "paper" or player == "scissor"):
        if(computer == "rock"):
            if(player == "paper"):
                print("You Win!")
            elif(player == "scissor"):
                print("You Loose!")
            else:
                print("Draw!")

        elif(computer == "paper"):
            if(player == "scissor"):
                print("You Win!")
            elif(player == "rock"):
                print("You Loose!")
            else:
                print("Draw!")

        else:
            if(player == "rock"):
                print("You Win!")
            elif(player == "paper"):
                print("You Loose!")
            else:
                print("Draw!")                
    else:
        print("Please enter Valid Choice!!")
    
    temp = input("You wanna play again?(y/n):")
    if(temp == "n" or temp == "N"):
        yes = False