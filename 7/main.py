def get_dir_size(lines, size, dir, dirs) -> int:
    current_dir_size = 0
    while True:
        try:
            line = next(lines).strip().split(' ')
            if line[0] == '$' and line[1] == 'cd':
                if line[2] == '..':
                    dirs[dir] = current_dir_size
                    return size + current_dir_size
                current_dir_size = get_dir_size(lines, current_dir_size, dir + '/' + line[2], dirs)
            elif line[0] == '$' and line[1] == 'ls':
                continue
            elif line[0] != 'dir':
                current_dir_size += int(line[0])
        except StopIteration:
            break
    dirs[dir] = current_dir_size
    return size + current_dir_size


if __name__ == '__main__':
    dirs, TOTAL, REQUIRED = {}, 70_000_000, 30_000_000

    with open('data.txt', 'r') as file:
        lines = iter(file)
        final_size = get_dir_size(lines, 0, '/', dirs)
        r1, candidates = 0, []
        for key, value in dirs.items():
            if TOTAL - (final_size - value) >= REQUIRED:
                candidates.append((key, value))
            if value <= 100_000:
                r1 += value
        print(f'Result 1: {r1}')
        print(f'Result 2: {min(x[1] for x in candidates)}')
