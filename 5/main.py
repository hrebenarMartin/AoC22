if __name__ == '__main__':
    with open('data.txt', 'r') as file:
        state, state2, size, loaded = [], [], 0, False
        for line in file:
            if size == 0:
                size = len(line) // 4
                state = ['' * size for i in range(size)]

            if len(line.strip()) == 0:
                continue

            # Check if state data are all loaded
            if line.strip()[0] == '1':
                loaded = True
                state2 = state.copy()
                continue

            # Read input state or read instructions when state is loaded
            if not loaded:
                for i in range(0, len(line), 4):
                    state[i // 4] = state[i // 4] + line[i:i + 4].strip().strip('[]')
            else:
                instructions = line.strip().split(' ')
                how_many, stack_from, stack_to = int(instructions[1]), int(instructions[3]) - 1, int(
                    instructions[5]) - 1
                to_move = state[stack_from][0:how_many][::-1]
                to_move2 = state2[stack_from][0:how_many]
                state[stack_from] = state[stack_from][how_many:len(state[stack_from])]
                state2[stack_from] = state2[stack_from][how_many:len(state2[stack_from])]
                state[stack_to] = to_move + state[stack_to]
                state2[stack_to] = to_move2 + state2[stack_to]
        print(f"All instructions processed.")
        print(f"\tResult 1: {''.join([x[0] for x in state])}")
        print(f"\tResult 2: {''.join([x[0] for x in state2])}")
        ...

# ---_---_---_---_---_---_---_---
