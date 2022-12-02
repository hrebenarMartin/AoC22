def evaluate_round_p1(choices) -> int:
    diff = ord(choices[0]) - (ord(choices[1]) - 23)
    choice_value = ord(choices[1]) - 87
    if diff == 0:
        return 3 + choice_value
    elif diff == 2 or diff == -1:
        return 6 + choice_value
    return choice_value


def evaluate_round_p2(round_data) -> int:
    _i, _w, _l = ['A', 'B', 'C'], ['B', 'C', 'A'], ['C', 'A', 'B']
    if round_data[1] == 'Y':
        return 3 + (ord(round_data[0]) - 64)
    elif round_data[1] == 'Z':
        return 6 + (ord(_w[_i.index(round_data[0])]) - 64)
    return ord(_l[_i.index(round_data[0])]) - 64


if __name__ == '__main__':
    with open('data.txt', 'r') as file:
        print(sum(evaluate_round_p1(line.strip().split(' ')) for line in file))

    with open('data.txt', 'r') as file:
        print(sum(evaluate_round_p2(line.strip().split(' ')) for line in file))
