
def solve(n):
    prev = None
    numbers = [2 * i + 1 for i in range(n)]
    flag = False
    for i in range(1, len(numbers)):
        cur = numbers[i]
        if cur == -1: # -1 represents numbers removed
            continue
        if cur > n:
            break
        elif cur == n:
            flag = True
        if not flag:
            prev = cur
        seen = 1
        for i in range(len(numbers)): # go through and remove every `cur`th number
            old = numbers[i]
            if seen % cur == 0:
                numbers[i] = -1
            if old != -1:
                seen += 1
    print(prev, cur)

def b_helper():
    # just copied solve() but removed unnecessary code
    count = 0
    
    numbers = [2 * i + 1 for i in range(60)] # in reality only need 50
    for i in range(1, len(numbers)):
        cur = numbers[i]
        if cur == -1: # -1 represents numbers removed
            continue
        if cur < 100:
            count += 1 # increment how many lucky numbers there are  
        else:
            break # break if checked all numbers less than 100
        for i in range(len(numbers)): # go through and remove every `cur`th number
            if (i + 1) % cur == 0:
                numbers[i] = -1
    print(count + 1)  # + 1 so 1 is also included


if __name__ == '__main__':
    for i in range(10):
        solve(int(input()))   # MARKS: 25/25
    # b_helper()            # ANS: 23 MARKS: 2/2
    # C                     # ANS: ? MARKS: 0
    