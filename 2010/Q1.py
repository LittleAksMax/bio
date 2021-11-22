
def check_anagram(n_freq, x):
    freq = [0 for i in range(10)]
    for c in x:
        freq[int(c)] += 1
    return freq == n_freq


def solve(n):
    freq = [0 for i in range(10)]
    res = []
    for c in n:
        freq[int(c)] += 1
    for i in range(2, 10):
        if check_anagram(freq, str(int(n) * i)):
            res.append(i)
    if len(res) == 0:
        return "NO"
    else:
        s = ""
        for a in res:
            s += str(a) + " "
        return s


def b_helper(n):
    freq = [0 for _ in range(10)]
    res = []
    for c in n:
        freq[int(c)] += 1
    for i in range(2, 10):
        if int(n) % i != 0:
            continue
        if check_anagram(freq, str(int(n) // i)):
            res.append(i)
    if len(res) == 0:
        return "NO"
    else:
        s = ""
        for a in res:
            s += str(int(n) // a) + " "
        return s


def c_helper():
    count = 0
    for num in range(100000, 1000000):
        if len(set(str(num))) != 6:
            continue
        if solve(str(num)) != "NO":
            count += 1
    return count


if __name__ == '__main__':
    print(solve(input()))         # 25/25
    # print(b_helper("85247910"))   # 2/2
    # print(c_helper())             # 3/3
