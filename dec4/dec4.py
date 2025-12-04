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

def simulate_removal_rounds(grid):
    R, C = len(grid), len(grid[0])
    total = 0

    while True:
        to_remove = []

        for r in range(R):
            for c in range(C):
                if grid[r][c] == '@':
                    if count_adjacent_at(grid, r, c, R, C) < 4:
                        to_remove.append((r, c))

        if not to_remove:
            break

        for r, c in to_remove:
            grid[r][c] = '.'

        total += len(to_remove)

    return total

def main():
    grid = read_grid("dec4_input.txt")
    rows, cols = len(grid), len(grid[0])
    part1 = 0
    for r in range(rows):
        for c in range(cols):
            if grid[r][c] == '@':
                if count_adjacent_at(grid, r, c, rows, cols) < 4:
                    part1 += 1

    print("Part 1:", part1)
    
    import copy
    g2 = copy.deepcopy(grid)
    rows2, cols2 = rows, cols

    total_removed = 0

    while True:
        to_remove = []

        for r in range(rows2):
            for c in range(cols2):
                if g2[r][c] == '@':
                    if count_adjacent_at(g2, r, c, rows2, cols2) < 4:
                        to_remove.append((r, c))

        if not to_remove:
            break

        for r, c in to_remove:
            g2[r][c] = '.'

        total_removed += len(to_remove)

    print("Part 2:", total_removed)

if __name__ == "__main__":
    main()
