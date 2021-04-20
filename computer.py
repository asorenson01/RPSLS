import random

from player import Player


class Computer(Player):
    def __init__(self):
        self.name = "HAL 9000"
        print("Downloading HAL 9000........ Preparing HAL 9000 for the Match")
        print(f"HAL 9000 Prints '(This Game is too important for me to allow you to win!)'")
        super().__init__()

    def turn(self):
        computer_choice = random.randint(0, 4)
        print(f"Hall 9000 has selected {self.gestures[computer_choice]}")
        return computer_choice

    def computer_methods(self):
        pass
