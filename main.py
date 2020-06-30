z = 0
a = ["1", "2", "3", "4", "5", "6", "7", "8", "9"]


def replacea(d, e, f):
    a.remove(d)
    a.insert(int(e), f)


def board():
    print(a[0], a[1], a[2])
    print(a[3], a[4], a[5])
    print(a[6], a[7], a[8])


while z == 0:
    h = "X"
    board()
    g = input(">>>")
    replacea(g, g, h)
    i = 0
    while i < 5:
        if a[i] and a[i + 1] and a[i + 2] == "X" or "O":
            z = 1
            break
        i += 3
    i = 0
    while i < 2:
        if a[i] and a[i + 3] and a[i + 6] == "X" or "O":
            z = 1
            break
        i += 1
    if a[0] and a[4] and a[7] or a[2] and a[4] and a[6] == "X" or "O":
        z = 1
    h = "O"
    board()
    g = input(">>>")
    replacea(g, g, h)
    i = 0
    while i < 5:
        if a[i] and a[i + 1] and a[i + 2] == "X" or "O":
            z = 1
            break
        i += 3
    i = 0
    while i < 2:
        if a[i] and a[i + 3] and a[i + 6] == "X" or "O":
            z = 1
            break
        i += 1
    if a[0] and a[4] and a[7] or a[2] and a[4] and a[6] == "X" or "O":
        z = 1
print("Someone won! You know who.")
print("Ending board:")
board()
