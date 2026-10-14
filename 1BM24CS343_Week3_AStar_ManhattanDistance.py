
# 8-Puzzle using A* - Manhattan Distance
start = (1, 2, 3, 4, 0, 6, 7, 5, 8)
goal = (1, 2, 3, 4, 5, 6, 7, 8, 0)

def heuristic(state):
    distance = 0
    for i in range(9):
        tile = state[i]
        if tile != 0:
            j = goal.index(tile)
            distance += abs(i//3 - j//3) + abs(i%3 - j%3)
    return distance

def moves(state):
    result = []
    i = state.index(0)
    for j in [i-3, i+3, i-1, i+1]:
        if 0 <= j < 9 and (abs(i-j) != 1 or i//3 == j//3):
            s = list(state)
            s[i], s[j] = s[j], s[i]
            result.append(tuple(s))
    return result

def astar():
    open_list = [(heuristic(start), 0, start, [start])]
    visited = set()
    while open_list:
        open_list.sort(key=lambda x: x[0])
        f, g, state, path = open_list.pop(0)
        if state == goal:
            return path
        if state in visited:
            continue
        visited.add(state)
        for next_state in moves(state):
            if next_state not in visited:
                new_g = g + 1
                new_f = new_g + heuristic(next_state)
                open_list.append((new_f, new_g, next_state,
                                  path + [next_state]))
    return None
path = astar()
if path:
    for state in path:
        print(state[:3])
        print(state[3:6])
        print(state[6:])
        print()
else:
    print("No solution found")