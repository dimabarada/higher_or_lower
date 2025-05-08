logo = r"""
.------.            _     _            _    _            _    
|A_  _ |.          | |   | |          | |  (_)          | |   
|( \/ ).-----.     | |__ | | __ _  ___| | ___  __ _  ___| | __
| \  /|K /\  |     | '_ \| |/ _` |/ __| |/ / |/ _` |/ __| |/ /
|  \/ | /  \ |     | |_) | | (_| | (__|   <| | (_| | (__|   < 
`-----| \  / |     |_.__/|_|\__,_|\___|_|\_\ |\__,_|\___|_|\_\\
      |  \/ K|                            _/ |                
      `------'                           |__/           
"""

print(logo)
import random

cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

user_input = input("Do you want to play Blackjack? (simple edition) Type 'yes' or 'no': ")

if user_input.lower() == 'yes':
    u_card_1, u_card_2 = random.sample(cards, 2)
    comp_1, comp_2 = random.sample(cards, 2)

    user_cards = [u_card_1, u_card_2]
    comp_cards = [comp_1, comp_2]

    user_result = sum(user_cards)
    comp_result = sum(comp_cards)

    print("Your cards are:", u_card_1, u_card_2)
    print("Computer's cards are: hidden")

    while user_result < 21:
        user_input = input("Do you want to draw another card? Type 'yes' or 'no': ")
        if user_input.lower() == 'yes':
            new_card = random.choice(cards)
            user_cards.append(new_card)
            user_result = sum(user_cards)
            print("Your cards are:", *user_cards)
            if user_result > 21:
                print(f"You busted with {user_result}. You lose.")
                break
        elif user_input.lower() == 'no':

            comp_3 = random.choice(cards)
            comp_cards.append(comp_3)
            comp_result = sum(comp_cards)

            print("Your final cards are:", *user_cards)
            print("Computer's cards were:", *comp_cards)
            print(f"Your total: {user_result}")
            print(f"Computer's total: {comp_result}")

            if comp_result > 21 and user_result <= 21:
                print(f"You win! Computer busted with {comp_result}")
            elif user_result > comp_result and user_result <= 21:
                print(f"You win with {user_result} against {comp_result}")
            elif user_result < comp_result and comp_result <= 21:
                print(f"You lose with {user_result} against {comp_result}")
            elif user_result == comp_result:
                print("It's a draw!")
            break
