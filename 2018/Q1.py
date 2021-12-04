from math import ceil

def solve(i, r):
    # d = 100
    # i /= 100
    # r /= 100
    # paid = 0

    # while d > 0:
    #     interest = ceil(d * i * 100) / 100
    #     d += interest
    #     payment = max([50, ceil(d * r * 100) / 100])
    #     d -= payment
    #     paid += payment
    # return paid + d 
    # the above score 22/26, because of floating point errors
    amount = 10000
    total_repaid = 0

    interest, repay = i, r

    while amount > 0:
        interest_month = ceil((interest / 100) * amount)
        amount += interest_month
        repaid = ceil((repay / 100) * amount)
        repaid = min(max(5000, repaid), amount)
        total_repaid += repaid
        amount -= repaid
    return total_repaid / 100


def b_helper():
    # literally copied solve()
    amount = 10000
    total_repaid = 0

    interest, repay = 43, 46
    count = 0

    while amount > 0:
        interest_month = ceil((interest / 100) * amount)
        amount += interest_month
        repaid = ceil((repay / 100) * amount)
        repaid = min(max(5000, repaid), amount)
        total_repaid += repaid
        amount -= repaid
        count += 1
    print(count)


def c_helper():
    best = 0
    best_interest = 0
    best_repay = 0

    for interest in range(100):
        for repay in range(100):

            amount = 10000
            total_repaid = 0

            while amount > 0:
                interest_month = ceil((interest / 100) * amount)
                amount += interest_month
                repaid = ceil((repay / 100) * amount)
                repaid = min(max(5000, repaid), amount)
                total_repaid += repaid
                amount -= repaid

                if amount >= 10000:  # impossible to repay
                    break

            if amount == 0:
                if total_repaid > best:
                    best = total_repaid
                    best_interest = interest
                    best_repay = repay
    print(best_interest, best_repay)

if __name__ == '__main__':
    # A
    print(round(solve(*[int(i) for i in input().split(" ")]), 2))  # MARKS: 26/26
    # B
    # b_helper()                                                     # ANS: 5 MARKS: 2/2
    # C                                                              # ANS: interest = 96, repayment = 49 MARKS: 3/3
    # c_helper()