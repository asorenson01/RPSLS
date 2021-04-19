from player import Player


class Computer(Player):
    def __init__(self):
        self.name = "HAL 9000"
        super().__init__()

    def computer_methods(self):
        pass