def main() -> None:
    with open("input.txt") as f:
        lines = f.read().splitlines()
    
    total = 0
    for line in lines:
        for ch in line:
            if ch.isdigit():
                total += int(ch) * 10
                break
        for ch in line[::-1]:
            if ch.isdigit():
                total += int(ch)
                break
    print(total)


if __name__ == "__main__":
    main()