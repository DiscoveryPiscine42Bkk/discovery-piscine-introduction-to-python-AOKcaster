def checkmate(board):
    board = board.strip().split('\n')
    size = len(board)

    # find king position
    king_pos = None
    for row in range(size):
        for col in range(size):
            if board[row][col] == 'K':
                king_pos = (row,col)
                break
        if king_pos:
            break
    if not king_pos:
        print("Fail")
        return
    
    k_row, k_col = king_pos
    
    #check if that position inside board or not
    def in_bounds(r, c):
        return 0 <= r < size and 0 <= c < size
    
    #check pawn(P) move
    for dx, dy in [(1, -1), (1, 1)]:
        x, y = k_row + dx, k_col + dy
        if in_bounds(x, y) and board[x][y] == 'P':
            print("Success")
            return

    # Check Bishops(B) move and Queens(Q) only x move
    for dx, dy in [(-1, -1), (-1, 1), (1, -1), (1, 1)]:
        x, y = k_row + dx, k_col + dy
        while in_bounds(x, y):
            if board[x][y] != '.':
                if board[x][y] in ['B', 'Q']:
                    print("Success")
                    return
                break
            x += dx
            y += dy

    # Check Rooks(R) move and Queens(Q) only x move
    for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
        x, y = k_row + dx, k_col + dy
        while in_bounds(x, y):
            if board[x][y] != '.':
                if board[x][y] in ['R', 'Q']:
                    print("Success")
                    return
                break
            x += dx
            y += dy

    print("Fail")