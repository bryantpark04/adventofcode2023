import itertools


def main() -> None:
    with open("input.txt") as f:
        lines = f.read().splitlines()

    n = len(lines)
    m = len(lines[0])
    total = 0

    gears_found = {}
    gears_added = set()

    for i in range(n):
        j = 0
        while j < m:
            if lines[i][j].isdigit():
                l = 0
                gear_coords = set()
                while j + l < m and lines[i][j + l].isdigit():
                    for di, dj in itertools.product((1, 0, -1), (1, 0, -1)):
                        if 0 <= (i + di) < n and 0 <= (j + l + dj) < m:
                           if lines[i + di][j + l + dj] == "*":
                                gear_coords.add((i + di, j + l + dj))
                    l += 1
                
                if gear_coords:
                    part_num = int(lines[i][j:j+l])
                    for gear_coord in gear_coords:
                        if gear_coord in gears_found and gear_coord not in gears_added:
                            total += part_num * gears_found[gear_coord]
                            gears_added.add(gear_coord)
                            print(part_num)
                        else:
                            gears_found[gear_coord] = part_num
                j += l
            else:
                j += 1

    print(total)


if __name__ == "__main__":
    main()
