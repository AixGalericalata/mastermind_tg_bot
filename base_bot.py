class BaseBot:
    def __init__(self, num_colors, num_symbols, repetition):
        self.num_colors = num_colors
        self.num_symbols = num_symbols
        self.repetition = repetition

    def check(self, guess):
        pass

    def get_greeting(self):
        msg = 'с повторениями' if self.repetition else 'без повторений'
        return f'Я загадал комбинацию из {self.num_symbols} цифр от 1 до ' \
               f'{self.num_colors} {msg}.\n' \
               f'Попробуйте её отгадать!'

    def get_answer(self):
        pass