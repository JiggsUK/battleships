"""A program to run a game of battleships that should be a one player version with a single ship hidden in a 5x5
grid. The player will have 10 guesses to try to sink the ship """

# import the random integer function to place the battleship
from random import randint
from time import *
import math


# TODO statistics for each game - wins/losses
# TODO closeness clues
# TODO computer battleship row needs converting to display at the end


class GameSetup:
    def __init__(self):
        self.user_gameboard_size_choice = int()
        self.gameboard = []
        self.difficulty_options = ['1 for Easy', '2 for Normal', '3 for Hard']
        self.options = [1, 2, 3]
        self.user_selected_difficulty = 0
        self.calculated_number_of_turns = 0
        self.flattened_gameboard_build = []
        self.build_gameboard = []
        self.numbers_to_letters_dictionary = {'1':'A', '2':'B', '3':'C', '4':'D', '5':'E', '6':'F', '7':'G', '8':'H', '9':'I', '10':'J'}

    def game_welcome(self):
        print("Welcome to Battleships!")
        print("Try to find the computers battleship before you run out of lives!")
        print("Let the games begin!\n")
        setup.user_input_error_handling()

    def user_input_error_handling(self):
        while True:
            try:
                self.user_gameboard_size_choice = int(input("First, pick your game board size. Select a number between 2 - 10: "))
                while self.user_gameboard_size_choice > 10 or self.user_gameboard_size_choice < 2:
                    self.user_gameboard_size_choice = int(input("Oops! Please select a number between 2 - 10: "))
                break
            except(ValueError):
                print("Oops! Please select a number between 2 - 10: ")

    def game_difficulty(self):
        while True:
            try:
                print("\nNow, how hard do you want to make it?\n" + ("\n".join(self.difficulty_options)))
                self.user_selected_difficulty = int(input("\nPick your difficulty: "))
                while self.user_selected_difficulty not in self.options:
                    self.user_selected_difficulty = int(input("\nPick your difficulty - " + (" ".join(self.difficulty_options)) + ": "))
                break

            except(ValueError):
                print("Oops! Please select an option! ")

        if self.user_selected_difficulty == 1:
            self.calculated_number_of_turns = int(math.ceil((self.user_gameboard_size_choice ** 2) * 0.75))
        elif self.user_selected_difficulty == 2:
            self.calculated_number_of_turns = int(math.ceil((self.user_gameboard_size_choice ** 2) * 0.5))
        else:
            self.calculated_number_of_turns = int(math.ceil((self.user_gameboard_size_choice ** 2) * 0.25))



    def board_creation(self):
        for i in range(0, self.user_gameboard_size_choice):
            self.build_gameboard.append([str(i + 1)])
            self.build_gameboard[i].append(["O"] * self.user_gameboard_size_choice)
            self.flattened_gameboard_build = [item for sublist in self.build_gameboard for item in sublist]

        self.flattened_gameboard_build = [item for sublist in self.flattened_gameboard_build for item in sublist]

        for i, num in enumerate(self.flattened_gameboard_build):
            if num in self.numbers_to_letters_dictionary:
                self.flattened_gameboard_build[i]  = self.numbers_to_letters_dictionary.get(num)

        self.gameboard = [self.flattened_gameboard_build[x:x + self.user_gameboard_size_choice + 1] for x in range(0, len(self.flattened_gameboard_build), self.user_gameboard_size_choice + 1)]
        self.gameboard.insert(0, list(range(0, self.user_gameboard_size_choice + 1)))



    def print_board(self):
        print("\nYour board: ")
        for row in self.gameboard:
            print("  ".join(map(str, row)))


class TheGame:
    def __init__(self):
        self.user_guess_row = ''
        self.converted_user_guess_row = int()
        self.user_guess_col = 0
        self.turn = 1
        self.number_of_guesses = setup.calculated_number_of_turns
        self.computer_battleship_row = randint(1, setup.user_gameboard_size_choice - 1)
        self.computer_battleship_column = randint(1, setup.user_gameboard_size_choice - 1)
        self.converted_computer_battleship_row = ''

    def user_guesses(self):
        game.input_validity_checks()

    def input_validity_checks(self):

        try:
            self.user_guess_row = str(input("\nGuess Row: "))
            self.user_guess_row = self.user_guess_row.upper()

            if self.user_guess_row.isalpha() == False:
                raise NameError

            self.user_guess_col = int(input("Guess Column: "))
            if self.user_guess_col not in range(1, setup.user_gameboard_size_choice + 1):
                raise ValueError
        except(NameError):
            print("Oops! Please enter a row letter.")
            game.user_guesses()
        except(ValueError):
            print("Oops! Please enter a number.")
            game.user_guesses()

    def run_game(self):
        while self.turn <= self.number_of_guesses:
            print("\n----------------")
            print("\nTurn", (self.turn))
            setup.print_board()
            game.user_guesses()

            for k,v in setup.numbers_to_letters_dictionary.items():
                if v in self.user_guess_row:
                    self.converted_user_guess_row = int(k)
                if k in str(self.computer_battleship_row):
                    self.converted_computer_battleship_row = str(v)




            # if statement to stop if battleship is sunk; breaks loop if triggered
            if self.converted_user_guess_row == self.computer_battleship_row and self.user_guess_col == self.computer_battleship_column:
                print("\nCongratulations! You sank my battleship!")
                setup.gameboard[self.computer_battleship_row][self.computer_battleship_column] = "B"
                setup.print_board()
                break

            # else statements for other scenarios
            else:
                if self.converted_user_guess_row not in range(0, setup.user_gameboard_size_choice + 1) or self.user_guess_col not in range(0, setup.user_gameboard_size_choice + 1):
                    print("\nOops, that's not even in the ocean.")
                    self.turn = self.turn - 1
                elif setup.gameboard[self.converted_user_guess_row][self.user_guess_col] == "X":
                    print("You guessed that one already.")
                    self.turn = self.turn - 1
                else:
                    print("\nYou missed my battleship!")
                    setup.gameboard[self.converted_user_guess_row][self.user_guess_col] = "X"
                if self.turn == self.number_of_guesses:
                    print("\nGame Over! \n" + "My battleship was in: " + str(self.converted_computer_battleship_row) + str(self.computer_battleship_column))
                    setup.gameboard[self.computer_battleship_row][self.computer_battleship_column] = "B"
                    setup.print_board()
                    break
            self.turn += 1


while True:
    setup = GameSetup()
    setup.game_welcome()
    setup.game_difficulty()
    setup.board_creation()

    game = TheGame()
    game.run_game()
    start_again = input("\nPress C to play again, or Q to quit: ")
    start_again.lower()
    if start_again == "q":
        print("Goodbye!")
        sleep(2)
        break
