def rule_to_binary(rule, width):
    """Convert a rule number to a binary string of given width, padded with zeros."""
    return format(rule, f'0{width}b')

def next_state(state, rule_bin):
    """Calculate the next state of a cell based on its current state and the states of its neighbors."""
    left_neighbor = (state[0] + 2 * state[1] + 4 * state[2]) % 8
    return int(rule_bin[left_neighbor])

def simulate_automaton(size, rule, iterations):
    """Simulate the cellular automaton."""
    # Initialize the state with all dead cells except the central one
    state = [0] * size
    if size % 2 == 0:
        state[size // 2] = 1
    else:
        state[size // 2 - 1] = 1

    rule_bin = rule_to_binary(rule, 8)

    print("CELLULAR AUTOMATON SIMULATION")
    print(f"Rule {rule}")

    for _ in range(iterations):
        next_state_list = [0] * size
        for i in range(size):
            # Determine the states of the current cell and its neighbors
            left_neighbor = (i - 1 + size) % size
            right_neighbor = (i + 1) % size
            next_state_list[i] = next_state([state[left_neighbor], state[i], state[right_neighbor]], rule_bin)
        
        # Update the current state to the next state
        state = next_state_list

        # Visualize the current state
        print(''.join('o' if cell else '.' for cell in state))

# Ask the user for input
try:
    size = int(input("Enter the size of the automaton (number of cells): "))
    if size <= 0:
        raise ValueError("Size must be a positive integer.")

    rule = int(input("Enter the rule number: "))
    if rule < 0 or rule >= 2**8:
        raise ValueError("Rule number must be between 0 and 255.")

    iterations = int(input("Enter the number of iterations: "))
    if iterations < 0:
        raise ValueError("Number of iterations must be a non-negative integer.")

    # Run the simulation
    simulate_automaton(size, rule, iterations)

except ValueError as e:
    print(f"Invalid input: {e}")
except KeyboardInterrupt:
    print("Simulation interrupted by user.")