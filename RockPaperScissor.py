import random

choiceDict = {'r' : 1, 'p' : 2, 's' : 3}
outputDict = {1 : 'Rock', 2 : 'Paper', 3 : 'Scissor'}

computer = random.randint(1, 3);
print("-- Let's Play Rock Paper Scissor --\nRules : r for Rock, p for paper, s for Scissor...")

while True :
    user = input("\nYou : ").lower()

    userChoice = choiceDict[user]

    if user == 'r' or user == 'p' or user == 's' : print(f"Computer Choice : {outputDict[computer]}\nUser Choice : {outputDict[userChoice]}")
    else : print("Invalid Input!")
        

    if computer == userChoice : print("Tie!")
    elif computer == 1 and userChoice == 2 or computer == 2 and userChoice == 3 or computer == 3     and userChoice == 1 : print("You Win!")
    else : print("You Lose!")