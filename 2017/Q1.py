from random import randint


def solve(s):
    if len(s) == 1:
        return s
    while True:
        new_row = ""

        for i in range(1, len(s)):
            new_row += (s[i] if s[i] == s[i - 1] else ("R" if { s[i], s[i - 1] } == { "B", "G" } else ("B" if { s[i], s[i - 1] } == { "G", "R" } else "G")))
            
        if len(new_row) == 1:  # the solution is when there is only one in the row
            return new_row[0]
        
        s = new_row


def d_helper():
    opts = ["R", "G", "B"]
    length = 6
    while True:
        inv = 5
        for _ in range(5):  # repeats make it more credible, I can also run it multiple times
            test = [opts[randint(0, 2)] for _ in range(length)]
            sol = solve(test)
            # copied from solve

            if sol == (test[0] if test[0] == test[-1] else ("R" if { test[0], test[-1] } == { "B", "G" } else ("B" if { test[0], test[-1] } == { "G", "R" } else "G"))):
                inv -= 1
        if inv == 0:
            return length

        length += 1


if __name__ == '__main__':
    # A
    print(solve(input()))                          # MARKS: 23/23
    # B (can be done with pen and paper very easily) # ANS: 3 solutions -> RRRBBGGRG, BGBRBGRGR, GBGGRRBBB MARKS: 3/3
    # C                                              # ANS: ? MARKS: 0/4
    # D                                              # ANS: 10 MARKS: 3/3
    # print(d_helper()
