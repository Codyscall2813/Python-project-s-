def intro():
    print("Welcome to the Adventure Game!")
    print("You find yourself at the entrance of a dark forest.")
    print("You can either enter the forest or walk away.")

def forest():
    print("\nYou have entered the forest.")
    print("The forest is dark and you hear strange noises.")
    print("You can either follow the path or turn back.")

def path():
    print("\nYou follow the path and come across a mysterious cabin.")
    print("You can either enter the cabin or continue walking.")

def cabin():
    print("\nYou enter the cabin and find a treasure chest.")
    print("You can either open the chest or leave it alone.")

def treasure_chest():
    print("\nYou open the chest and find a pile of gold coins!")
    print("Congratulations, you have found the treasure and won the game!")
    print("Thank you for playing!")

def game_over():
    print("\nYou have chosen to leave or turned back.")
    print("Game Over. Thank you for playing!")

def main():
    intro()
    choice = input("What do you want to do? (enter/leave): ").strip().lower()
    
    if choice == 'enter':
        forest()
        choice = input("What do you want to do? (follow/turn back): ").strip().lower()
        
        if choice == 'follow':
            path()
            choice = input("What do you want to do? (enter/continue): ").strip().lower()
            
            if choice == 'enter':
                cabin()
                choice = input("What do you want to do? (open/leave): ").strip().lower()
                
                if choice == 'open':
                    treasure_chest()
                else:
                    game_over()
            else:
                game_over()
        else:
            game_over()
    else:
        game_over()

if __name__ == "__main__":
    main()
