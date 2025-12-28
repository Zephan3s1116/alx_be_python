size = int(input("Enter the size of the pattern: "))
row = 0

while row < size:
    for _ in range(size):
        print("*", end="")
    print()  # This moves to the next line after finishing a row
    row += 1