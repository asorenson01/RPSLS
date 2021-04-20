from player import Player


class Computer(Player):
    def __init__(self):
        self.name = "HAL 9000"
        print("Downloading HAL 9000........ Preparing HAL 9000 for the Match")
        print(f"HAL 9000 Prints '(This Game is too important for me to allow you to win!)'")
        super().__init__()

    def computer_methods(self):
        pass
