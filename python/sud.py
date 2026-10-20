def find_empty_cell(grid):
    
    for r in range(9):
        for c in range(9):
            if grid[r][c] == 0:
                return (r, c)
    return None

def is_valid(grid, num, pos):
    
    row, col = pos
    
    for c in range(9):
        if grid[row][c] == num and col != c:
            return False
    
    for r in range(9):
        if grid[r][col] == num and row != r:
            return False
    
    box_start_row = (row // 3) * 3
    box_start_col = (col // 3) * 3
    for r in range(box_start_row, box_start_row + 3):
        for c in range(box_start_col, box_start_col + 3):
            if grid[r][c] == num and (r, c) != pos:
                return False

    return True

def solve_sudoku(grid):
    
    find = find_empty_cell(grid)

    if not find:
        return True
    else:
        row, col = find

    for num in range(1, 10):
        if is_valid(grid, num, (row, col)):
            grid[row][col] = num

            if solve_sudoku(grid):
                return True
            
            
            grid[row][col] = 0

    return False


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

if solve_sudoku(puzzle):
    print("Solved Puzzle:")
    
    for row in puzzle:
        print(" ".join(map(str, row)))
else:
    print("This puzzle cannot be solved.")