def main() -> None:
    with open("input.txt") as f:
        lines = f.read().splitlines()
    
    total = 0
    
    for line in lines:
        _, line = line.split(": ")
        winning, mine = line.split(" | ")
        winning = set(map(int, winning.split()))
        mine = set(map(int, mine.split()))
        matches = winning.intersection(mine)
        if matches:
            total += 2 ** (len(matches) - 1)
    
    print(total)


if __name__ == "__main__":
    main()