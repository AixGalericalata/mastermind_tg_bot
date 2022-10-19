import random
from mastermind import bulls_cows
from base_bot import BaseBot


class SimpleBot(BaseBot):
    def __init__(self, num_colors, num_symbols, repetition):
        super().__init__(num_colors, num_symbols, repetition)
        self.enigma = bytearray()
        if repetition:
            for i in range(num_symbols):
                self.enigma.append(random.randrange(0, num_colors))
        else:
            self.enigma = bytearray(random.sample(range(num_colors), num_symbols))

    def check(self, guess):
        return bulls_cows(self.enigma, guess)

    def get_answer(self):
        return self.enigma