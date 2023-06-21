def water_jug_problem(jug1_capacity, jug2_capacity, target_amount):
    # Initialize the jugs with 0 water
    jug1 = 0
    jug2 = 0

    # Keep track of visited states to avoid infinite loops
    visited = set()

    # Perform Breadth-First Search (BFS) using a queue
    queue = [((jug1, jug2), [])]  # Store the current state and the steps taken

    while queue:
        current_state, steps = queue.pop(0)

        jug1 = current_state[0]
        jug2 = current_state[1]

        # If target amount is achieved, return the steps
        if jug1 == target_amount or jug2 == target_amount:
            steps.append(current_state)
            return steps

        # Generate all possible next states and add them to the queue
        next_states = []

        # Fill jug1
        next_states.append(((jug1_capacity, jug2), steps + [(jug1, jug2, "Fill Jug 1")]))

        # Fill jug2
        next_states.append(((jug1, jug2_capacity), steps + [(jug1, jug2, "Fill Jug 2")]))

        # Empty jug1
        next_states.append(((0, jug2), steps + [(jug1, jug2, "Empty Jug 1")]))

        # Empty jug2
        next_states.append(((jug1, 0), steps + [(jug1, jug2, "Empty Jug 2")]))

        # Pour jug1 to jug2 until jug2 is full or jug1 is empty
        amount_poured = min(jug1, jug2_capacity - jug2)
        next_states.append(((jug1 - amount_poured, jug2 + amount_poured), steps + [(jug1, jug2, "Pour Jug 1 to Jug 2")]))

        # Pour jug2 to jug1 until jug1 is full or jug2 is empty
        amount_poured = min(jug2, jug1_capacity - jug1)
        next_states.append(((jug1 + amount_poured, jug2 - amount_poured), steps + [(jug1, jug2, "Pour Jug 2 to Jug 1")]))

        for state in next_states:
            if state[0] not in visited:
                queue.append(state)
                visited.add(state[0])

    # If no solution is found
    return "No solution found."

#print("\nYou could test this out using")
#print("Jug1 Capacity = 3")
#print("Jug2 capacity = 4")
#print("Desired output = 1\n")
#print("Anyway")

# Get user input for jug capacities and target amount
jug1_capacity = int(input("Enter the capacity of Jug 1: "))
jug2_capacity = int(input("Enter the capacity of Jug 2: "))
target_amount = int(input("Enter the target amount: "))

# Solve the water jug problem
solution = water_jug_problem(jug1_capacity, jug2_capacity, target_amount)

# Print the solution
if solution == "No solution found.":
    print(solution)
else:
    print("Steps to measure", target_amount, "liters:")
    for step in solution:
        print(step)

