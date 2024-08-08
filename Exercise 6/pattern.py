row_count = int(input("Enter the number of rows: "))
x = 1

while row_count > 0:
    for i in range(row_count):
        print(x, end = " ")
    row_count = row_count-1
    x = x + 1
    print()
