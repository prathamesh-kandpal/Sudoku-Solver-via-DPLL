# Sudoku-Solver-via-DPLL

This Python program is a Sudoku solver that uses the DPLL (Davis-Putnam-Logemann-Loveland) algorithm for solving Sudoku puzzles. It takes a Sudoku puzzle as input, solves it, and provides the solved puzzle as output.

## Table of Contents

1. Prerequisites
2. Usage
3. Input Format
4. Running the Program
5. Sample Input and Output
6. Implementation Details
7. License

## 1. Prerequisites

- Python 3.x (This code is written in Python 3)
- A text file containing a Sudoku puzzle (e.g., `sudoku_input.txt`)

## 2. Usage

The program is modularized into functions for readability and ease of understanding. The main steps are as follows:

1. Parse the Sudoku puzzle from an input file.
2. Generate CNF (Conjunctive Normal Form) clauses to represent the Sudoku puzzle.
3. Use the DPLL algorithm to solve the CNF clauses.
4. Convert the DPLL assignments back into a Sudoku solution.
5. Display the solved Sudoku puzzle.

## 3. Input Format

The Sudoku puzzle should be stored in a text file. Each line of the text file represents a row of the Sudoku puzzle, with numbers separated by spaces. Use '0' to represent empty cells.

Here is an example of the input format:

```
5 3 0 0 7 0 0 0 0
6 0 0 1 9 5 0 0 0
0 9 8 0 0 0 0 6 0
8 0 0 0 6 0 0 0 3
4 0 0 8 0 3 0 0 1
7 0 0 0 2 0 0 0 6
0 6 0 0 0 0 2 8 0
0 0 0 4 1 9 0 0 5
0 0 0 0 8 0 0 7 9
```

## 4. Running the Program

1. Save your Sudoku puzzle in a text file (e.g., `sudoku_input.txt`) using the specified input format.
2. Run the program with the following command:

   ```
   python sudoku_solver.py
   ```

3. The program will read the input from the file, solve the puzzle, and display the solved Sudoku puzzle or inform you if no solution exists.

## 5. Sample Input and Output

### Sample Input (`sudoku_input.txt`):

```
5 3 0 0 7 0 0 0 0
6 0 0 1 9 5 0 0 0
0 9 8 0 0 0 0 6 0
8 0 0 0 6 0 0 0 3
4 0 0 8 0 3 0 0 1
7 0 0 0 2 0 0 0 6
0 6 0 0 0 0 2 8 0
0 0 0 4 1 9 0 0 5
0 0 0 0 8 0 0 7 9
```

### Sample Output (Solved Sudoku):

```
5 3 4 6 7 8 9 1 2
6 7 2 1 9 5 3 4 8
1 9 8 3 4 2 5 6 7
8 5 9 7 6 1 4 2 3
4 2 6 8 5 3 7 9 1
7 1 3 9 2 4 8 5 6
9 6 1 5 3 7 2 8 4
2 8 7 4 1 9 6 3 5
3 4 5 2 8 6 1 7 9
```

## 6. Implementation Details

- The program uses the DPLL algorithm to solve Sudoku puzzles, which is a popular SAT solver.
- It represents the Sudoku puzzle as CNF clauses.
- The `dpll` function is responsible for solving the CNF clauses, while the `convert_back` function converts the assignments back to a Sudoku solution.
- The code is modularized to make it easier to understand and maintain.

## 7. License

This program is provided under the MIT License. You are free to use, modify, and distribute it according to the terms of the license.

---

This README file provides an overview of the Sudoku solver program, its usage, and sample input/output. You can save it as a separate text file for reference.
