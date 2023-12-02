def main() -> None:
    with open("input.txt") as f:
        lines = f.read().splitlines()
    
    total = 0
    max_colors = {"red": 12, "green": 13, "blue": 14}
    
    for i, line in enumerate(lines):
        _, moves = line.split(": ")
        moves = moves.split("; ")
        is_valid = True
        for move in moves:
            show = move.split(", ")
            for part in show:
                n, color = part.split(" ")
                n = int(n)
                is_valid = is_valid and n <= max_colors[color]
        if is_valid:
            total += i + 1
    
    print(total)


if __name__ == "__main__":
    main()