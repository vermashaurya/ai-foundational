from collections import deque

# Define the initial and goal states
initial_state = (3, 3, 'L')  # (num_missionaries_left, num_cannibals_left, boat_position)
goal_state = (0, 0, 'R')

# Function to check if a state is valid
def is_valid(state):
    num_missionaries_left, num_cannibals_left, boat_position = state

    # Check if the number of cannibals is greater than the number of missionaries on either side
    if num_missionaries_left > 0 and num_cannibals_left > num_missionaries_left:
        return False

    num_missionaries_right = 3 - num_missionaries_left
    num_cannibals_right = 3 - num_cannibals_left

    if num_missionaries_right > 0 and num_cannibals_right > num_missionaries_right:
        return False

    return True

# Function to generate all possible valid moves from a given state
def generate_moves(state):
    moves = []
    num_missionaries_left, num_cannibals_left, boat_position = state

    if boat_position == 'L':
        for i in range(3):
            for j in range(3):
                # Move one or two missionaries from left to right
                if i + j > 0 and i + j <= 2 and num_missionaries_left - i >= 0 and num_missionaries_left - i <= 3:
                    new_state = (num_missionaries_left - i, num_cannibals_left - j, 'R')
                    if is_valid(new_state):
                        moves.append((new_state, f"{i} missionaries and {j} cannibals cross left"))

                # Move one or two cannibals from left to right
                if i + j > 0 and i + j <= 2 and num_cannibals_left - i >= 0 and num_cannibals_left - i <= 3:
                    new_state = (num_missionaries_left - j, num_cannibals_left - i, 'R')
                    if is_valid(new_state):
                        moves.append((new_state, f"{j} missionaries and {i} cannibals cross left"))
    else:
        for i in range(3):
            for j in range(3):
                # Move one or two missionaries from right to left
                if i + j > 0 and i + j <= 2 and num_missionaries_left + i >= 0 and num_missionaries_left + i <= 3:
                    new_state = (num_missionaries_left + i, num_cannibals_left + j, 'L')
                    if is_valid(new_state):
                        moves.append((new_state, f"{i} missionaries and {j} cannibals come back"))

                # Move one or two cannibals from right to left
                if i + j > 0 and i + j <= 2 and num_cannibals_left + i >= 0 and num_cannibals_left + i <= 3:
                    new_state = (num_missionaries_left + j, num_cannibals_left + i, 'L')
                    if is_valid(new_state):
                        moves.append((new_state, f"{j} missionaries and {i} cannibals come back"))

    return moves

# Function to solve the problem using breadth-first search
def solve():
    visited = set()
    queue = deque([(initial_state, [])])

    while queue:
        state, path = queue.popleft()

        if state == goal_state:
            return path

        if state not in visited:
            visited.add(state)
            moves = generate_moves(state)
            for move, phrase in moves:
                queue.append((move, path + [phrase]))

    return None

# Print the initial state
print("Initial state:")
print(f"Missionaries: {initial_state[0]}, Cannibals: {initial_state[1]}")
print(f"Boat position: {initial_state[2]}")
print()

# Solve the problem
solution = solve()

# Print the solution
if solution is None:
    print("No solution found.")
else:
    print("Solution:")
    for phrase in solution:
        print(phrase)

# Print the final state and counts
print()
print("Final state:")
print(f"Missionaries: {goal_state[0]}, Cannibals: {goal_state[1]}")
print(f"Boat position: {goal_state[2]}")
