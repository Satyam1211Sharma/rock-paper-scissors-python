import random

# Instructions
print('Winning rules of the game ROCK PAPER SCISSORS are:\n'
      + "Rock vs Paper -> Paper wins\n"
      + "Rock vs Scissors -> Rock wins\n"
      + "Paper vs Scissors -> Scissors wins\n")

# Mapping numbers to choices
choices = {1: "Rock", 2: "Paper", 3: "Scissors"}

while True:
    print("\nEnter your choice:")
    print("1 - Rock")
    print("2 - Paper")
    print("3 - Scissors")

    # Take user input
    try:
        user_choice = int(input("Enter your choice: "))
        if user_choice not in choices:
            print("Invalid choice. Please choose between 1-3.")
            continue
    except ValueError:
        print("Please enter a number (1, 2 or 3).")
        continue

    user_choice_name = choices[user_choice]
    print("User choice is:", user_choice_name)

    print("Now it's Computer's Turn...")

    # Computer choice
    comp_choice = random.randint(1, 3)
    comp_choice_name = choices[comp_choice]
    print("Computer choice is:", comp_choice_name)

    print(user_choice_name, "vs", comp_choice_name)

    # Decision logic
    if user_choice == comp_choice:
        print("<== It's a tie! ==>")
    elif (user_choice == 1 and comp_choice == 3) or \
         (user_choice == 2 and comp_choice == 1) or \
         (user_choice == 3 and comp_choice == 2):
        print("<== You win! 🎉 ==>")
    else:
        print("<== Computer wins! 😈 ==>")

    # Play again?
    again = input("Do you want to play again? (Y/N): ").lower()
    if again != 'y':
        print("Thanks for playing! 👋")
        break
2
