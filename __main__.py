import curses
import datetime
import traceback
from curses import wrapper
import time

def schermo(scr, *args):
    try:
        ch = ''
        stdscr = curses.initscr()
        curses.cbreak()
        stdscr.timeout(100)
        while ch != ord('q'):
            stdscr.addstr(3, 2, f'{datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")}',  curses.A_NORMAL)
            stdscr.clrtobot()
            ch = stdscr.getch()

    except:
        traceback.print_exc()
    finally:
        curses.endwin()

curses.wrapper(schermo) 
