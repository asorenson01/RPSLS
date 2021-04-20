import human
from human import Human
from computer import Computer
from validation import Validation


class Game:
    def __init__(self):
        self.play_one = " "
        self.play_two = " "
        self.counter = 1

    def play_the_game(self):
        self.select_players()
        self.welcome_message()
        self.game_table()
        self.game_winner()

    def select_players(self):
        x = Validation.input_number(self, "Press 1 for 1 Player game.  Press 2 for a 2 player game")
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
        while self.counter < 4:
            print(f"Round {self.counter} current score is {self.play_one.name} has {self.play_one.score} points. While {self.play_two.name} has {self.play_two.score} points.")
            print("HERE WE GO!")
            x = self.play_one.turn()
            y = self.play_two.turn()
            self.game_mech(x, y)


    def game_mech(self, x, y):

        if x == y:
            print(f"You both Selected {self.play_one.gestures[x]} lets try again")
            self.game_table()
        elif x == 0:
            if y == 2 or y == 3:
                self.p1_win(x, "CRUSHES", y)
            elif y == 1:
                self.p2_win(x, "COVERS", y)
            elif y == 4:
                self.p2_win(x, "VAPORIZES", y)
        elif x == 1:
            if y == 0:
                self.p1_win(x, "COVERS", y)
            elif y == 4:
                self.p1_win(x, "DISPROVES", y)
            elif y == 2:
                self.p2_win(x, "CUT", y)
            elif y == 3:
                self.p2_win(x, "EATS", y)
        elif x == 2:
            if y == 1:
                self.p1_win(x, "CUTS", y)
            elif y == 3:
                self.p1_win(x, "DECAPITATES", y)
            elif y == 0:
                self.p2_win(x, "CRUSHES", y)
            elif y == 4:
                self.p2_win(x, "SMASHES", y)
        elif x == 3:
            if y == 1:
                self.p1_win(x, "EATS", y)
            elif y == 4:
                self.p1_win(x, "POISONS", y)
            elif y == 0:
                self.p2_win(x,"CRUSHES", y)
            elif y == 2:
                self.p2_win(x, "DECAPITATES", y)
        elif x ==4:
            if y == 0:
                self.p1_win(x, "VAPORIZES", y)
            elif y == 2:
                self.p1_win(x, "SMASHES", y)
            elif y == 1:
                self.p2_win(x, "DISPROVES", y)
            elif y == 3:
                self.p2_win(x, "POISONS", y)

    def p1_win(self, x, word, y):
        self.counter += 1
        self.play_one.score += 1
        print(f"{self.play_one.name}'s {self.play_one.gestures[x]} {word} {self.play_two.name}'s {self.play_two.gestures[y]}")

    def p2_win(self, x, word, y):
        self.counter += 1
        self.play_two.score += 1
        print(f"{self.play_two.name}'s {self.play_one.gestures[y]} {word} {self.play_one.name}'s {self.play_two.gestures[x]}")

    def game_winner(self):
        if self.play_one.score > self.play_two.score:
            print(f"{self.play_one.name} won with a score of {self.play_one.score} to {self.play_two.name}'s score of {self.play_two.score}")
        else:
            print(f"{self.play_two.name} won with a score of {self.play_two.score} to {self.play_one.name}'s score of {self.play_one.score}")


