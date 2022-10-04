# Deonne Ludwig - IT-140 MODULE SIX MILESTONE

def show_instructions():
    # print game title and how to play
    print("||||||||||||||||||||||||||||||||||||||||||||||||||||")
    print()
    print("                    MOO---VE-IT:                    ")
    print("            ESCAPE THE PROCESSING CENTER            ")
    print()
    print("           ...A Text Adventure Game...")
    print("||||||||||||||||||||||||||||||||||||||||||||||||||||")
    print()
    print("HOW TO PLAY:")
    print("Collect 6 items to complete your disguise, \nfool the Butcher, and escape the processing center!")
    print()
    print("MOVE COMMANDS: N -North, S -South, E -East, W -West")
    print("Type 'QUIT' at any time to end the game")
    print()
    print("====================================================")


# Function to display the current status of the player
#def player_status(current_room):
    #print("You are in", current_room)


# Function to move to new room
def move_to_new_room(current_room, move, rooms):
    current_room = (rooms[current_room][move])
    return current_room


# Main function
def main():
    # The dictionary links a room to other rooms.
    rooms = {
        'Front Office': {'N': 'Packaging Room', 'S': 'Skinning Room', 'E': 'Storage Room', 'W': 'Mounting Room'},
        'Mounting Room': {'E': 'Front Office'},
        'Skinning Room': {'N': 'Front Office', 'E': 'Corral'},
        'Corral': {'W': 'Skinning Room'},
        'Storage Room': {'W': 'Front Office'},
        'Packaging Room': {'S': 'Front Office', 'E': 'Kitchen'},
        'Kitchen': {'S': 'Freezer', 'W': 'Packaging Room'},
        'Freezer': {'N': 'Kitchen'}  # butcher
    }

    # Function call to display instructions
    show_instructions()

    # Starting room
    current_room = 'Front Office'

    move = ""

    # Game loop to simulate the game
    while move != 'QUIT':
        print("You are in the ", current_room)

        # If the player is in 'Freezer' the butcher gets them.
        if current_room == 'Freezer':
            print("WACK! WACK! Oh no! The Butcher got you!")
            break

        move = input("Which way would you like to go?").upper()

        # user move to new room
        if move == 'N' or move == 'S' or move == 'E' or move == 'W':
            next_room = move_to_new_room(current_room, move, rooms)
            print("let's go!...clip .. clop .. clip .. clop ")
            print()
            current_room = next_room
        else:
            print("I don't understand, Please try again!!!")
            print()

    print("Thanks for playing the game. Hope you enjoyed it.")


main()
