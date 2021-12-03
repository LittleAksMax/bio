
def brute_force(n):
    while True:
        n += 1
        if str(n) == str(n)[::-1]:
            return n


def solve(n):
    if n < 10000000:
        print(brute_force(n))
    
    sn = str(n)
    flag = 0
    if sn == sn[::-1]:  # check if input is palindrome
        flag = 1
    if len(set(sn)) == 1 and sn[0] == '9':
        return "1" + ((len(sn) - 1) * "0") + "1"
    if len(sn) % 2 == 0:
        # split into first half and second half of number
        fhalf = int(sn[:len(sn) // 2])
        shalf = int(sn[len(sn) // 2:])
        if flag:
            fhalf += 1  # increase the size of first half so it doesn't send back the the input
        if str(fhalf)[::-1] > str(shalf):
            return str(fhalf) + str(fhalf)[::-1]
        fhalf += 1 if not flag else 0
        return str(fhalf) + str(fhalf)[::-1]
    else:
        fhalf = int(sn[:len(sn) // 2])
        shalf = int(sn[len(sn) // 2 + 1:])
        mid = int(sn[len(sn) // 2])
        if flag:
            fhalf += 1
            mid += 1
            mid %= 10
        if str(fhalf)[::-1] > str(shalf):
            return str(fhalf) + str(mid) + str(fhalf)[::-1]
        fhalf += 1 if flag else 0
        mid += 1 if flag else 0
        mid %= 10
        return str(fhalf) + str(mid) + str(fhalf)[::-1]

if __name__ == "__main__":
    print(solve(int(input())))