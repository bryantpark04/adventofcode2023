import itertools


def main() -> None:
    with open("input.txt") as f:
        lines = f.read().splitlines()

    n = len(lines)
    m = len(lines[0])
    total = 0

    for i in range(n):
        j = 0
        while j < m:
            if lines[i][j].isdigit():
                l = 0
                is_adjacent = False
                while j + l < m and lines[i][j + l].isdigit():
                    if any(not (ch := lines[i + di][j + l + dj]).isdigit() and ch != "." for di, dj in itertools.product((1, 0, -1), (1, 0, -1)) if 0 <= (i + di) < n and 0 <= (j + l + dj) < m):
                        is_adjacent = True
                    l += 1
                
                if is_adjacent:
                    part_num = int(lines[i][j:j+l])
                    print(part_num)
                    total += part_num
                j += l
            else:
                j += 1

    print(total)


if __name__ == "__main__":
    main()
