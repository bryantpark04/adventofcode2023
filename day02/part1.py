def main() -> None:
    with open("input.txt") as f:
        lines = f.read().splitlines()
    
    total = 0
    max_colors = {"red": 12, "green": 13, "blue": 14}
    
    for i, line in enumerate(lines):
        id = i + 1
        _, moves = line.split(": ")
        moves = moves.split("; ")
        is_valid = True
        for move in moves:
            show = move.split(", ")
            for part in show:
                n, color = part.split(" ")
                n = int(n)
                thresh = max_colors[color]
                if n > thresh:
                    is_valid = False
                    break
            if not is_valid:
                break
        if is_valid:
            print(f"{id} valid")
            total += id
    
    print(total)


if __name__ == "__main__":
    main()