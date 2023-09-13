import sys
import board
import board as b
import pygame as p
import time

# solve libpng warning: iCCP: known incorrect sRGB profile
# use: mogrify *.png
ROW_DIM = 10
COL_DIM = 9
background_colour = (234, 212, 252)
PIECE_SIZE = 60
OFFSET = 50
CENTER = (-20, -20)
ROW_MARGIN = 10
COL_MARGIN = 10
WIDTH = 750
HEIGHT = 667
# load and transform images

# a dictionary of scaled images
# board = 960 * 880 pieces = 70 * 70
IMAGES = {}
PIECESLIST = ('bC', 'bM', 'bP', 'bX', 'bS', 'bW', 'bZ', 'rC', 'rM', 'rP', 'rX', 'rS', 'rW', 'rZ')
# scale the board



def load_images():
    IMAGES['bg'] = p.transform.scale(p.image.load("./images/bg.jpg"), (750,500))
    IMAGES['wood_bg'] = p.transform.scale(p.image.load("./images/wood_bg.jpg"), (COL_DIM*PIECE_SIZE,ROW_DIM*PIECE_SIZE))
    IMAGES['board'] = p.transform.scale(p.image.load("./images/chinese_chess.jpg"),
                                        ((COL_DIM-1)*PIECE_SIZE+2*COL_MARGIN, (ROW_DIM-1)*PIECE_SIZE+2*ROW_MARGIN))
    #IMAGES['board'] = p.image.load("./images/chinese_chess.jpg")
    for piece in PIECESLIST:
        IMAGES[piece] = p.transform.scale(p.image.load("./images/" + piece + ".png"), (PIECE_SIZE, PIECE_SIZE))
def draw_board(screen):
    screen.blit(IMAGES['bg'], (0, 0))
    screen.blit(IMAGES['bg'], (0, 500))
    screen.blit(IMAGES['wood_bg'], (OFFSET+CENTER[0], OFFSET+CENTER[1]))
    screen.blit(IMAGES['board'], (OFFSET, OFFSET))


def draw_pieces(screen, b):
    # 9 * 10 board
    for row in range(ROW_DIM):
        for col in range(COL_DIM):
            # find what is in this intersection
            if b.board[row][col] != "--" :
                piece = b.board[row][col]
                screen.blit(IMAGES[piece], (col * PIECE_SIZE  + OFFSET + CENTER[0], row * PIECE_SIZE +
                                            OFFSET+ CENTER[1]))


# main loop
def main():
    p.init()
    screen = p.display.set_mode((WIDTH, HEIGHT))
    load_images()
    screen.fill(background_colour)
    b = board.chess_board()
    # to record mouse positions
    start_end = []
    while True:

        # detect events
        # if quit then close the process
        for event in p.event.get():
            if event.type == p.QUIT:
                p.quit()
                sys.exit()
            # detect mouse input as piece moves
            elif event.type == p.MOUSEBUTTONDOWN:
                # compute row and col of the position
                # need to shift the board so the bC align with the origin
                row = (p.mouse.get_pos()[1] - (OFFSET + CENTER[0])) // PIECE_SIZE
                col = (p.mouse.get_pos()[0] - (OFFSET + CENTER[1])) // PIECE_SIZE
                # only count as piece selection if the click happens on the board
                if (row>=0 and row<=9) and (col>=0 and col<=8):
                    mouse_pos = (row, col)
                    # get where the mouse clicked
                    # if it is the starting pos
                    if len(start_end) == 0:
                        start_end.append(mouse_pos)
                    # if it is the ending pos
                    else:
                        # if not click same square twice
                        if start_end[0] != mouse_pos:
                            start_end.append(mouse_pos)
                            # create and make move from start pos to end pos
                            move = board.move(start_end[0], start_end[1], b)
                            b.make_move(move)

                        # clear the list to take next move
                        start_end = []




        # render the board
        draw_board(screen)
        # render the pieces
        draw_pieces(screen, b)
        p.display.flip()









if __name__ == '__main__':
    main()

