import time
import random


def print_pause(message_to_print):
    print(message_to_print)
    time.sleep(2)


def intro():
    print_pause("You find yourself in a castle ruins. ")
    print_pause("Rumor has it that the malicious lord of the castle has "
                "imprisoned your friend Leo. ")
    print_pause("In your hand you hold a sword from your grandfather. ")
    print_pause("In front of you are two passageways. The first passage leads "
                "to the beautiful chapel, "
                "the second passage takes you up to the tower of the castle.")


def choose_passage(items):
    print_pause("Which passage do you choose?")
    passage = input("Enter 1 to go to the chapel.\n"
                    "Enter 2 to get to the tower of the castle.")
    if passage == "1":
        first_passage(items)
    elif passage == "2":
        second_passage(items)
    else:
        print_pause("Unfortunately this is not a valid response.")
        choose_passage(items)


def reaction(items):
    print_pause("You have two options: 1. escape, 2. fight.")
    option = input("Please enter the number of the option you prefer.")
    if option == "1":
        print_pause("Luckily you are able to escape and head back.")
        print_pause("You're again at the starting point.")
        choose_passage(items)
    elif option == "2":
        print_pause("You have no chance and get imprisoned, too.")
        print_pause("Gameover")
        play_again(items)
    else:
        print_pause("Unfortunately this is not a valid response.")
        reaction(items)


def someone_there(items):
    who = random.choice(["lord", "servant", "mouse"])
    if who == "lord":
        print_pause("Right in front of you is the lord of the castle.")
        print_pause("He holds a sword ten times bigger than yours.")
        reaction(items)
    elif who == "servant":
        print_pause("A woman in serving clothes approaches.")
        print_pause("When she spots you, she whispers 'Don't go in the yard"
                    " where the lord is right now.'")
        print_pause("You're again at the starting point.")
        choose_passage(items)
    elif who == "mouse":
        print_pause("It's only a mouse. Thank God!")
        print_pause("You're again at the starting point.")
        choose_passage(items)


def first_passage(items):
    print_pause("You approach the door of the chapel which is open. "
                "Entering the chapel, you see a wooden box at the end of the "
                "corridor.")
    if "key" in items:
        print_pause("The box is empty because you have already taken all that "
                    "was inside.")
    else:
        print_pause("Inside the box is a key which you will need to free your "
                    "friend Leo.")
        items.append("key")
    print_pause("You take it and head back to the starting point.\n"
                "Suddenly you hear noises and become nervous.")
    someone_there(items)


def second_passage(items):
    print_pause("After 80 steps you reach a door behind which the top floor is"
                " located.\n"
                "Unfortunately the door is locked.")
    if "key" in items:
        print_pause("You put the key in the door and the door creaky opens!")
        print_pause("It's dark, but you can see the shape of a person in the "
                    "corner.")
        print_pause("Unbelievable, it's Leo tied up.")
        print_pause("Fortunately you can free Leo with the sword so that both "
                    "of you can flee. \n"
                    "Congratulations, you won the game!")
        play_again(items)
    else:
        print_pause("It cannot be opened without a key. You need to go back.")
        choose_passage(items)


def play_again(items):
    user_input = input("Would you like to play again? (yes/no)")
    if user_input == "yes":
        play_game(items)
    elif user_input == "no":
        print_pause("Ok, goodbye!")
        exit()
    else:
        print_pause("Unfortunately this is not a valid response.")
        play_again(items)


def play_game(items):
    items = []
    intro()
    choose_passage(items)


if __name__ == "__main__":
    items = []
    play_game(items)
