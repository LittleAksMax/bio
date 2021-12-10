
def iterate(inst, left, right):

    l, m = left
    r, s = right

    o = (l + r, m + s)

    if inst != "":
        if inst[0] == "L":
            o = iterate(inst[1:], o, right)
        else:
            o = iterate(inst[1:], left, o)
    return o


def solve(inst):
    numerator, denominator = iterate(inst, (1, 0), (0, 1))
    print(f"{numerator} / {denominator}")


def b_helper():
    numerator, denominator = iterate("", iterate("LRL", (1, 0), (0, 1)), iterate("LLLL", (1, 0), (0, 1)))
    print(f"{numerator} / {denominator}")


if __name__ == "__main__":
    # A
    solve(input())
    # B
    # b_helper() # ANS: 4 / 10 MARKS: 23/23
    # C
    # ANS: 0 Rs and 999999 Ls MARKS: 3/3
    # D
    # ANS: No, as the starting point (when no L or R moves have been made) is 1 / 1, and both the denominator and numerator
    # can only being increased with every instruction, and since you need a negative numerator or denominator to represent
    # a negative promenade, you can't have a negative promenade MARKS: 3/3
