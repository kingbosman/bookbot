def get_num_words(string):
    return len(string.split())


def get_character_count(string):
    dict = {}
    for c in string:
        letter = c.lower()
        if letter not in dict:
            dict[letter] = 1
        else:
            dict[letter] += 1

    return dict
