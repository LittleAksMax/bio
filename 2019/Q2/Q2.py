
def turn(orientation, direction):
    if direction == 'L':
        orientation += 90
    elif direction == 'R':
        orientation -= 90
    return abs(orientation % 360)


def solve(t, i, m):
    instruction = 0
    orientation = 90
    moves = [(0, 0)]

    for _ in range(m):
        # change direction if needed
        if i[instruction] in ['L', 'R']:
            orientation = turn(orientation, i[instruction])
        
        # move forward
        invalid = True
        invalids = 1
        while invalid:
            # checked all directions
            if invalids == 4:
                print(moves[0])
                return "STUCK"

            move = None
            if orientation == 0:     # right
                move = (moves[0][0] + 1, moves[0][1])

            elif orientation == 90:  # up
                move = (moves[0][0], moves[0][1] + 1)
            elif orientation == 180: # left
                move = (moves[0][0] - 1, moves[0][1])
            else:                    # down
                move = (moves[0][0], moves[0][1] - 1)
            
            if move not in moves:
                moves.insert(0, move)
                invalid = False
            else:
                invalids += 1
                orientation = turn(orientation, 'R')

        # get next instruction prepared
        instruction += 1
        instruction %= len(i)

        # increment count and remove trail if needed
        if t != 1:
            t -= 1
        else:
            moves.pop()
    print(moves[0])
    return "NOT STUCK"


def c_get_row_col_from_coord(coord):
    if coord[0] not in range(-10, 11):
        return None, None
    if coord[1] not in range(-10, 11):
        return None, None
    return coord[0] + 10, coord[1] + 10

def c_check_if_full(visited):
    for row in visited:
        for col in row:
            if not col:
                return False
    return True

def c_helper(t, i, m):
    visited = [[False for x in range(21)] for y in range(21)] # -10 <= x <= 10, -10 <= y <= 10
    visited[10][10] = True  # change starting point to True
    instruction = 0
    orientation = 90
    moves = [(0, 0)]
    count = 0

    for _ in range(m):
        # change direction if needed
        if i[instruction] in ['L', 'R']:
            orientation = turn(orientation, i[instruction])
        
        # move forward
        invalid = True
        invalids = 1
        while invalid:
            # checked all directions
            if invalids == 4:
                print(moves[0])
                return

            move = None
            if orientation == 0:     # right
                move = (moves[0][0] + 1, moves[0][1])

            elif orientation == 90:  # up
                move = (moves[0][0], moves[0][1] + 1)
            elif orientation == 180: # left
                move = (moves[0][0] - 1, moves[0][1])
            else:                    # down
                move = (moves[0][0], moves[0][1] - 1)
            
            if move not in moves:
                moves.insert(0, move)
                invalid = False
            else:
                invalids += 1
                orientation = turn(orientation, 'R')

        # get next instruction prepared
        instruction += 1
        instruction %= len(i)

        # increment count and remove trail if needed
        if t > 1:
            t -= 1
        else:
            moves.pop()
        row, col = c_get_row_col_from_coord(moves[0])
        if row is None or col is None:
            continue
        visited[row][col] = True
        count += 1
        if count < 100:
            continue
        if c_check_if_full(visited):
            break
    print(count)


def d_helper():
    t = 1010
    while t != 0:
        if solve(t, "LLRFFF", 10000) != "NOT STUCK":
            return t
        t -= 1

if __name__ == "__main__":
    data = input().split()
    solve(int(data[0]), data[1], int(data[2]))       # MARKS: 18/24
    # c_helper(int(data[0]), data[1], int(data[2]))  # ANS: 440 CORRECT ANS: 440
    # print(d_helper())                              # ANS: 937 CORRECT ANS: 1007

# MARKS 23/34