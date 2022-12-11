cycles = 0
new_val = None
cycles_skip = 1
reg_x = 1
value_archive = []

if __name__ == '__main__':
    with open('data.txt', 'r') as file:
        lines = iter(file)
        while True:
            try:
                cycles_skip -= 1
                cycles += 1

                if cycles_skip == 0 and new_val is not None:
                    reg_x, new_val = reg_x + new_val, None

                if cycles % 20 == 0:
                    value_archive.append(cycles * reg_x)

                draw_pixel = False
                if (cycles - 1) % 40 in (reg_x - 1, reg_x, reg_x + 1):
                    draw_pixel = True
                print('#' if draw_pixel else '.', end="\n" if cycles % 40 == 0 else "")

                if cycles_skip != 0:
                    continue

                line = next(lines).strip().split()

                if line[0] == 'noop':
                    cycles_skip += 1
                else:
                    cycles_skip += 2
                    new_val = int(line[1])
            except StopIteration:
                break

    print(f'Result 1: {sum([value_archive[x] for x in range(0, len(value_archive), 2)])}')
