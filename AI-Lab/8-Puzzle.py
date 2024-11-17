import heapq

class Puzzle:
    def __init__(self, board, parent=None, move=0, cost=0):
        self.board = board  # Current board configuration
        self.parent = parent  # Parent state
        self.move = move  # Moves taken to reach this state
        self.cost = cost  # Cost = moves + heuristic

    def __lt__(self, other):
        return self.cost < other.cost  # For priority queue comparison

    def find_empty(self):
        for i in range(3):
            for j in range(3):
                if self.board[i][j] == 0:
                    return i, j

    def generate_neighbors(self):
        x, y = self.find_empty()
        neighbors = []
        moves = [(0, 1), (1, 0), (0, -1), (-1, 0)]  # Right, Down, Left, Up
        for dx, dy in moves:
            nx, ny = x + dx, y + dy
            if 0 <= nx < 3 and 0 <= ny < 3:
                new_board = [row[:] for row in self.board]
                new_board[x][y], new_board[nx][ny] = new_board[nx][ny], new_board[x][y]
                neighbors.append(Puzzle(new_board, self))
        return neighbors


def heuristic(board, goal):
    # Manhattan distance heuristic
    distance = 0
    for i in range(3):
        for j in range(3):
            value = board[i][j]
            if value != 0:
                target_x, target_y = divmod(value - 1, 3)
                distance += abs(i - target_x) + abs(j - target_y)
    return distance


def solve_8_puzzle(start, goal):
    open_list = []
    closed_set = set()
    start_puzzle = Puzzle(start, cost=heuristic(start, goal))
    heapq.heappush(open_list, start_puzzle)

    while open_list:
        current = heapq.heappop(open_list)

        if current.board == goal:
            solution = []
            while current:
                solution.append(current.board)
                current = current.parent
            return solution[::-1]

        closed_set.add(tuple(tuple(row) for row in current.board))

        for neighbor in current.generate_neighbors():
            if tuple(tuple(row) for row in neighbor.board) in closed_set:
                continue

            neighbor.move = current.move + 1
            neighbor.cost = neighbor.move + heuristic(neighbor.board, goal)
            heapq.heappush(open_list, neighbor)

    return None


def print_board(board):
    for row in board:
        print(" ".join(str(x) if x != 0 else "." for x in row))
    print()


# Example usage
start = [
    [1, 2, 3],
    [4, 0, 6],
    [7, 5, 8]
]

goal = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 0]
]

solution = solve_8_puzzle(start, goal)

if solution:
    print("Solution found!")
    for step, state in enumerate(solution):
        print(f"Step {step}:")
        print_board(state)
else:
    print("No solution exists.")
