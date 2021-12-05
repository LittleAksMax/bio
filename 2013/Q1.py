from time import gmtime, strftime


def solve(f1, f2):
    a = -1
    b = 0

    while a != b:
        if a == -1: a = 0

        a = (60 + a + f1) % 1440 # 1440 = 60 * 24
        b = (60 + b + f2) % 1440
    return a


def b_helper():
    sol = []
    for bfast in range(20):
        a = -1
        b = 0

        while a != b:
            if a == -1: a = 0

            a = (60 + a) % 1440 # 1440 = 60 * 24
            b = (60 + b + bfast) % 1440
        sol.append((a, bfast))
    sol = filter(lambda x: x[0] != 0, sol)
    for s, bfast in sol:
        print(strftime("%H:%M", gmtime(60 * s)), bfast)


def c_helper():
    sol = []
    for f1 in range(60):
        for f2 in range(60):
            # copied from solve()
            a = -1
            b = 0
            hours = 0

            while a != b:
                if a == -1: a = 0

                a = (60 + a + f1) % 1440 # 1440 = 60 * 24
                b = (60 + b + f2) % 1440
                hours += 1
            sol.append((f1, f2, hours))
    print(max(sol, key=lambda x: x[2]))


if __name__ == '__main__':
    # A MARKS: 25/25
    for _ in range(10):
        print(strftime("%H:%M", gmtime(60 * solve(*list(map(int, input().split()))))))
    # B
    # b_helper() MARKS: 3/3
    # 01:00 0 mins fast
    # 12:00 8 mins fast
    # 16:00 9 mins fast
    # 18:00 16 mins fast
    # 08:00 18 mins fast
    # C
    # c_helper() MARKS: 4/4
    # 0, 1, with 1440 hours, meeting at 00:00
