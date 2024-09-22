# pattern_drawing.py

# Prompt the user for the size of the pattern
size = int(input("Enter the size of the pattern: "))

# Initialize the row counter
row = 0

# Outer loop (while loop) for the rows
while row < size:
    # Inner loop (for loop) for printing asterisks in each row
    for _ in range(size):
        print("*", end="")  # Print asterisks without moving to the next line
    print()  # Print a newline after each row
    row += 1
