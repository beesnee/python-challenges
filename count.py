start = int(input("Enter a number to start counting from: "))
end = int(input("enter a number to end counting from: "))
count_by = int(input("Enter a number to count in: "))


for x in range(start, end, count_by):
    print(x)