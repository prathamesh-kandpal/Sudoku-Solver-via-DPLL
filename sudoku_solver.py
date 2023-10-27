def parse_input(file_name):
    try:
        with open(file_name, 'r') as file:
            lines = file.readlines()
            sudoku_board = []
            for line in lines:
                row = [int(num) for num in line.split()]
                sudoku_board.append(row)
            return sudoku_board
    except FileNotFoundError:
        print(f"File '{file_name}' not found.")
        return None

def sudoku_constraints(board):
    # Create CNF clauses to represent the Sudoku puzzle
    clauses = []
    n = 9  # Sudoku grid size

    # Helper function to convert Sudoku coordinates to literal numbers
    def literal(row, col, num):
        return (row * 81) + (col * 9) + (num - 1) + 1

    # Ensure that each cell contains a number from 1 to 9
    for row in range(n):
        for col in range(n):
            cell_value = board[row][col]
            if cell_value != 0:
                clauses.append([literal(row, col, cell_value)])

    # Ensure each row contains distinct numbers
    for row in range(n):
        for num in range(1, n + 1):
            clause = [literal(row, col, num) for col in range(n)]
            clauses.append(clause)

    # Ensure each column contains distinct numbers
    for col in range(n):
        for num in range(1, n + 1):
            clause = [literal(row, col, num) for row in range(n)]
            clauses.append(clause)

    # Ensure each 3x3 subgrid contains distinct numbers
    for row_block in range(3):
        for col_block in range(3):
            for num in range(1, n + 1):
                clause = [literal(row_block * 3 + r, col_block * 3 + c, num)
                          for r in range(3) for c in range(3)]
                clauses.append(clause)

    return clauses

def dpll(clauses, assignments=[]):
    # DPLL algorithm to solve CNF clauses
    if all(len(clause) == 0 for clause in clauses):
        return []  # All clauses are satisfied

    if any(len(clause) == 0 for clause in clauses):
        return None  # Backtrack, this branch is not valid

    # Unit propagation: Find and assign unit clauses
    unit_clauses = [clause[0] for clause in clauses if len(clause) == 1]
    new_clauses = [clause for clause in clauses if len(clause) != 1]

    # Recursive solving
    for literal in unit_clauses:
        new_assignments = assignments + [literal]
        result = dpll([[l for l in clause if l != -literal] for clause in new_clauses], new_assignments)
        if result is not None:
            return result

    # If no unit clauses left, try pure literal elimination
    literals = [literal for clause in new_clauses for literal in clause]
    pure_literals = [literal for literal in literals if -literal not in literals]
    if pure_literals:
        literal = pure_literals[0]
        new_assignments = assignments + [literal]
        return dpll([[l for l in clause if l != -literal] for clause in new_clauses], new_assignments)

    # If no pure literals, make an arbitrary choice
    literal = new_clauses[0][0]
    new_assignments = assignments + [literal]
    result = dpll([[l for l in clause if l != -literal] for clause in new_clauses], new_assignments)
    if result is not None:
        return result

    # If no choice leads to a solution, backtrack
    return None

def convert_back(assignments):
    # Convert DPLL assignments back to a Sudoku board
    n = 9  # Sudoku grid size
    board = [[0] * n for _ in range(n)]

    for assignment in assignments:
        if assignment > 0:
            row = (assignment - 1) // (n * n)
            col = ((assignment - 1) // n) % n
            num = (assignment - 1) % n + 1
            board[row][col] = num

    return board

def main():
    file_name = "sudoku_input.txt"
    board = parse_input(file_name)

    if board:
        print("Sudoku puzzle from file:")
        for row in board:
            print(" ".join(map(str, row)))

        clauses = sudoku_constraints(board)
        assignments = dpll(clauses)
        if assignments:
            solution = convert_back(assignments)
            print("\nSolved Sudoku:")
            for row in solution:
                print(" ".join(map(str, row)))
        else:
            print("\nNo solution exists.")

if __name__ == "__main__":
    main()
