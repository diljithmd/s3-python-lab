def find_empty_cell(grid):
    """
    Finds the next empty cell in the Sudoku grid (represented by 0).
    Returns a tuple (row, col) or None if no empty cells are left.
    """
    for r in range(9):
        for c in range(9):
            if grid[r][c] == 0:
                return (r, c)
    return None

def is_valid(grid, num, pos):
    """
    Checks if placing a number at a given position is valid according to
    Sudoku rules (row, column, and 3x3 box).
    """
    row, col = pos
    
    # Check row
    for c in range(9):
        if grid[row][c] == num and col != c:
            return False
            
    # Check column
    for r in range(9):
        if grid[r][col] == num and row != r:
            return False
            
    # Check 3x3 box
    box_start_row = (row // 3) * 3
    box_start_col = (col // 3) * 3
    
    for r in range(box_start_row, box_start_row + 3):
        for c in range(box_start_col, box_start_col + 3):
            if grid[r][c] == num and (r, c) != pos:
                return False

    return True

def solve_sudoku(grid):
    """
    Solves the Sudoku puzzle using a recursive backtracking (trial and error) algorithm.
    """
    find = find_empty_cell(grid)

    # Base case: If no empty cells are found, the puzzle is solved
    if not find:
        return True
    else:
        row, col = find

    # The core "Trial and Error" loop
    for num in range(1, 10):
        if is_valid(grid, num, (row, col)):
            # 1. ***TRY (Trial)***: Place the number
            grid[row][col] = num

            # 2. Check if the rest of the puzzle can be solved
            if solve_sudoku(grid):
                return True
            
            # 3. ***ERROR (Backtrack)***: If not solved, reset and try the next number
            grid[row][col] = 0

    # If no number from 1-9 works, return False to trigger the backtrack in the previous call
    return False

# -------------------------------------------------------------
## Main Program Execution
# -------------------------------------------------------------

puzzle = [
    [5, 3, 0, 0, 7, 0, 0, 0, 0],
    [6, 0, 0, 1, 9, 5, 0, 0, 0],
    [0, 9, 8, 0, 0, 0, 0, 6, 0],
    [8, 0, 0, 0, 6, 0, 0, 0, 3],
    [4, 0, 0, 8, 0, 3, 0, 0, 1],
    [7, 0, 0, 0, 2, 0, 0, 0, 6],
    [0, 6, 0, 0, 0, 0, 2, 8, 0],
    [0, 0, 0, 4, 1, 9, 0, 0, 5],
    [0, 0, 0, 0, 8, 0, 0, 7, 9]
]

print("Solving Puzzle...")
if solve_sudoku(puzzle):
    print("\nSolved Puzzle:")
    # Print the solved grid
    for row in puzzle:
        # Adds visual separation between the 3x3 boxes for better readability
        print(" ".join(map(str, row)))
else:
    print("\nThis puzzle cannot be solved.")