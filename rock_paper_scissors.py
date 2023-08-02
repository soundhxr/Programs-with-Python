import random, time
user_score = 0
computer_score = 0
outcomes = {"stone":"paper", "paper":"scissors", "scissors":"stone"}
choices = ["stone", "paper", "scissors"]
while True:
    user_choice = input("\nWhat do you choose? stone, paper or scissors: ").lower()
    while user_choice not in choices:
        user_choice = input("invalid input\nWhat do you choose? stone, paper or scissors: ").lower()
    computer_choice = str(random.choice(choices)).lower()
    print("computer chose", computer_choice)
    if user_choice == computer_choice:
        time.sleep(1)
        print("it's a tie")
    else:
        for i in outcomes:
            if i == user_choice and outcomes[i] == computer_choice:
                time.sleep(1)
                print("computer wins!")
                computer_score += 1
                break
        else:
            time.sleep(1)
            print("you win!")
            user_score += 1
    time.sleep(2)
    if input("\nwanna play again? (y/n): ").capitalize() != "Y":
        break
print("\nyour score:", user_score)
print("computer's score:", computer_score)
