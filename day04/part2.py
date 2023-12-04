from collections import Counter


def main() -> None:
    with open("input.txt") as f:
        lines = f.read().splitlines()

    q = list(range(len(lines)))
    i = 0

    memo = {}

    while i < len(q):
        if q[i] in memo:
            n_matches = memo[q[i]]
        else:
            line = lines[q[i]]
            _, line = line.split(": ")
            winning, mine = line.split(" | ")
            winning = set(map(int, winning.split()))
            mine = set(map(int, mine.split()))
            matches = winning.intersection(mine)
            n_matches = len(matches)
            memo[q[i]] = n_matches
        for j in range(q[i] + 1, min(q[i] + 1 + n_matches, len(lines))):
            # print(f"adding {j + 1}")
            q.append(j)
        i += 1

    ct = Counter(q)

    print({k + 1:ct[k] for k in sorted(ct)})
    
    print(len(q))


if __name__ == "__main__":
    main()