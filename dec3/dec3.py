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

def two_joltage_optimized(bank):
    n = len(bank)

    #---------------------
    #    BACKWARD SCAN 
    #---------------------

    # Biggest digit that will appear after index i
    right_max = [None] * n

    # biggest digit we've seen so far from the right
    biggest_seen = None

    # start at the end and iterate backwards
    for i in range(n - 2, -1, -1):
        next_digit = bank[i + 1]
        
        # update biggest_seen if needed
        if biggest_seen is None or next_digit > biggest_seen:
            biggest_seen = next_digit
        
        # store biggest digit available to the right of i
        right_max[i] = biggest_seen

    #---------------------
    #    FORWARD SCAN 
    #---------------------

    best_value = -1
    for i in range(n):
        
        # the best digit to the right of bank[i]
        partner = right_max[i]

        # if there is no digit to the right, skip
        if partner is None:
            continue
        
        # form the 2-digit number using the current digit and it's partner
        candidate = int(bank[i] + partner)
        if candidate > best_value:
            best_value = candidate

    return best_value

def main():
    banks = read_input("dec3_input.txt")
    
    pt1_total, pt2_total, pt1_total_optimized = 0, 0, 0

    for bank in banks:
        pt1_total += two_joltage(bank)
        pt1_total_optimized += two_joltage_optimized(bank)
        pt2_total += twelve_joltage(bank)
    
    print("Part 1:", pt1_total)
    print("Part 2:", pt2_total)
    print("Part 1 Optimized:", pt1_total_optimized)

if __name__ == "__main__":
    main()
