size = 42
center_ix = size // 2 - 1
state = [['.'] * size for _ in range(size)]
visited = set()

# For checking result of part 2, increase knots_count to 10
knots_count = 10
knots = [[center_ix, center_ix] for _ in range(knots_count)]
print(knots)
pos_h = [center_ix, center_ix]
pos_t = [center_ix, center_ix]


def reset_state():
    global state
    state = [['.'] * size for i in range(size)]
    for _vis in visited:
        state[_vis[0]][_vis[1]] = '#'
    for ix in range(len(knots) - 1, -1, -1):
        if ix == 0:
            state[knots[ix][0]][knots[ix][1]] = 'H'
        else:
            state[knots[ix][0]][knots[ix][1]] = str(ix)
    print(*[''.join(row) for row in state], sep='\n')
    print()


def move_knot(knot_ix=0):
    if knot_ix == len(knots) - 1:
        visited.add((knots[knot_ix][0], knots[knot_ix][1]))

    pos_d_x = knots[knot_ix - 1][0] - knots[knot_ix][0]
    pos_d_y = knots[knot_ix - 1][1] - knots[knot_ix][1]

    if abs(pos_d_x) <= 1 and abs(pos_d_y) <= 1:
        print(f'Knot {knot_ix} does not need to move.')
        return

    if pos_d_x == 0:  # Horizontally
        knots[knot_ix][1] = knots[knot_ix][1] + (pos_d_y - 1 if pos_d_y > 0 else pos_d_y + 1)
        ...
    elif pos_d_y == 0:  # Vertically
        knots[knot_ix][0] = knots[knot_ix][0] + (pos_d_x - 1 if pos_d_x > 0 else pos_d_x + 1)
        ...
    else:  # Diagonally
        if abs(pos_d_x) == 1:
            knots[knot_ix][0] = knots[knot_ix][0] + pos_d_x
            knots[knot_ix][1] = knots[knot_ix][1] + (pos_d_y - 1 if pos_d_y > 0 else pos_d_y + 1)
            ...
        elif abs(pos_d_y) == 1:
            knots[knot_ix][0] = knots[knot_ix][0] + (pos_d_x - 1 if pos_d_x > 0 else pos_d_x + 1)
            knots[knot_ix][1] = knots[knot_ix][1] + pos_d_y
            ...
        elif abs(pos_d_x) == 2 or abs(pos_d_y) == 2:
            knots[knot_ix][0] = knots[knot_ix][0] + (pos_d_x - 1 if pos_d_x > 0 else pos_d_x + 1)
            knots[knot_ix][1] = knots[knot_ix][1] + (pos_d_y - 1 if pos_d_y > 0 else pos_d_y + 1)
            ...

    print(f'Position difference of knot {knot_ix - 1} and {knot_ix} = (row:col) {pos_d_x}:{pos_d_y}')


def move(direction, count) -> None:
    if count == 0:
        return
    if direction == 'R':
        print("Head moved RIGHT")
        knots[0][0], knots[0][1] = knots[0][0], knots[0][1] + 1
        ...
    elif direction == 'L':
        print("Head moved LEFT")
        knots[0][0], knots[0][1] = knots[0][0], knots[0][1] - 1
        ...
    elif direction == 'U':
        print("Head moved UP")
        knots[0][0], knots[0][1] = knots[0][0] - 1, knots[0][1]
        ...
    else:
        print("Head moved DOWN")
        knots[0][0], knots[0][1] = knots[0][0] + 1, knots[0][1]
        ...

    for knot_ix in range(1, len(knots)):
        move_knot(knot_ix)

    reset_state()
    move(direction, count - 1)


if __name__ == '__main__':
    with open('_data2.txt', 'r') as file:
        reset_state()
        for _line in file:
            line = _line.strip().split(' ')
            move(line[0], int(line[1]))
        print(f'Tail visited {len(visited)} unique positions')
