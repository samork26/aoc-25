def read_input(file_path):
    with open(file_path, 'r') as file:
        return [line.strip() for line in file]

def main():
    pos = 50
    part1_count = 0

    pos2 = 50
    part2_count = 0

    instructions = read_input("dec1_input.txt")

    for instruction in instructions:
        direction = instruction[0]
        value = int(instruction[1:])
        step = 1 if direction == 'R' else -1

        # PART 1: only final positions
        new_pos = (pos + step * value) % 100
        pos = new_pos
        if pos == 0:
            part1_count += 1

        # PART 2: count every click
        for _ in range(value):
            pos2 = (pos2 + step) % 100
            if pos2 == 0:
                part2_count += 1

    print("Part 1:", part1_count)
    print("Part 2:", part2_count)

if __name__ == "__main__":
    main()
