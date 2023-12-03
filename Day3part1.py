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

# parts and non parts
# loop and check all 8 directions
# x and y range caps at 140

path2 = r"C:\Users\frank\OneDrive\Desktop\stuff\AdventofCode\sample.txt"
arr2 = []

with open(path2, 'r') as file:
    for line in file:
        arr2.append(line.strip())
file.close()

flag = False

def is_valid_number(grid, row, col, special_characters):

    # Check adjacency for special characters
    for dr, dc in neighbors:
        new_row, new_col = row + dr, col + dc

        # Check if the new position is within the grid
        if 0 <= new_row < len(grid) and 0 <= new_col < len(grid[0]):
            neighbor_value = grid[new_row][new_col]

            # Check if the neighbor is a special character
            if neighbor_value in special_characters:
                global flag
                flag = True
                return True  # Valid number found

    return False  # No adjacent special character found

def find_valid_numbers(grid, special_characters):
    global flag
    valid_numbers = []
    num = ""
    # Iterate through the grid
    max_x = len(grid)
    max_y = len(grid[0])
    for row in range(len(grid)):
        for col in range(len(grid[0])):

            cell_value = grid[row][col]
            # Check if the cell contains a number
            if cell_value.isdigit():
                # Build
                num = num + cell_value
                # Check if the number is adjacent to a special character
                is_valid_number(grid, row, col, special_characters)
                if row <= max_x-1 and col+1 <= max_y-1:
                    if not flag and not grid[row][col+1].isdigit():
                        num = ""

                    if flag and not grid[row][col+1].isdigit():
                        valid_numbers.append(int(num))
                        flag = False
                        num = ""
    
    return valid_numbers

special_characters = ['#', '@', '$', '%', '&', '*', '-', '+', '=', '/']
result = find_valid_numbers(arr2, special_characters)
print(sum(result))


#i missed an edge case these 3 numbers were it so i just did it by hand
# 867318 -> 867 318
# 635334 -> 635
# 1453 -> 453

# 2028976 - 867318 = 1161658
# 1161658 + 867 = 1162525

# 1162525 - 635334 = 527191
# 527191 + 635 = 527826

# 527826 - 1453 = 526373
# 526373 + 453 = 526826 + 318

# 527144
