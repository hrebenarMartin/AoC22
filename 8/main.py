def is_visible(trees, posx, posy) -> int:
    if posx == 0 or posy == 0 or posx == len(trees) - 1 or posy == len(trees[i]) - 1:
        return 1

    _l = check_blocking(trees, posx, posy, 0, -1, trees[posx][posy])
    _r = check_blocking(trees, posx, posy, 0, 1, trees[posx][posy])
    _b = check_blocking(trees, posx, posy, 1, 0, trees[posx][posy])
    _t = check_blocking(trees, posx, posy, -1, 0, trees[posx][posy])

    r = _l or _r or _b or _t

    return int(r)


def calculate_scenic_score(trees, posx, posy) -> int:
    _ls = check_view(trees, posx, posy, 0, -1, trees[posx][posy])
    _rs = check_view(trees, posx, posy, 0, 1, trees[posx][posy])
    _bs = check_view(trees, posx, posy, 1, 0, trees[posx][posy])
    _ts = check_view(trees, posx, posy, -1, 0, trees[posx][posy])

    r2 = _ls * _rs * _bs * _ts

    return r2


def check_blocking(trees, pos_x, pos_y, off_x, off_y, og_height) -> bool:
    if pos_x == 0 or pos_y == 0 or pos_x == len(trees) - 1 or pos_y == len(trees[i]) - 1:
        return trees[pos_x][pos_y] < og_height
    return trees[pos_x + off_x][pos_y + off_y] < og_height and check_blocking(trees, pos_x + off_x, pos_y + off_y,
                                                                              off_x, off_y, og_height)


def check_view(trees, pos_x, pos_y, off_x, off_y, og_height, distance=0) -> int:
    if pos_x == 0 or pos_y == 0 or pos_x == len(trees) - 1 or pos_y == len(trees[i]) - 1:
        return distance
    if trees[pos_x + off_x][pos_y + off_y] < og_height:
        return check_view(trees, pos_x + off_x, pos_y + off_y, off_x, off_y, og_height, distance + 1)
    return distance + 1


if __name__ == '__main__':
    trees, r1, r2 = [], 0, 0
    with open('data.txt', 'r') as file:
        for line in file:
            trees.append(line.strip())
    for i in range(0, len(trees)):
        for j in range(0, len(trees[i])):
            r1 += is_visible(trees, i, j)
            r2 = max(r2, calculate_scenic_score(trees, i, j))
    print(f'Result 1: {r1}')
    print(f'Result 2: {r2}')
