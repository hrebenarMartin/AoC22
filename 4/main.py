if __name__ == '__main__':
    with open('data.txt', 'r') as file:
        r1, r2 = 0, 0
        for line in file:
            elf1, elf2 = [x.split('-') for x in line.strip().split(',')]
            range1 = set(range(int(elf1[0]), int(elf1[1]) + 1))
            range2 = set(range(int(elf2[0]), int(elf2[1]) + 1))
            if range1.issubset(range2) or range2.issubset(range1):
                r1 += 1
            if len(range1.intersection(range2)) > 0:
                r2 += 1
        print(f'Result 1: {r1}')
        print(f'Result 2: {r2}')
