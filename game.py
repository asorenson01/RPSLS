import human
from human import Human
from computer import Computer


class Game:
    def __init__(self):
        self.play_one = " "
        self.play_two = " "

    def play_the_game(self):
        self.select_players()

    def select_players(self):
        x = int(input("Press 1 for 1 Player game.  Press 2 for a 2 player game"))
        if x == 1 or x == 2:
            if x == 1:
                self.play_one = Human()
                self.play_two = Computer()
            elif x == 2:
                self.play_one = Human()
                self.play_two = Human()
        else:
            print("That is not a valid entry please try again")



    def welcome_message(self):
        pass

    def game_table(self):
        pass

    def game_mech(self):
        pass

    def game_winner(self):
        pass
