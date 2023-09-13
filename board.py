class chess_board:
    def __init__(self):
        # 9 * 10 board
        self.board = [
        ["bC", "bM", "bX", "bS", "bW", "bS", "bX", "bM", "bC"],
        ["--", "--", "--", "--", "--", "--", "--", "--", "--"],
        ["--", "bP", "--", "--", "--", "--", "--", "bP", "--"],
        ["bZ", "--", "bZ", "--", "bZ", "--", "bZ", "--", "bZ"],
        ["--", "--", "--", "--", "--", "--", "--", "--", "--"],
        ["--", "--", "--", "--", "--", "--", "--", "--", "--"],
        ["rZ", "--", "rZ", "--", "rZ", "--", "rZ", "--", "rZ"],
        ["--", "rP", "--", "--", "--", "--", "--", "rP", "--"],
        ["--", "--", "--", "--", "--", "--", "--", "--", "--"],
        ["rC", "rM", "rX", "rS", "rW", "rS", "rX", "rM", "rC"]]
        self.white_to_move = True
        self.movelog = []


    def make_move(self, move):
        # change pos of the piece in board var
        self.board[move.s_row][move.s_col] = "--"
        self.board[move.e_row][move.e_col] = move.piece_moved
        self.white_to_move = not self.white_to_move
        # update movelog
        self.movelog.append(move)
class move:
    def __init__(self, s_pos, e_pos, b):
        self.s_row = s_pos[0]
        self.s_col = s_pos[1]
        self.e_row = e_pos[0]
        self.e_col = e_pos[1]
        # record piece moved and captured for un-move operation
        self.piece_moved = b.board[s_pos[0]][s_pos[1]]
        self.piece_captured = b.board[e_pos[0]][e_pos[1]]
        # record the move in the log



