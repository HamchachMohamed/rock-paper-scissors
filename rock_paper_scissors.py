import random 

user_wins = 0
computer_wins = 0

options = ["r", "p", "s"]
you = input("Enter your name: ")
while True :
    user_input = input("Type Rock (R)/ Paper (P)/ Scissors (S) or Q to quit: ").lower()
    if user_input == "q":
        break
    
    if user_input not in options:
        continue

    random_number = random.randint(0, 2)
    # rock = 0, paper = 1, scissors = 2
    computer_pick = options[random_number]
    if computer_pick == "r":
        trc = "Rock"
    elif computer_pick == "p":
        trc = "Paper"
    else :
        trc = "Scissors"
    if user_input == "r":
        tru = "Rock"
    elif user_input == "s":
        tru = "Scissors"
    else :
        tru = "Paper"

    print(f"{you} : {tru} - {trc} : COMPUTER")
    
    if user_input == "r" and computer_pick == "s":
        print("You won!")
        user_wins += 1
    elif user_input == "p" and computer_pick == "r":
        print("You won!")
        user_wins += 1
    elif user_input == "s" and computer_pick == "p":
        print("You won!")
        user_wins += 1
    elif user_input == "s" and computer_pick == "r":
        print("You lost!")
        computer_wins += 1
    elif user_input == "p" and computer_pick == "s":
        print("You lost!")
        computer_wins += 1
    elif user_input == "r" and computer_pick == "p":
        print("You lost!")
        computer_wins += 1
    elif user_input == "s" and computer_pick == "s":
        print("The score is tied!")
    elif user_input == "r" and computer_pick == "r":
        print("The score is tied!")
    elif user_input == "p" and computer_pick == "p":
        print("The score is tied!")

    #print("You won ",user_wins, "times.")
    #print("The computer won ",computer_wins, "times.")
    print(f" {you} {user_wins} - {computer_wins} computer") 

print("Goodbye!")