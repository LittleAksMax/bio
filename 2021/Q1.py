from itertools import permutations

def valid(s1, s2):
    # print(s1, s2)
    least = 100
    for c in s1:
        if ord(c) < least:
            least = ord(c)
    for c in s2:
        if ord(c) >= least:
            return False
    return True


def is_pat(s):
    if len(s) == 1:
        # print(s, True)
        return True
    if len(s) == 2 and ord(s[0]) > ord(s[1]):
        # print(s, True)
        return True
    for i in range(1, len(s)):
        if valid(s[:i], s[i:]):
            if is_pat(s[:i][::-1]) and is_pat(s[i:][::-1]):
                # print(s, True)
                return True
    # print(s, False)
    return False


def solve(s1, s2):
    print("YES" if is_pat(s1) else "NO")
    print("YES" if is_pat(s2) else "NO")
    print("YES" if is_pat(s1 + s2) else "NO")


def b_helper():
    for perm in permutations("ABCD"):
        if perm[0] == "A":
            continue
        perm = "".join(perm)
        if is_pat(perm):
            print(perm)

if __name__ == '__main__':
    # A
    for i in range(10):solve(*input().split())  # MARKS: 24/24
    # B ANS: BDCA CBDA CDAB DACB DBAC MARKS: 3/3
    # b_helper()
    # C ANS: ? MARKS: 0/5
