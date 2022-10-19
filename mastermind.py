def bulls_cows(s1, s2):
    s1_copy = s1.copy()
    s2_copy = s2.copy()
    n = len(s1_copy)

    assert (n == len(s2_copy))

    invalid = 255
    cows = 0
    bulls = 0

    for i in range(n):
        if s1_copy[i] == s2_copy[i]:
            bulls += 1
            s1_copy[i] = invalid
            s2_copy[i] = invalid

    for i in range(n):
        s1_copy_i = s1_copy[i]
        if s1_copy_i == invalid:
            continue
        for j in range(n):
            if s1_copy_i == s2_copy[j]:
                cows += 1
                s2_copy[j] = invalid
                break

    return bulls, cows