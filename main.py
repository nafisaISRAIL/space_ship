import time
import curses
import random

from fire import fire
from ship import print_ship
from stars import blink


SYMBOLS = ['*', ':', '+', '.']
TIC_TIMEOUT = 0.1


with open("rocket_frame_1.txt", "r") as f:
    frame1 = f.read()


with open("rocket_frame_2.txt", "r") as f:
    frame2 = f.read()


def draw(canvas):
    coroutines = []
    row, column = canvas.getmaxyx()
    curses.curs_set(False)
    bang = fire(canvas, row / 2, column / 2)
    ships = print_ship(canvas, row / 2, column / 2, (frame1, frame2))
    coroutines.append(bang)
    coroutines.append(ships)

    for _ in range(100):
        symbol = random.choice(SYMBOLS)
        y = random.randint(1, row - 1)
        x = random.randint(1, column - 1)
        coroutine = blink(canvas, y, x, symbol, random.randint(1, 5))
        coroutines.append(coroutine)
    while True:
        for coroutine in coroutines:
            try:
                coroutine.send(None)
                canvas.refresh()
            except StopIteration:
                coroutines.remove(coroutine)
        if len(coroutines) == 0:
            break
        time.sleep(TIC_TIMEOUT)


if __name__ == "__main__":
    curses.update_lines_cols()
    curses.wrapper(draw)
