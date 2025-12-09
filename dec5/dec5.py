def read_input(path):
    with open(path, "r") as f:
        content = f.read().strip()

    ranges_block, ids_block = content.split("\n\n", 1)

    ranges = []
    for line in ranges_block.splitlines():
        low, high = line.split("-")
        ranges.append((int(low), int(high)))

    ids = [int(line.strip()) for line in ids_block.splitlines() if line.strip()]

    return ranges, ids

def is_fresh(ingredient_id, ranges):
    for low, high in ranges:
        if low <= ingredient_id <= high:
            return True
    return False

def count_fresh(ranges, ids):
    return sum(1 for x in ids if is_fresh(x, ranges))


def merge_ranges(ranges):
    ranges = sorted(ranges)
    merged = []

    cur_low, cur_high = ranges[0]

    for low, high in ranges[1:]:
        if low <= cur_high + 1:
            cur_high = max(cur_high, high)
        else:
            merged.append((cur_low, cur_high))
            cur_low, cur_high = low, high

    merged.append((cur_low, cur_high))
    return merged


def count_total_fresh_ids(ranges):
    merged = merge_ranges(ranges)
    total = 0

    for low, high in merged:
        total += (high - low + 1)

    return total


def main():
    ranges, ids = read_input("dec5_input.txt")

    pt1_answer = count_fresh(ranges, ids)
    print("Part 1 — Fresh ingredient count:", pt1_answer)

    pt2_answer = count_total_fresh_ids(ranges)
    print("Part 2 — Total fresh IDs:", pt2_answer)


if __name__ == "__main__":
    main()
