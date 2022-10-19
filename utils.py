def to_byte_array(s, num_symbols, num_colors, repetition):
    if len(s) != num_symbols:
        return f'Неправильное кол-во символов.\n' \
               f'Их должно быть ровно {num_symbols}.\n' \
               f'Если хотите выйти, напишите /exit.'

    array = bytearray()
    for i in s:
        if i.isdigit():
            t = int(i)
            if 1 <= t <= num_colors:
                array.append(t - 1)
            else:
                return f'Можно вводить только цифры от 1 до {num_colors}.\n' \
                       f'У вас присутствует цифра {t}.\n' \
                       f'Если хотите выйти, напишите /exit.'
        else:
            return f'Можно вводить только цифры от 1 до {num_colors}.\n' \
                   f'У вас присутствует символ "{i}".\n' \
                   f'Если хотите выйти, напишите /exit.'

    if not repetition:
        if len(array) != len(set(array)):
            return 'Мы играем без повторений цифр.\n' \
                   f'Если хотите выйти, напишите /exit.'

    return array
