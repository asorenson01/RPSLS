import time
class Player:

    def __init__(self):
        self.gestures = ["Rock", "Paper", "Scissors", "Lizard", "Spock"]
        self.score = 0

    def round_winner(self, x, word, y, winner, looser):
        self.score += 1
        print(
            f"{winner.name}'s {winner.gestures[y]} {word} {looser.name}'s {looser.gestures[x]}")
        time.sleep(.500)

    def play_method(self):
        pass
