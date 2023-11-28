from typing import List
from collections import defaultdict


def largestIsland(grid: List[List[int]]) -> int:
    if not grid:
        return 0

    def search(row, col, key, seen):
        if 0 <= row < len(grid) and 0 <= col < len(grid[0]) and (row, col) not in seen and grid[row][col] != 0:
            grid[row][col] = key
            seen.add((row, col))
            return (search(row + 1, col, key, seen) +
                    search(row - 1, col, key, seen) +
                    search(row, col + 1, key, seen) +
                    search(row, col - 1, key, seen)) + 1
        else:
            return 0

    island_map = defaultdict(int)
    key = 1
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if grid[i][j] == 1:
                key += 1
                area = search(i, j, key, set())
                island_map[key] = area

    # found no islands
    if key == 1:
        return 1
    res = 0
    # search through every water tile and see if we can connect any islands together
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if grid[i][j] == 0:
                seen = set()
                area = 0
                for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                    r = i + dx
                    c = j + dy

                    if 0 <= r < len(grid) and 0 <= c < len(grid[0]):
                        key = grid[r][c]
                        if key not in seen:
                            seen.add(key)
                            area += island_map[key]
                res = max(res, area + 1)

    # found no water tile to replace
    if res == 0:
        return island_map[key]
    return res


print(largestIsland(
    [[0, 0, 0, 0, 0, 0, 0],
     [0, 1, 1, 1, 1, 0, 0],
     [0, 1, 0, 0, 1, 0, 0],
     [1, 0, 1, 0, 1, 0, 0],
     [0, 1, 0, 0, 1, 0, 0],
     [0, 1, 0, 0, 1, 0, 0],
     [0, 1, 1, 1, 1, 0, 0]]))
