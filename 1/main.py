if __name__ == "__main__":
    with open('data.txt', 'r') as file:
        data = file.read()
        # Day 1 Part 1
        print(max(sum([int(i) for i in y.split('\n')]) for y in data.split('\n\n')))

        # Day 1 Part 2
        print(sum(sorted([sum([int(i) for i in y.split('\n')]) for y in data.split('\n\n')], reverse=True)[0:3]))
