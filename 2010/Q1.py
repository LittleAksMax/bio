from itertools import permutations


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
    freq = [0 for i in range(10)]
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


def c_helper(n):
    # get all permutations of 123456 but they have to start with 4
    # because if it is higher it multiplied by 2 it is larger than 999999
    perms_ = list(permutations(n))
    perms = []
    i = 0
    while i < len(perms_):
        if perms_[i][0] == '5' or perms_[i][0] == '6':
            perms_.pop(i)
            i += 1
            continue
        perms.append("".join(perms_[i]))
        i += 1
    count = 0
    print(len(perms))
    freq = [0, 1, 1, 1, 1, 1, 1, 0, 0, 0]
    for perm in perms:
        flag = 0
        for i in range(2, 10):
            if flag == 1:
                continue
            if check_anagram(freq, str(int(perm) * i)):
                flag = 1
                count += 1
                continue
    return count


if __name__ == '__main__':
    # print(solve(input()))
    # print(b_helper("85247910"))
    print(c_helper("123456"))
