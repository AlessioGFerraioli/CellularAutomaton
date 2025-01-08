def get_cell_state(grid, row, rule):
    """Determina il nuovo stato di una cella in base alla regola."""
    neighbors = "".join([str(grid[row - 1][col]) for col in range(row - 1, row + 2)])
    rule_in_binary = format(rule, '08b')  # Rappresenta la regola come stringa binaria a 8 bit
    return rule_in_binary[neighbors.index('1')]  # Trova l'indice '1' nei vicini e restituisce il bit corrispondente nella regola

def simulate_cellular_automaton(size, rule, iterations):
    """Simula l'evoluzione dell'automa cellulare."""
    grid = [[0 for _ in range(size)] for _ in range(iterations + 1)]  # Initializza la griglia con tutti stati morti
    grid[0][size // 2] = 1  # Imposta la cella centrale (o quella a destra della metà se size è pari) come viva inizialmente

    for row in range(1, iterations + 1):  # Evoluzione per ogni iterazione
        for col in range(size):
            if col == 0 or col == size - 1:
                grid[row][col] = grid[row - 1][col]  # Le cellule agli estremi rimangono uguali
            else:
                grid[row][col] = int(get_cell_state(grid, row - 1, rule))  # Calcola il nuovo stato

    # Generazione e visualizzazione del risultato
    print("CELLULAR AUTOMATON SIMULATION")
    print(f"Rule used: Rule {rule}")
    
    for row in range(iterations + 1):
        visualization = "".join(['o' if grid[row][col] else '.' for col in range(size)])
        print(visualization)

# Richiesta degli input all'utente
size = int(input("Enter the size of the cellular automaton (number of cells): "))
rule = int(input("Enter the rule number to be used: "))
iterations = int(input("Enter the number of iterations for the simulation: "))

# Simulazione e visualizzazione
simulate_cellular_automaton(size, rule, iterations)