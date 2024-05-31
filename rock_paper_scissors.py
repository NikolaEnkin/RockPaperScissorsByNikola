import random
from colorama import Fore, Back, Style

rock = "Rock"
paper = "Paper"
scissors = "Scissors"
end = '\033[1mEnd\033[0m'
invalid_input = '\033[1mInvalid Input! Please try again:\033[0m'

winning_counter = 0
losing_counter = 0
draw_counter = 0

player_move = input(Fore.RESET + "Choose " + Fore.LIGHTGREEN_EX + "[r] " + Fore.RESET + "for rock, " +
                    Fore.LIGHTCYAN_EX + "[p] " + Fore.RESET + "for paper, and " +
                    Fore.LIGHTMAGENTA_EX + "[s] " + Fore.RESET + "for scissors: ")
print()

while player_move != "End":

    if player_move == "r":
        player_move = rock
    elif player_move == "p":
        player_move = paper
    elif player_move == "s":
        player_move = scissors

    else:
        raise SystemExit(Fore.RED + f"{invalid_input}")

    computer_random_number = random.randint(1, 3)

    computer_move = ""

    if computer_random_number == 1:
        computer_move = rock
    elif computer_random_number == 2:
        computer_move = paper
    elif computer_random_number == 3:
        computer_move = scissors

    print(f"The computer chose {computer_move}.")

    if player_move == rock and computer_move == scissors or \
            player_move == scissors and computer_move == paper or \
            player_move == paper and computer_move == rock:

        print(Fore.BLUE + "You WIN!")
        winning_counter += 1

    elif player_move == computer_move:
        print(Fore.LIGHTYELLOW_EX + "Draw!")
        draw_counter += 1

    else:
        print(Fore.LIGHTRED_EX + "You were defeated!")
        losing_counter += 1

    print(Fore.RESET + f"If you want to stop playing, type:" + (Fore.CYAN + f" {end}"))
    print()
    question = input("Do you want to continue playing? {Yes or End} ")

    if question == "Yes":
        player_move = input(Fore.RESET + "Choose " + Fore.LIGHTGREEN_EX + "[r] " + Fore.RESET + "for rock, " +
                            Fore.LIGHTCYAN_EX + "[p] " + Fore.RESET + "for paper, and " +
                            Fore.LIGHTMAGENTA_EX + "[s] " + Fore.RESET + "for scissors: ")
        print()
    elif question == "End":
        break


print()
print("'\033[1mThank you for playing! See you next time!\033[0m'")
print(f"You won {winning_counter} time/s, lost {losing_counter} time/s \
and you were tie with the computer {draw_counter} time/s")
