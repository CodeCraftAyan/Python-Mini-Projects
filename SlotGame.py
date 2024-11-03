import random

def spin_slot():
    symbols = ['🍒', '🍋', '🍊', '🍉', '⭐', '💎']
    slot = []
    
    for _ in range(3):
        randomChoice = random.choice(symbols)
        slot.append(randomChoice)
    
    return slot

def win_slot(slot):
    if slot[0] == slot[1] == slot[2]:
        return True
    else:
        return False

def money_handeling(user):
    pass

def play_slot_game():
    input("Press Enter Key for Start :")
    print("-- Welcome To Coders Kasino --\n")    
    
    try:
        money = int(input("Add Balance :  "))
        print(f"Total Amount : ${money}")

        while True:
            if money != 0:
                bet = int(input("Bet Amount :  "))
                
                slot = spin_slot()
                print("Reels : ", " | ".join(slot))
                
                if win_slot(slot):
                    money += (len(slot)*10) + bet
                    print(f"You Win! Congratulation...\nCurrent Balance :  ${money}\n")
                else:
                    money -= bet
                    print(f"You Lose!\nCurrent Balance :  ${money}\n")
                    if money == 0:
                        print("You Lose Your All Money...")
    
    except ZeroDivisionError and ValueError:
        print("At First Add Some Money!!")

play_slot_game()
