start = (1, 2, 3,
         4, 0, 6,
         7, 5, 8)

goal = (1, 2, 3,
        4, 5, 6,
        7, 8, 0)

def get_moves(state):
    moves = []
    i = state.index(0)
    for j in [i-3, i+3, i-1, i+1]:
        if 0 <= j < 9:
            if abs(i-j) != 1 or i//3 == j//3:
                new_state = list(state)
                new_state[i], new_state[j] = new_state[j], new_state[i]
                moves.append(tuple(new_state))
    return moves

# Depth First Search
def dfs(state, visited):
    if state == goal:
        return [state]
    visited.add(state)
    for next_state in get_moves(state):
        if next_state not in visited:
            path = dfs(next_state, visited)
            if path:
                return [state] + path
    return None

# Iterative Deepening Search
def dls(state, limit, path):
    if state == goal:
        return [state]
    if limit == 0:
        return None
    path.add(state)
    for next_state in get_moves(state):
        if next_state not in path:
            result = dls(next_state, limit-1, path)
            if result:
                return [state] + result
    path.remove(state)
    return None

def ids():
    depth = 0
    while True:
        result = dls(start, depth, set())
        if result:
            return result
        depth += 1

def display(solution):
    if solution is None:
        print("No solution found")
        return
    for state in solution:
        for i in range(0, 9, 3):
            print(state[i:i+3])
        print()

print("DFS Solution:")
display(dfs(start, set()))
print("IDS Solution:")
display(ids())