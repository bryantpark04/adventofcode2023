def main() -> None:
    with open("input.txt") as f:
        lines = f.read().splitlines()

    digits = {str(i): i for i in range(1, 10)}
    numbers = ["one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]
    digits_map = {numbers[i]: i + 1 for i in range(len(numbers))}
    digits_map.update(digits)
    digits_map_reversed = {"".join(reversed(key)): val for key, val in digits_map.items()}
    
    total = 0

    for line in lines:
        for line, mult, d_map in [(line, 10, digits_map), (line[::-1], 1, digits_map_reversed)]:
            for i in range(len(line)):
                flag = False
                for digit_word in d_map:
                    if line[i:].startswith(digit_word):
                        flag = True
                        total += d_map[digit_word] * mult
                        break
                if flag: 
                    break

    print(total)


if __name__ == "__main__":
    main()