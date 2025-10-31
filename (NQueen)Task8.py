'''def print_board(b):
    for row in b: print(" ".join(str(c) for c in row))
    print()

def safe(b, r, c, N):
    return all(b[r][i]==0 for i in range(c)) and \
           all(b[r-i][c-i]==0 for i in range(1,min(r,c)+1)) and \
           all(b[r+i][c-i]==0 for i in range(1,min(N-r,c)+1))

def solve(b, c, N):
    if c==N: print_board(b); return True
    res = False
    for r in range(N):
        if safe(b,r,c,N):
            b[r][c]=1
            res = solve(b,c+1,N) or res
            b[r][c]=0
    return res

N=4
board=[[0]*N for _ in range(N)]
solve(board,0,N)
'''
def print_board(b):
    for r in b: print(" ".join(str(c) for c in r))
    print()

def safe(b, r, c, N):
    # Check left side
    for i in range(c):
        if b[r][i]: return False
    # Check upper-left diagonal
    i, j = r, c
    while i >= 0 and j >= 0:
        if b[i][j]: return False
        i -= 1; j -= 1
    # Check lower-left diagonal
    i, j = r, c
    while i < N and j >= 0:
        if b[i][j]: return False
        i += 1; j -= 1
    return True

def solve(b, c, N):
    if c == N:
        print_board(b)
        return True
    res = False
    for r in range(N):
        if safe(b, r, c, N):
            b[r][c] = 1
            res = solve(b, c + 1, N) or res
            b[r][c] = 0
    return res

N = 4
board = [[0]*N for _ in range(N)]
solve(board, 0, N)
