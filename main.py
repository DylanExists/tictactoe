z = 0
a = ["1", "2", "3", "4", "5", "6", "7", "8", "9"]


def replace(d, e, f):
    a.remove(d)
    a.insert(int(e) - 1, f)


def board():
    print(a[0], a[1], a[2])
    print(a[3], a[4], a[5])
    print(a[6], a[7], a[8])


while z == 0:
    h = "X"
    board()
    g = input(">>>")
    replace(g, g, h)
    if a[0] and a[3] and a[6] or a[1] and a[4] and a[7] or a[2] and a[5] and a[8] == "X" or "O":
        z = 1
    elif a[0] and a[1] and a[2] or a[3] and a[4] and a[5] or a[6] and a[7] and a[8] == "X" or "O":
        z = 1
    elif a[0] and a[4] and a[7] or a[2] and a[4] and a[6] == "X" or "O":
        z = 1
    h = "O"
    board()
    g = input(">>>")
    replace(g, g, h)
    if a[0] and a[3] and a[6] or a[1] and a[4] and a[7] or a[2] and a[5] and a[8] == "X" or "O":
        z = 1
    elif a[0] and a[1] and a[2] or a[3] and a[4] and a[5] or a[6] and a[7] and a[8] == "X" or "O":
        z = 1
    elif a[0] and a[4] and a[7] or a[2] and a[4] and a[6] == "X" or "O":
        z = 1
print("WIN!")
print("Ending board:")
board()
