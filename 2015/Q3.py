from itertools import permutations

def solve(a, b, c, d, n):
    s = a * "A" + b * "B" + c * "C" + d * "D"
    perms = sorted(["".join(i) for i in list(set(permutations(s)))])
    print(perms[n - 1])


def b_helper():
    # copied solve()
    s = 2 * "A" + 2 * "B" + 2 * "C" + 2 * "D"
    perms = sorted(["".join(i) for i in list(set(permutations(s)))])
    for idx, perm in enumerate(perms):
        if perm == "AABCCBDD":
            print(idx + 1)
            return

if __name__ == '__main__':
    # A
    solve(*[int(i) for i in input().split()])  # MARKS: 11/25
    # B
    # b_helper()  # ANS: 10th arrangement MARKS: 2/2
    # C
    # ANS: ? MARKS: 0/5
