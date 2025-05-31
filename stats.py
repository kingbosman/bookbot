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


def sort_on(dict):
    return dict["num"]


def sorted_count(dict):
    result = []
    for i, v in dict.items():
        result.append({"char": i, "num": v})

    result.sort(reverse=True, key=sort_on)
    return result
