def main() -> None:
    with open("input.txt") as f:
        lines = f.read().splitlines()
    
    total = 0
    digits = ["one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]
    digits_map = {digits[i]: i + 1 for i in range(len(digits))}
    digits_map_reversed = {"".join(reversed(key)): val for key, val in digits_map.items()}
    for line in lines:
        for i in range(len(line)):
            ch = line[i]
            if ch.isdigit():
                total += int(ch) * 10
                break
            flag = False
            for digit_word in digits_map:
                if line[i:].startswith(digit_word):
                    flag = True
                    total += digits_map[digit_word] * 10
                    break
            if flag: 
                break
        line = line[::-1]
        for i in range(len(line)):
            ch = line[i]
            if ch.isdigit():
                total += int(ch)
                break
            flag = False
            for digit_word in digits_map_reversed:
                if line[i:].startswith(digit_word):
                    flag = True
                    total += digits_map_reversed[digit_word]
                    break
            if flag: 
                break
    print(total)


if __name__ == "__main__":
    main()