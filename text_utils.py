bull = '\U0001F402'
cow = '\U0001F404'


def create_text(moves):
    lines = []
    for move in moves:
        user_move = ''.join(map(lambda x: str(x + 1), move[0]))
        text = f'{user_move} {" " * 7} {bull * move[1][0]} {cow * move[1][1]}'
        lines.append(text)

    return '\n'.join(reversed(lines))
