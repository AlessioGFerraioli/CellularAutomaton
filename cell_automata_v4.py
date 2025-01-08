def rule_to_binary(rule, width):
    """Convert a rule number to a binary string of given width, padded with zeros."""
    return format(rule, f'0{width}b')

def next_state(neighbor, rule_bin):
    """Calculate the next state of a cell based on its current state and the states of its neighbors."""
    #print("Inside next_state")

    index_ = (neighbor[2] + 2 * neighbor[1] + 4 * neighbor[0]) % 8
    print("index_", index_)
    print("rule_bin", rule_bin)
    print("rule_bin[-index_]", rule_bin[-index_])
    #print("left_neighborALT", left_neighborALT)
    #print("rule_bin[left_neighborALT]", rule_bin[left_neighborALT])
    return int(rule_bin[-index_])

def simulate_automaton(size, rule, iterations):
    """Simulate the cellular automaton."""
    # Initialize the state with all dead cells except the central one
    state = [0] * size
    state[size // 2] = 1
    
    rule_bin = rule_to_binary(rule, 8)

    print("CELLULAR AUTOMATON SIMULATION")
    print(f"Rule {rule}")

    for _ in range(iterations):
        #print("Iteration", _)
        next_state_list = [0] * size
      #  print("next_state_list", next_state_list)

        for i in range(size):
            print("i", i)

            print(f"State {state}")
            # Determine the states of the current cell and its neighbors
            left_neighbor = (i - 1 + size) % size
         #   print("left_neighbor", left_neighbor)
            right_neighbor = (i + 1) % size
          #  print("right_neighbor", right_neighbor)
            neighbor = [state[left_neighbor], state[i], state[right_neighbor]]
            print("neighbor", neighbor)
            next_state_list[i] = next_state(neighbor, rule_bin)
           # print("next_state_list", next_state_list)
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