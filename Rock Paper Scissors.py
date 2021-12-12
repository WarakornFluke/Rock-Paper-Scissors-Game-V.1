import random
choices = ["Rock", 'Paper' ,"Scissors"]
score=0
computer_score=0

while 1:
    computer = random.choices(choices)
    player = input("Rock or Paper or Scissors : ") 
    print(computer)
    #print(player)
    if player == "Rock":
        if computer == ["Paper"]:
            print("You lose! ")
            computer_score+=1
        elif computer ==["Rock"]:
            print("Draw!! ")
        elif computer ==["Scissors"]:
            print("You Win!! ")
            score+=1
    elif player == "Paper":
        if computer == ["Paper"]:
            print("Draw!! ")
        elif computer ==["Rock"]:
            print("You Win!! ")
            score+=1
        elif computer ==["Scissors"]:
            print("ํYou lose!! ")
            computer_score+=1
    elif player == "Scissors":
        if computer == ["Scissors"]:
            print("Draw!! ")
        elif computer ==["Paper"]:
            print("You Win!! ")
            score+=1
        elif computer ==["Rock"]:
            print("ํYou lose!! ")
            computer_score+=1
    print("player score: ",score)
    print("computer score: ",computer_score)