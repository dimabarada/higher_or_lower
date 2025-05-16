import random

logo=r"""  ________                               _______               ___.                 
 /  _____/ __ __   ____   ______ ______  \      \  __ __  _____\_ |__   ___________ 
/   \  ___|  |  \_/ __ \ /  ___//  ___/  /   |   \|  |  \/     \| __ \_/ __ \_  __ \
\    \_\  \  |  /\  ___/ \___ \ \___ \  /    |    \  |  /  Y Y  \ \_\ \  ___/|  | \/
 \______  /____/  \___  >____  >____  > \____|__  /____/|__|_|  /___  /\___  >__|   
        \/            \/     \/     \/          \/            \/    \/     \/       
""" 

print(logo)
import random

comp = random.randint(1, 100)
attempts = 0

user_choice = input("Do you want the easy or hard game? Type here: ").lower()

if user_choice == 'easy':
    print("You have 10 attempts!")
    attempts = 10
elif user_choice == 'hard':
    print("You have 5 attempts!")
    attempts = 5
else:
    print("Invalid choice, defaulting to hard mode with 5 attempts.")
    attempts = 5

for i in range(attempts):
    user_input = input(f"\nAttempt {i+1} - Enter your guess (1-100): ")
    
    

    num = int(user_input)

    if num == comp:
        print("🎉 You win!")
        break
    else:
        difference = abs(num - comp)
        if difference <= 10:
            print("🔥 Super close!")
        elif difference <= 20:
            print("😊 Close!")
        elif difference <= 50:
            print("😐 A little far.")
        else:
            print("❄️ Way too far.")
        
        if i == attempts - 1:
            print(f"\n😢 You're out of attempts! The correct number was {comp}.")

