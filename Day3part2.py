path = r"C:\Users\frank\OneDrive\Desktop\stuff\AdventofCode\input3.txt"
arr = []

with open(path, 'r') as file:
    for line in file:
        arr.append(line.strip())
file.close()

neighbors = [
        (-1, 0), (1, 0),  # Up, Down
        (0, -1), (0, 1),  # Left, Right
        (-1, -1), (-1, 1), (1, -1), (1, 1)  # Diagonals
    ]

def is_valid_number(grid, row, col, special_characters):

    # Check adjacency for special characters
    for dr, dc in neighbors:
        new_row, new_col = row + dr, col + dc

        # Check if the new position is within the grid
        if 0 <= new_row < len(grid) and 0 <= new_col < len(grid[0]):
            neighbor_value = grid[new_row][new_col]

            # Check if the neighbor is a special character
            if neighbor_value in special_characters:
                return True  # Valid number found

    return False  # No adjacent special character found

def is_gear(grid,spc):
    return 

special_characters = ['#', '@', '$', '%', '&', '*', '-', '+', '=', '/']
result = is_gear(arr, special_characters)
print(sum(result))