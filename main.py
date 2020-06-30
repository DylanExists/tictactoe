z = 0
a = ["1", "2", "3", "4", "5", "6", "7", "8", "9"]


def replacea(d, e, f):
    a.remove(d)
    a.insert(e, f)


def board():
    print(a[0], a[1], a[2])
    print(a[3], a[4], a[5])
    print(a[6], a[7], a[8])


while z == 0:
    h = "X"
    board()
    g = input(">>>")
    if g == "1" or g == "2" or g == "3" and a[g] != "X" or "O":
        replacea(g, g, h)
    elif g == "4" or g == "5" or g == "6" and a[g] != "X" or "O":
        replaceb(g, g, h)
    elif g == "7" or g == "8" or g == "9" and a[g] != "X" or "O":
        replacec(g, g, h)
    else:
        print("you did a bad")
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
    if g == "1" or g == "2" or g == "3" and a[g] != "X" or "O":
        replacea(g, g, h)
    elif g == "4" or g == "5" or g == "6" and a[g] != "X" or "O":
        replaceb(g, g, h)
    elif g == "7" or g == "8" or g == "9" and a[g] != "X" or "O":
        replacec(g, g, h)
    else:
        print("you did a bad")
        bad = 42 / 0
    if a[0, 1, 2] or a[3, 4, 5] or a[6, 7, 8] == "X" or "O":
        z = 1
    elif a[0, 3, 6] or a[1, 4, 7] or a[2, 5, 8] == "X" or "O":
        z = 1
    elif a[0, 5, 8] or a[3, 5, 6] == "X" or "O":
        z = 1
print("Someone won! You know who.")
print("Ending board:")
board()
