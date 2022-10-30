n = int(input(": "))
for i in range(n ** 2):
    line = ((i % n) * ' ') + (n * '* ')
    print(line)

n = int(input(": "))
for i in range(n ** 2):

    for k in range(i % n):
        print(" ", end="")

    for j in range(n):
        print("* ", end="")

    print("")
