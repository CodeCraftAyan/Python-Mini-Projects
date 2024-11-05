# terminal based pssword generetor

import random
import string

try :
    print("--- Create Your Own Password in Just One Clicks ---")
    user_PasswordSize = int(input("\nPassword Length :  "))

    if user_PasswordSize <= 0: print("Warning : Password size can't be 0 or less then 0")
    else:
        all_Charecters_List = list(string.ascii_letters + string.digits + string.punctuation)
        print(f"Genarated Password :  {''.join(random.sample(all_Charecters_List, user_PasswordSize))}")
        print("\nPassword Generated Successfully!")

except ValueError: print("Invalid User Input, Try Again...")
