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
    if a[0] and b[0] and c[0] or a[1] and b[1] and c[1] or a[2] and b[2] and c[2] == "X" or "O":
        z = 1
    elif a[0] and a[1] and a[2] or b[0] and b[1] and b[2] or c[0] and c[1] and c[2] == "X" or "O":
        z = 1
    elif a[0] and b[1] and c[2] or a[2] and b[1] and c[0] == "X" or "O":
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
    if a[0] and b[0] and c[0] or a[1] and b[1] and c[1] or a[2] and b[2] and c[2] == "X" or "O":
        z = 1
    elif a[0] and a[1] and a[2] or b[0] and b[1] and b[2] or c[0] and c[1] and c[2] == "X" or "O":
        z = 1
    elif a[0] and b[1] and c[2] or a[2] and b[1] and c[0] == "X" or "O":
        z = 1
print("Someone won! You know who.")
print("Ending board:")
board()
