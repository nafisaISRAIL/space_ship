import asyncio
import curses


async def blink(canvas, row, column, symbol='*', offset_tics=0):
    for _ in range(offset_tics):
        await asyncio.sleep(0)
    while True:
        canvas.addstr(row, column, symbol, curses.A_DIM)
        for _ in range(3):
            await asyncio.sleep(0)
        canvas.addstr(row, column, symbol)
        await asyncio.sleep(0)
        canvas.addstr(row, column, symbol, curses.A_BOLD)
        for _ in range(2):
            await asyncio.sleep(0)
        canvas.addstr(row, column, symbol)
        await asyncio.sleep(0)
