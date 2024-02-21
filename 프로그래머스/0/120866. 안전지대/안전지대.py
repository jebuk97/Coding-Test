def check(c, n):
    return 0<=c[0]<n and 0<=c[1]<n

def solution(board):
    n = len(board[0])
    dyx = [(-1, -1), (-1, 0), (-1, 1),
          (0, -1),         (0, 1),
          (1, -1), (1, 0), (1, 1)]
    for i in range(n):
        for j in range(n):
            if board[i][j] == 1:
                for yx in dyx:
                    ny, nx = yx
                    ny, nx = (i + ny, j + nx)
                    if check((ny, nx), n) and board[ny][nx] == 0:
                        board[ny][nx] = -1
    for b in board:
        print(b)
    answer = 0
    for i in range(n):
        for j in range(n):
            if board[i][j] == 0:
                answer += 1
        
    return answer