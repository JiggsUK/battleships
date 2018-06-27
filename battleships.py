"""A program to run a game of battleships that is one player with a single ship hidden in a user chosen
grid. The player will have a set number of guesses to try to sink the ship """

# import the random integer function to place the battleship
from random import randint
from time import *

# TODO statistics for each game - wins/losses
# TODO print a list of previous guesses? - NO. Board is a record of that


class GameSetup:
    def __init__(self):
        self.user_size_choice = int()
        self.gameboard = []
        self.ship_row = int()
        self.ship_column = int()
        self.difficulty_list =[ '1 for Easy', '2 for Normal', '3 for Hard']
        self.options = [1, 2, 3]
        self.user_difficulty = 0
        self.gamedifficulty = 0


    def game_welcome(self):
        print("Welcome to Battleships!")
        print("Try to find the computers battleship before you run out of lives!")
        print("Let the games begin!\n")
        setup.valid_game_check()

    def game_difficulty(self):
        while True:
            try:
                print("\nNow, how hard do you want to make it?\n" + ("\n".join(self.difficulty_list)))
                self.user_difficulty = int(input("\nPick your difficulty: "))
                while self.user_difficulty not in self.options:
                    self.user_difficulty = int(input("\nPick your difficulty - " + (" ".join(self.difficulty_list)) + ": "))
                break

            except(ValueError):
                print("Oops! Please try again! ")


        if self.user_difficulty == 1:
            self.gamedifficulty = self.user_size_choice * 2
        elif self.user_difficulty == 2:
            self.gamedifficulty = self.user_size_choice
        else:
            self.gamedifficulty = self.user_size_choice / 2


    def valid_game_check(self):
        while True:
            try:
                self.user_size_choice = int(input("First, pick your game board size. Select a number between 2 - 20: "))
                while self.user_size_choice > 20 or self.user_size_choice < 2:
                    self.user_size_choice = int(input("Oops! Please select a number between 2 - 20: "))
                break
            except(ValueError):
                print("Oops! Please select a number between 2 - 20: ")

    def board_size(self):
        # print(self.user_size_choice)
        self.ship_row = randint(0, self.user_size_choice - 1)
        self.ship_column = randint(0, self.user_size_choice - 1)
        # print(self.ship_row, self.ship_column)
        for i in range(0, self.user_size_choice):
            self.gameboard.append([" o "] * self.user_size_choice)

    def print_board(self):

        print("\nYour board: ")
        for row in self.gameboard:
            print(" ".join(row))


class TheGame:
    def __init__(self):
        self.guess_row = 0
        self.guess_col = 0
        self.indexed_guess_row = 0
        self.indexed_guess_col = 0
        self.turn = 1
        self.number_of_guesses = setup.gamedifficulty
        self.start_again = ''

    def input_validity_checks(self):
        while True:
            try:
                self.guess_row = int(input("\nGuess Row: "))
                self.guess_col = int(input("Guess Column: "))
                break
            except(ValueError):
                print("Oops! Please enter a number.")



    def run_game(self):
        while self.turn <= self.number_of_guesses:
            print("\n----------------")
            print("\nTurn", (self.turn))
            setup.print_board()
            game.input_validity_checks()

            self.indexed_guess_row = self.guess_row - 1
            self.indexed_guess_col = self.guess_col - 1

            # if statement to stop if battleship is sunk; breaks if triggered
            if self.indexed_guess_row == setup.ship_row and self.indexed_guess_col == setup.ship_column:
                print("\nCongratulations! You sank my battleship!")
                setup.gameboard[setup.ship_row][setup.ship_column] = " B "
                setup.print_board()
                break
            # else statements for other scenarios
            else:
                if self.indexed_guess_row not in range(0, setup.user_size_choice) or self.indexed_guess_col not in range(0, setup.user_size_choice):
                    print("\nOops, that's not even in the ocean.")
                    self.turn = self.turn - 1
                elif setup.gameboard[self.indexed_guess_row][self.indexed_guess_col] == " X ":
                    print("You guessed that one already.")
                    self.turn = self.turn - 1
                else:
                    print("\nYou missed my battleship!")
                    setup.gameboard[self.indexed_guess_row][self.indexed_guess_col] = " X "
                if self.turn == self.number_of_guesses:
                    print("\nGame Over! \n" + "My battleship was in row: " + str(setup.ship_row + 1) + " and column: " + str(setup.ship_column + 1))
                    setup.gameboard[setup.ship_row][setup.ship_column] = " B "
                    setup.print_board()
                    break
            self.turn += 1


while True:
    setup = GameSetup()
    setup.game_welcome()
    setup.game_difficulty()
    setup.board_size()

    game = TheGame()
    game.run_game()
    start_again = input("\nPress C to play again, or Q to quit: ")
    start_again.lower()
    if start_again == "q":
        print("Goodbye!")
        sleep(2)
        break

