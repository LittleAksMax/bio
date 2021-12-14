from itertools import permutations
from pprint import pprint
from functools import lru_cache

def add(window, warehouse):
    return window + warehouse[0]


def swap(window):
    return window[1] + window[0] + window[2:]


def rotate(window):
    return window[1:] + window[0]

@lru_cache(maxsize=None)
def solve(end):
    q = [("", 0)]
    seen = set()
    while len(q) > 0:
        cur, steps = q.pop(0)
        wh = [c for c in [chr(i + ord('A')) for i in range(len(end))] if c not in cur]
        if cur in seen:
            continue
        seen.add(cur)
        if cur == end:
            return steps
        if len(wh) != 0:  # is warehouse empty?
            q.append((add(cur, wh), steps + 1)) # Add
        if len(cur) == 2:  # swap and rotate have same effect, no reason to add both
            q.append((swap(cur), steps + 1))
        if len(cur) > 2:  # are there at least 2 boxes on display
            q.append((swap(cur), steps + 1))
            q.append((rotate(cur), steps + 1))
        
    return -1


def b_helper():
    count = []
    for perm in permutations("ABCDE"):
        if solve("".join(perm)) == 6:
            count.append(perm)
    pprint(count)


def c_helper():
    # copied solve() with some extra stuff
    end = "HGFEDCBA"
    q = [("", 0)]
    seen = set()
    count = 0

    while len(q) > 0:
        cur, steps = q.pop(0)
        wh = [c for c in [chr(i + ord('A')) for i in range(len(end))] if c not in cur]
        if cur in seen:
            continue
        # seen.add(cur)
        if cur == end and steps != 24:
            count += 1
            print(count)
        if len(wh) != 0:  # is warehouse empty?
            q.append((add(cur, wh), steps + 1)) # Add
        if len(cur) == 2:  # swap and rotate have same effect, no reason to add both
            q.append((swap(cur), steps + 1))
        if len(cur) > 2:  # are there at least 2 boxes on display
            q.append((swap(cur), steps + 1))
            q.append((rotate(cur), steps + 1))
        
    print(count)

if __name__ == '__main__':
    # A MARKS: 24/24
    print(solve(input()))
    # B
    # b_helper()  # ANS: BACDE BCADE BCDAE BCDEA MARKS: 3/3
    # C # ANS: ? MARKS: /