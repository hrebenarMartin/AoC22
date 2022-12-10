if __name__ == '__main__':
    with open('data.txt', 'r') as file:
        line = file.readline().strip()
        marker_pos = -1
        for i in range(0, len(line) - 4):
            if len(set(line[i:i + 4])) == 4:
                marker_pos = i + 4
                print(f'R1: Found marker packet. Ending on position {marker_pos}')
                break

        for i in range(0, len(line) - 14):
            if len(set(line[i:i + 14])) == 14:
                print(f'R2: Found message packet. Ending on position {i + 14}')
                break
