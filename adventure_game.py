def start_game():
    """Main function to start the game."""
    print("Welcome to the Adventure Game!")
    print("You wake up in a mysterious forest with two paths ahead.")
    print("1. Take the left path.")
    print("2. Take the right path.")
    
    choice = get_choice(2)
    
    if choice == 1:
        left_path()
    elif choice == 2:
        right_path()

def left_path():
    print("\nYou take the left path and find a river blocking your way.")
    print("1. Try to swim across.")
    print("2. Look for a bridge.")
    
    choice = get_choice(2)
    
    if choice == 1:
        print("\nYou swim across but are attacked by a crocodile. Game over!")
    elif choice == 2:
        print("\nYou find a bridge and safely cross the river. You win!")

def right_path():
    print("\nYou take the right path and encounter a hungry bear.")
    print("1. Fight the bear.")
    print("2. Run away.")
    
    choice = get_choice(2)
    
    if choice == 1:
        print("\nThe bear is too strong. You lose the fight. Game over!")
    elif choice == 2:
        print("\nYou run away and find a safe house. You win!")

def get_choice(options):
    """Validate user input for a choice."""
    while True:
        try:
            choice = int(input("Enter your choice: "))
            if 1 <= choice <= options:
                return choice
            else:
                print(f"Please enter a number between 1 and {options}.")
        except ValueError:
            print("Invalid input. Please enter a number.")

if __name__ == "__main__":
    while True:
        start_game()
        play_again = input("\nDo you want to play again? (yes/no): ").strip().lower()
        if play_again not in ['yes', 'y']:
            print("Thanks for playing! Goodbye.")
            break
