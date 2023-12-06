def main() -> None:
    with open("input.txt") as f:
        lines = f.read().splitlines()

    times = lines[0].split()[1:]
    distances = lines[1].split()[1:]

    times = list(map(int, times))
    distances = list(map(int, distances))

    product = 1

    for time, distance in zip(times, distances):
        total = 0
        for hold_time in range(1, time):
            if hold_time * (time - hold_time) > distance:
                total += 1
        print(total)
        product *= total
    
    print(product)


if __name__ == "__main__":
    main()