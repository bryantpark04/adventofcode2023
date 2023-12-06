def main() -> None:
    with open("input.txt") as f:
        lines = f.read().splitlines()

    time = int("".join(lines[0].split()[1:]))
    distance = int("".join(lines[1].split()[1:]))

    total = 0
    for hold_time in range(1, time):
        if hold_time * (time - hold_time) > distance:
            total += 1
    
    print(total)


if __name__ == "__main__":
    main()