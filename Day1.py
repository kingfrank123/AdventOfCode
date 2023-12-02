# replace path with your local path
path = r"C:\\Users\\frank\\OneDrive\Desktop\stuff\AdventofCode\\input.txt"
# just a smaller sample txt for edge cases
path2 = r"C:\Users\frank\OneDrive\Desktop\stuff\AdventofCode\sample.txt"

arr = []
arr2 = []

with open(path, 'r') as file:
    for line in file:
        arr.append(line.strip())
file.close()

with open(path2, 'r') as file:
    for line in file:
        arr2.append(line.strip())
file.close()

word_number_mapping = { 'one': 1, 'two': 2,'three': 3,'four': 4,'five': 5,'six': 6,'seven': 7,'eight': 8,'nine': 9 }

# checks if string contains an integer
def contains_integer(input_str):
    return any(char.isdigit() for char in input_str)

def find_firsts(line):
    first_left = None
    first_right = None

    for char in line:
        if char.isdigit():
            first_left = char
            break

    for char in reversed(line):
        if char.isdigit():
            first_right = char
            break

    return int(first_left + first_right)

def add_numbers_to_words(arr):
    myarr = []
    for line in arr:
        for word, number in word_number_mapping.items():
            line = line.replace(word, word[0] + str(number) + word)

        myarr.append(line)

    return myarr

def d1p1():
    sum = 0
    for line in arr:
        #if contains_integer(line):
        sum += find_firsts(line)
    return sum

def d1p2():
    res = 0
    replaced = add_numbers_to_words(arr)
    for line in replaced:
        res += find_firsts(line)
    return res

print("answer1:" + str(d1p1()) , "answer2:" + str(d1p2())) 

# run d1p1() or d1p2() for the answer