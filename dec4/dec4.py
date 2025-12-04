def read_grid(path):
    grid = []
    with open(path, "r") as f:
        for line in f:
            line = line.strip()
            if line:
                grid.append(list(line))
    return grid


DIRS = [
    (-1, -1), (-1, 0), (-1, 1),
    ( 0, -1),          ( 0, 1),
    ( 1, -1), ( 1, 0), ( 1, 1)
]

def neighbors(r, c, rows, cols):
    for dr, dc in DIRS:
        nr, nc = r + dr, c + dc
        if 0 <= nr < rows and 0 <= nc < cols:
            yield nr, nc

def count_adjacent_at(grid, r, c, rows, cols):
    return sum(
        1 for nr, nc in neighbors(r, c, rows, cols)
        if grid[nr][nc] == '@'
    )

def main():
    grid = read_grid("dec4_input.txt")
    rows, cols = len(grid), len(grid[0])

    pt1_valid_count = 0

    for r in range(rows):
        for c in range(cols):
            if grid[r][c] == '@':
                adjacent = count_adjacent_at(grid, r, c, rows, cols)
                if adjacent < 4:
                    pt1_valid_count += 1

    print("Part 1:", pt1_valid_count)


if __name__ == "__main__":
    main()
