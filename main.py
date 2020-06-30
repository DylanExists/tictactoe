z = 0
a = ["1", "2", "3", "4", "5", "6", "7", "8", "9"]


def replacea(d, e, f):
    a.remove(int(d))
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
        bad = 42 / 0
    if a[0, 1, 2] or a[3, 4, 5] or a[6, 7, 8] == "X" or "O":
        z = 1
    elif a[0, 3, 6] or a[1, 4, 7] or a[2, 5, 8] == "X" or "O":
        z = 1
    elif a[0, 5, 8] or a[3, 5, 6] == "X" or "O":
        z = 1
    h = "O"
    board()
    g = input(">>>")
    replacea(g, g, h)
    if a[0, 1, 2] or a[3, 4, 5] or a[6, 7, 8] == "X" or "O":
        z = 1
    elif a[0, 3, 6] or a[1, 4, 7] or a[2, 5, 8] == "X" or "O":
        z = 1
    elif a[0, 5, 8] or a[3, 5, 6] == "X" or "O":
        z = 1
print("Someone won! You know who.")
print("Ending board:")
board()
