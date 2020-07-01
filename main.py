z = 0
a = ["1", "2", "3", "4", "5", "6", "7", "8", "9"]


def replace(d, e, f):
    a.remove(d)
    a.insert(int(e) - 1, f)


def board():
    print(a[0], a[1], a[2])
    print(a[3], a[4], a[5])
    print(a[6], a[7], a[8])


while 1 < 2:
    h = "X"
    board()
    g = input(">>>")
    replace(g, g, h)
    if a[0] == h and a[1] == h and a[2] == h:
        break
    elif a[3] == h and a[4] == h and a[5] == h:
        break
    elif a[6] == h and a[7] == h and a[8] == h:
        break
    elif a[0] == h and a[3] == h and a[6] == h:
        break
    elif a[1] == h and a[4] == h and a[7] == h:
        break
    elif a[2] == h and a[5] == h and a[8] == h:
        break
    elif a[0] == h and a[4] == h and a[8] == h:
        break
    elif a[2] == h and a[4] == h and a[6] == h:
        break
    h = "O"
    board()
    g = input(">>>")
    replace(g, g, h)
    if a[0] == h and a[1] == h and a[2] == h:
        break
    elif a[3] == h and a[4] == h and a[5] == h:
        break
    elif a[6] == h and a[7] == h and a[8] == h:
        break
    elif a[0] == h and a[3] == h and a[6] == h:
        break
    elif a[1] == h and a[4] == h and a[7] == h:
        break
    elif a[2] == h and a[5] == h and a[8] == h:
        break
    elif a[0] == h and a[4] == h and a[8] == h:
        break
    elif a[2] == h and a[4] == h and a[6] == h:
        break
print("WIN!")
print("Ending board:")
board()
