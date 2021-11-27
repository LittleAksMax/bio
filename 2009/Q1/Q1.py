
def solve(word):
    letters = [
        "ONE",
        "TWO",
        "THREE",
        "FOUR",
        "FIVE",
        "SIX",
        "SEVEN",
        "EIGHT",
        "NINE",
    ]
    for num in letters:
        i = 0
        for c in word:
            if i == len(num):
                continue
            if c == num[i]:
                i += 1
        if i == len(num):
            print(letters.index(num) + 1)
            return
    print("NO")

if __name__ == "__main__":
    solve(input())  # 24/24
    # b             # ANS: 10 2/2
    # c             # ANS: ?  0/4