line = int(input("Enter number of lines: "))

# Upper side
for i in range(1, line+1):
    for j in range(0, line-i):
        print("*", end="")
    print("")

# Lower side
for i in range(1, line+1):
    for j in range(line-1, line-i, -1):
        print("*", end="")
    print("")
