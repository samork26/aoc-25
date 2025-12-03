def read_input(file_path):
    with open(file_path, 'r') as file:
        return [line.strip() for line in file]

def two_joltage(bank):
    best = -1
    for i in range(len(bank)):
        for j in range(i+1, len(bank)):
            value = int(bank[i] + bank[j])
            if value > best:
                best = value
    return best

def twelve_joltage(bank):
    to_drop = len(bank) - 12
    stack = []

    for digit in bank:
        while stack and to_drop > 0 and stack[-1] < digit:
            stack.pop()
            to_drop -= 1
        
        stack.append(digit)
    
    result = stack[:12]
    return int("".join(result))

def main():
    banks = read_input("dec3_input.txt")
    
    pt1_total, pt2_total = 0, 0

    for bank in banks:
        pt1_total += two_joltage(bank)
        pt2_total += twelve_joltage(bank)
    
    print("Part 1:", pt1_total)
    print("Part 2:", pt2_total)

if __name__ == "__main__":
    main()
