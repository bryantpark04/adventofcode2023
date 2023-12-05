import sys
import bisect


def main() -> None:
    with open("input.txt") as f:
        lines = f.read()
    
    seeds, *maps_data = lines.split("\n\n")

    seeds = list(map(int, seeds.split(": ")[1].split()))

    maps = []
    for map_data in maps_data:
        map_data = map_data.split(":\n")[1]
        map_lines = map_data.splitlines()
        maps.append(list(sorted((tuple(map(int, line.split())) for line in map_lines), key=lambda t: (t[1], t[0], t[2]))))

    res = sys.maxsize
    
    it = iter(seeds)
    i = 0
    for seed_base in it:
        print(i, len(seeds) // 2)
        seed_range_length = next(it)
        for seed in range(seed_base, seed_base + seed_range_length):
            for stage in maps:
                ip = bisect.bisect_right(stage, seed, key=lambda t: t[1])
                selected = ip - 1
                translate_base, base, range_length = stage[selected]
                if seed >= base and seed - base < range_length:
                    seed = seed - base + translate_base
            res = min(res, seed)
        i += 1

    print(res)


if __name__ == "__main__":
    main()