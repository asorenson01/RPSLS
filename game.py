import human
from human import Human
from computer import Computer
from validation import Validation


class Game:
    def __init__(self):
        self.play_one = " "
        self.play_two = " "
        self.counter = 0

    def play_the_game(self):
        self.select_players()
        self.welcome_message()

    def select_players(self):
        x = Validation.input_number(self,"Press 1 for 1 Player game.  Press 2 for a 2 player game")
        if x == 1 or x == 2:
            if x == 1:
                self.play_one = Human()
                self.play_two = Computer()
            elif x == 2:
                self.play_one = Human()
                self.play_two = Human()
        else:
            print("That is not a valid entry please try again")
            self.select_players()

    def welcome_message(self):
        print(f"Welcome to this match of Rock, Paper, Scissors, Lizard, Spock ")
        print(f"Today's match up will be {self.play_one.name} versus {self.play_two.name}")
        pass

    def game_table(self):
        pass

    def game_mech(self):
        pass

    def game_winner(self):
        pass
