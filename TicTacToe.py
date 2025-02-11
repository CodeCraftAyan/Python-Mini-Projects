import random

class TicTacToe:
    def __init__(self):
        self.list_of_box = [" "] * 9
        self.player = "X"
        self.computer = "O"

    def display_board(self):
        print(f"     |     |     ")
        print(f"  {self.list_of_box[0]}  |  {self.list_of_box[1]}  |  {self.list_of_box[2]}  ")
        print(f"_____|_____|_____")
        print(f"     |     |     ")
        print(f"  {self.list_of_box[3]}  |  {self.list_of_box[4]}  |  {self.list_of_box[5]}  ")
        print(f"_____|_____|_____")
        print(f"     |     |     ")
        print(f"  {self.list_of_box[6]}  |  {self.list_of_box[7]}  |  {self.list_of_box[8]}  ")
        print(f"     |     |     \n")

    def player_move(self):
        while True:                
            user = int(input("Enter number between (1 - 9) >>>  "))
            if user <= 9 and user >= 1:
                index = user - 1
                if self.list_of_box[index] == ' ': 
                    self.list_of_box[index] = self.player
                    break
                else:
                    print("This position already filled...")
            else:
                print("Inavlid inpot, choose number between 1 - 9")

    def computer_move(self):
        while True:
            randIndex = random.randrange(0, 9)
            if self.list_of_box[randIndex] == ' ':
                self.list_of_box[randIndex] = self.computer
                break

    def cheack_winner(self):
        
        for i in range(0, 9, 3): # for rows
            if self.list_of_box[i] == self.list_of_box[i+1] == self.list_of_box[i+2] != " ":
                return self.list_of_box[i]
            
        for i in range(3): # for columns
            if self.list_of_box[i] == self.list_of_box[i+3] == self.list_of_box[i+6] != " ":
                return self.list_of_box[i]

        # for diagonals
        if self.list_of_box[0] == self.list_of_box[4] == self.list_of_box[8] != " ": 
            return self.list_of_box[0]
        if self.list_of_box[2] == self.list_of_box[4] == self.list_of_box[6] != " ":
            return self.list_of_box[2]
        
        if " " not in self.list_of_box:
            return 'tie'
        
        return None
        

if __name__ == "__main__":

    play = TicTacToe()
    print("\n\nlet's play...\n")
    play.display_board()

    while True:
        # player
        play.player_move()
        print("\n\nuser played...\n")
        play.display_board()

        winner = play.cheack_winner()
        if winner:
            if winner == 'tie':
                print("Game Tied!...")
            else:
                print(f"User Wins!")
            break

        # computer
        play.computer_move()
        print("\n\ncomputer played...\n")
        play.display_board()

        winner = play.cheack_winner()
        if winner:
            if winner == 'tie':
                print("Game Tied!...")
            else:
                print(f"Computer Wins!")
            break
