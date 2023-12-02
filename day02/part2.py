def main() -> None:
    with open("input.txt") as f:
        lines = f.read().splitlines()
    
    total = 0
    
    for _, line in enumerate(lines):
        max_colors = {"red": 0, "green": 0, "blue": 0}
        _, moves = line.split(": ")
        moves = moves.split("; ")
        for move in moves:
            show = move.split(", ")
            for part in show:
                n, color = part.split(" ")
                n = int(n)
                max_colors[color] = max(max_colors[color], n)
        total += max_colors["red"] * max_colors["green"] * max_colors["blue"]
    
    print(total)


if __name__ == "__main__":
    main()