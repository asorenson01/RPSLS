from player import Player


class Human(Player):
    def __init__(self):
        self.name = input("Please Enter your name")
        super().__init__()

    def human_methods(self):
        pass
