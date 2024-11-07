import random

print("-- Let's Play Guess the Number (1 ~ 100) --")
random = random.randint(1, 100)
count = 0
 
while True :
    user = int(input("\nGuess : "))
    if user > 100 : print("Sorry try Again, you enter greater then 100 !!!")
    else :
        count += 1
        if user > random : print(f"Try Again... \nHint : Guess Smaller then {user}")
        elif user < random : print(f"Try Again... \nHint : Guess Greater then {user}")
        else : 
            print(f"Congrates, You Win!\nYou find {random} in {count} attempts.")
            break