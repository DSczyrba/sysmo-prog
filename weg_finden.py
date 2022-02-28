from pprint import pprint
import sys
import markt_generieren

sys.setrecursionlimit(1000)


def get_visitable(x, y):
    if matrix_is_regal[y][x]:
        return []
    targets = []
    for dx, dy in ((0, 1), (0, -1), (1, 0), (-1, 0)):
        nx = x + dx
        ny  = y + dy
        if nx < 0 or ny < 0:
            continue
        if nx >= DIM_X or ny >= DIM_Y:
            continue
        targets.append((nx, ny))
    return targets


def find_path(target, known_paths=(((0, 0),),)):
    print(len(known_paths))
    if not known_paths:
        return None
    for path in sorted(known_paths, key=len):
        if path[-1] == target:
            return path
    # breadth-first
    new_paths = []
    seen_nodes = set(node for path in known_paths for node in path)
    for path in known_paths:
        # if path[-1] in path[:-1]:
        #     # this path loops
        #     continue
        for visitable in get_visitable(*path[-1]):
            if visitable in seen_nodes:
                continue
            seen_nodes.add(visitable)
            new_paths.append(list(path) + [visitable])
    return find_path(target, new_paths)




for i in range(4, 30):
    MAP_INPUT = markt_generieren.markt_erzeugen(i, i, 20)
    print(MAP_INPUT)
    matrix_is_regal = [[char == "x" for char in line] for line in MAP_INPUT.split("\n")]
    DIM_Y = len(matrix_is_regal)
    DIM_X = len(matrix_is_regal[0])
    print("total dimensions:", DIM_X, DIM_Y)

    regal_nodes = []
    gang_nodes = []
    for y, line in enumerate(matrix_is_regal):
        for x, is_regal in enumerate(line):
            if is_regal:
                regal_nodes.append((x, y))
            else:
                gang_nodes.append((x, y))

    result = find_path((DIM_X - 1, DIM_Y - 1))
    if result is None:
        i = i - 1
    else:
        print(result)

