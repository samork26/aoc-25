def read_input(file_path):
    with open(file_path, 'r') as f:
        return f.read().strip()

def parse_ranges(text):
    ranges = []
    for segment in text.split(","):
        start, end = segment.split("-")
        ranges.append((int(start), int(end)))
    return ranges

def sum_invalid_ids(ranges):
    total = 0

    for low, high in ranges:
        low_len = len(str(low))
        high_len = len(str(high))

        for length in range(low_len, high_len + 1):
            if length % 2 != 0:
                continue

            half = length // 2
            start_prefix = 10 ** (half - 1)
            end_prefix = 10 ** half

            for prefix in range(start_prefix, end_prefix):
                repeated = int(str(prefix) + str(prefix))

                if repeated < low:
                    continue
                if repeated > high:
                    break

                total += repeated

    return total

def is_primitive(s):
    return s not in (s + s)[1:-1]

def sum_invalid_ids_part2(ranges):
    total = 0

    for low, high in ranges:
        low_len = len(str(low))
        high_len = len(str(high))

        for total_len in range(low_len, high_len + 1):
            for pat_len in range(1, total_len // 2 + 1):
                if total_len % pat_len != 0:
                    continue

                k = total_len // pat_len
                if k < 2:
                    continue

                for prefix in range(10**(pat_len - 1), 10**pat_len):
                    pat = str(prefix)
                    if not is_primitive(pat):
                        continue

                    repeated = int(pat * k)

                    if repeated < low:
                        continue
                    if repeated > high:
                        break

                    total += repeated

    return total

def main():
    text = read_input("dec2_input.txt")
    ranges = parse_ranges(text)
    result1 = sum_invalid_ids(ranges)
    result2 = sum_invalid_ids_part2(ranges)
    
    print("Part 1:", result1)
    print("Part 2:", result2)

if __name__ == "__main__":
    main()
