import bisect
import sys


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
    
    for seed in seeds:
        for i, stage in enumerate(maps):
            for selected in range(len(stage)):
                translate_base, base, range_length = stage[selected]
                print(f"{i=} {seed}->", end="")
                if seed >= base and seed - base < range_length:
                    seed = seed - base + translate_base
                    break
                print(f"{seed}")
        print(f"{seed=}")
        res = min(res, seed)

    print(res)


if __name__ == "__main__":
    main()