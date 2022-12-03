def evaluate_item_priority(item_type) -> int:
    if ord(item_type) > 96:
        return ord(item_type) - 96
    return ord(item_type) - 38


if __name__ == '__main__':
    with open('data.txt', 'r') as file:
        res1, res2, _group = 0, 0, []
        for line in file:
            _group.append(line.strip())
            intersection = set(list(line[0:len(line.strip()) // 2])).intersection(
                set(list(line[len(line.strip()) // 2: len(line.strip())]))).pop()
            res1 += evaluate_item_priority(intersection)
            if len(_group) == 3:
                intersection = set(list(_group[0])).intersection(set(list(_group[1])), set(list(_group[2]))).pop()
                res2 += evaluate_item_priority(intersection)
                _group = []
        print(f'Result 1: {res1}')
        print(f'Result 2: {res2}')
