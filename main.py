import time
import curses
import random

from fire import fire
from ship import animate_ship
from stars import blink
from load_frames import get_frames_from_files


SYMBOLS = ['*', ':', '+', '.']
TIC_TIMEOUT = 0.1


def draw(canvas):
    coroutines = []
    height, width = canvas.getmaxyx()
    curses.curs_set(False)
    ship_frames = get_frames_from_files(('rocket_frame_1.txt', 'rocket_frame_2.txt'))
    coroutine_bang = fire(canvas, height / 2, width / 2)
    coroutine_ship = animate_ship(canvas, height / 2, width / 2, ship_frames)
    coroutines.append(coroutine_bang)
    coroutines.append(coroutine_ship)
    border_size = 1

    for _ in range(100):
        symbol = random.choice(SYMBOLS)
        y_coord = random.randint(1, height - border_size)
        x_coord = random.randint(1, width - border_size)
        coroutine = blink(canvas, y_coord, x_coord, symbol, random.randint(1, 5))
        coroutines.append(coroutine)
    while coroutines:
        for coroutine in coroutines.copy():
            try:
                coroutine.send(None)
            except StopIteration:
                coroutines.remove(coroutine)
        canvas.refresh()
        time.sleep(TIC_TIMEOUT)


if __name__ == "__main__":
    curses.update_lines_cols()
    curses.wrapper(draw)
