'''Implement a program to find the LCM of two numbers



'''"""
# Take input from the user
num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))

# Choose the greater number
if num1 > num2:
    greater = num1
else:
    greater = num2

while True:
    if (greater % num1 == 0) and (greater % num2 == 0):
        lcm = greater
        break
    greater += 1

print("The LCM of", num1, "and", num2, "is", lcm)
""""""
# Take input for the first matrix
print("Enter elements of the first matrix:")
rows1 = int(input("Enter the number of rows: "))
cols1 = int(input("Enter the number of columns: "))

matrix1 = []
for i in range(rows1):
    row = []
    for j in range(cols1):
        row.append(float(input(f"Enter element [{i+1},{j+1}]: ")))
    matrix1.append(row)

# Take input for the second matrix
print("\nEnter elements of the second matrix:")
rows2 = int(input("Enter the number of rows: "))
cols2 = int(input("Enter the number of columns: "))

matrix2 = []
for i in range(rows2):
    row = []
    for j in range(cols2):
        row.append(float(input(f"Enter element [{i+1},{j+1}]: ")))
    matrix2.append(row)

# Check if matrices can be multiplied
if cols1 != rows2:
    print("\nMatrices cannot be multiplied!")
else:
    # Initialize the result matrix with zeros
    result = [[0 for _ in range(cols2)] for _ in range(rows1)]

    # Perform matrix multiplication
    for i in range(rows1):
        for j in range(cols2):
            for k in range(cols1):
                result[i][j] += matrix1[i][k] * matrix2[k][j]

    # Display the result
    print("\nThe result of matrix multiplication is:")
    for row in result:
        print(row)
"""