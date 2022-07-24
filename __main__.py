from curses import wrapper
import curses
import datetime
import canvas
import traceback
import random
import time

_canvas = canvas.Canvas()
l = canvas.Line(x1=0, y1=0, x2=1023, y2=1023, color=255)
_canvas.add_line(l)


def schermo(scr, *args):
    try:
        ch = ''
        stdscr = curses.initscr()
        curses.cbreak()
        stdscr.timeout(100)
        while ch != ord('q'):
            l.x1 = random.randint(0, 100)
            l.y1 = random.randint(0, 100)
            l.x2 = random.randint(100, 200)
            l.y2 = random.randint(100, 200)
            stdscr.addstr(0, 0, f"{datetime.datetime.now()}")
            stdscr.addstr(0, 0, _canvas.ret(scr.getmaxyx()[1]-1, scr.getmaxyx()[0]-1))
            stdscr.clrtobot()
            ch = stdscr.getch()

    except:
        traceback.print_exc()
    finally:
        curses.endwin()


curses.wrapper(schermo)
