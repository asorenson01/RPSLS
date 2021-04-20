from player import Player
from validation import Validation


class Human(Player):
    def __init__(self):
        self.name = input("Please Enter your name")
        super().__init__()

    def turn(self):
        human_choice = 0
        print(f"{self.name}")
        for i in range(len(self.gestures)):
            print(f"Press {i+1} to select {self.gestures[i]}")
        human_choice = Validation.input_number(self,"waiting for selection")
        human_choice -= 1

        if human_choice > 4:
            print(" That gesture was not offered lets try again")
            self.turn()
        else:
            print(f"You have selected {self.gestures[human_choice]}")
            return human_choice


    def human_methods(self):
        pass
