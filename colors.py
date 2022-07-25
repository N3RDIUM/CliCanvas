#!/usr/bin/env python
import curses


def define_colors():
    curses.start_color()
    curses.use_default_colors()

    curses.init_pair(1, curses.COLOR_BLACK, curses.COLOR_BLACK)
    curses.init_pair(2, curses.COLOR_RED, curses.COLOR_BLACK)
    curses.init_pair(3, curses.COLOR_GREEN, curses.COLOR_BLACK)
    curses.init_pair(4, curses.COLOR_YELLOW, curses.COLOR_BLACK)
    curses.init_pair(5, curses.COLOR_BLUE, curses.COLOR_BLACK)
    curses.init_pair(6, curses.COLOR_MAGENTA, curses.COLOR_BLACK)
    curses.init_pair(7, curses.COLOR_CYAN, curses.COLOR_BLACK)
    curses.init_pair(8, curses.COLOR_WHITE, curses.COLOR_BLACK)

    curses.init_pair(9, curses.COLOR_BLACK, curses.COLOR_RED)
    curses.init_pair(10, curses.COLOR_RED, curses.COLOR_RED)
    curses.init_pair(11, curses.COLOR_GREEN, curses.COLOR_RED)
    curses.init_pair(12, curses.COLOR_YELLOW, curses.COLOR_RED)
    curses.init_pair(13, curses.COLOR_BLUE, curses.COLOR_RED)
    curses.init_pair(14, curses.COLOR_MAGENTA, curses.COLOR_RED)
    curses.init_pair(15, curses.COLOR_CYAN, curses.COLOR_RED)
    curses.init_pair(16, curses.COLOR_WHITE, curses.COLOR_RED)

    curses.init_pair(17, curses.COLOR_BLACK, curses.COLOR_GREEN)
    curses.init_pair(18, curses.COLOR_RED, curses.COLOR_GREEN)
    curses.init_pair(19, curses.COLOR_GREEN, curses.COLOR_GREEN)
    curses.init_pair(20, curses.COLOR_YELLOW, curses.COLOR_GREEN)
    curses.init_pair(21, curses.COLOR_BLUE, curses.COLOR_GREEN)
    curses.init_pair(22, curses.COLOR_MAGENTA, curses.COLOR_GREEN)
    curses.init_pair(23, curses.COLOR_CYAN, curses.COLOR_GREEN)
    curses.init_pair(24, curses.COLOR_WHITE, curses.COLOR_GREEN)

    curses.init_pair(25, curses.COLOR_BLACK, curses.COLOR_YELLOW)
    curses.init_pair(26, curses.COLOR_RED, curses.COLOR_YELLOW)
    curses.init_pair(27, curses.COLOR_GREEN, curses.COLOR_YELLOW)
    curses.init_pair(28, curses.COLOR_YELLOW, curses.COLOR_YELLOW)
    curses.init_pair(29, curses.COLOR_BLUE, curses.COLOR_YELLOW)
    curses.init_pair(30, curses.COLOR_MAGENTA, curses.COLOR_YELLOW)
    curses.init_pair(31, curses.COLOR_CYAN, curses.COLOR_YELLOW)
    curses.init_pair(32, curses.COLOR_WHITE, curses.COLOR_YELLOW)

    curses.init_pair(33, curses.COLOR_BLACK, curses.COLOR_BLUE)
    curses.init_pair(34, curses.COLOR_RED, curses.COLOR_BLUE)
    curses.init_pair(35, curses.COLOR_GREEN, curses.COLOR_BLUE)
    curses.init_pair(36, curses.COLOR_YELLOW, curses.COLOR_BLUE)
    curses.init_pair(37, curses.COLOR_BLUE, curses.COLOR_BLUE)
    curses.init_pair(38, curses.COLOR_MAGENTA, curses.COLOR_BLUE)
    curses.init_pair(39, curses.COLOR_CYAN, curses.COLOR_BLUE)
    curses.init_pair(40, curses.COLOR_WHITE, curses.COLOR_BLUE)

    curses.init_pair(41, curses.COLOR_BLACK, curses.COLOR_MAGENTA)
    curses.init_pair(42, curses.COLOR_RED, curses.COLOR_MAGENTA)
    curses.init_pair(43, curses.COLOR_GREEN, curses.COLOR_MAGENTA)
    curses.init_pair(44, curses.COLOR_YELLOW, curses.COLOR_MAGENTA)
    curses.init_pair(45, curses.COLOR_BLUE, curses.COLOR_MAGENTA)
    curses.init_pair(46, curses.COLOR_MAGENTA, curses.COLOR_MAGENTA)
    curses.init_pair(47, curses.COLOR_CYAN, curses.COLOR_MAGENTA)
    curses.init_pair(48, curses.COLOR_WHITE, curses.COLOR_MAGENTA)

    curses.init_pair(49, curses.COLOR_BLACK, curses.COLOR_CYAN)
    curses.init_pair(50, curses.COLOR_RED, curses.COLOR_CYAN)
    curses.init_pair(51, curses.COLOR_GREEN, curses.COLOR_CYAN)
    curses.init_pair(52, curses.COLOR_YELLOW, curses.COLOR_CYAN)
    curses.init_pair(53, curses.COLOR_BLUE, curses.COLOR_CYAN)
    curses.init_pair(54, curses.COLOR_MAGENTA, curses.COLOR_CYAN)
    curses.init_pair(55, curses.COLOR_CYAN, curses.COLOR_CYAN)
    curses.init_pair(56, curses.COLOR_WHITE, curses.COLOR_CYAN)

    curses.init_pair(57, curses.COLOR_BLACK, curses.COLOR_WHITE)
    curses.init_pair(58, curses.COLOR_RED, curses.COLOR_WHITE)
    curses.init_pair(59, curses.COLOR_GREEN, curses.COLOR_WHITE)
    curses.init_pair(60, curses.COLOR_YELLOW, curses.COLOR_WHITE)
    curses.init_pair(61, curses.COLOR_BLUE, curses.COLOR_WHITE)
    curses.init_pair(62, curses.COLOR_MAGENTA, curses.COLOR_WHITE)
    curses.init_pair(63, curses.COLOR_CYAN, curses.COLOR_WHITE)
    curses.init_pair(64, curses.COLOR_WHITE, curses.COLOR_WHITE)

def convert_color(fore, back):
    if back == 'black':
        if fore == 'black':
            return curses.color_pair(1)
        elif fore == 'red':
            return curses.color_pair(2)
        elif fore == 'green':
            return curses.color_pair(3)
        elif fore == 'yellow':
            return curses.color_pair(4)
        elif fore == 'blue':
            return curses.color_pair(5)
        elif fore == 'magenta':
            return curses.color_pair(6)
        elif fore == 'cyan':
            return curses.color_pair(7)
        elif fore == 'white':
            return curses.color_pair(8)
    elif back == 'red':
        if fore == 'black':
            return curses.color_pair(9)
        elif fore == 'red':
            return curses.color_pair(10)
        elif fore == 'green':
            return curses.color_pair(11)
        elif fore == 'yellow':
            return curses.color_pair(12)
        elif fore == 'blue':
            return curses.color_pair(13)
        elif fore == 'magenta':
            return curses.color_pair(14)
        elif fore == 'cyan':
            return curses.color_pair(15)
        elif fore == 'white':
            return curses.color_pair(16)
    elif back == 'green':
        if fore == 'black':
            return curses.color_pair(17)
        elif fore == 'red':
            return curses.color_pair(18)
        elif fore == 'green':
            return curses.color_pair(19)
        elif fore == 'yellow':
            return curses.color_pair(20)
        elif fore == 'blue':
            return curses.color_pair(21)
        elif fore == 'magenta':
            return curses.color_pair(22)
        elif fore == 'cyan':
            return curses.color_pair(23)
        elif fore == 'white':
            return curses.color_pair(24)
    elif back == 'yellow':
        if fore == 'black':
            return curses.color_pair(25)
        elif fore == 'red':
            return curses.color_pair(26)
        elif fore == 'green':
            return curses.color_pair(27)
        elif fore == 'yellow':
            return curses.color_pair(28)
        elif fore == 'blue':
            return curses.color_pair(29)
        elif fore == 'magenta':
            return curses.color_pair(30)
        elif fore == 'cyan':
            return curses.color_pair(31)
        elif fore == 'white':
            return curses.color_pair(32)
    elif back == 'blue':
        if fore == 'black':
            return curses.color_pair(33)
        elif fore == 'red':
            return curses.color_pair(34)
        elif fore == 'green':
            return curses.color_pair(35)
        elif fore == 'yellow':
            return curses.color_pair(36)
        elif fore == 'blue':
            return curses.color_pair(37)
        elif fore == 'magenta':
            return curses.color_pair(38)
        elif fore == 'cyan':
            return curses.color_pair(39)
        elif fore == 'white':
            return curses.color_pair(40)
    elif back == 'magenta':
        if fore == 'black':
            return curses.color_pair(41)
        elif fore == 'red':
            return curses.color_pair(42)
        elif fore == 'green':
            return curses.color_pair(43)
        elif fore == 'yellow':
            return curses.color_pair(44)
        elif fore == 'blue':
            return curses.color_pair(45)
        elif fore == 'magenta':
            return curses.color_pair(46)
        elif fore == 'cyan':
            return curses.color_pair(47)
        elif fore == 'white':
            return curses.color_pair(48)
    elif back == 'cyan':
        if fore == 'black':
            return curses.color_pair(49)
        elif fore == 'red':
            return curses.color_pair(50)
        elif fore == 'green':
            return curses.color_pair(51)
        elif fore == 'yellow':
            return curses.color_pair(52)
        elif fore == 'blue':
            return curses.color_pair(53)
        elif fore == 'magenta':
            return curses.color_pair(54)
        elif fore == 'cyan':
            return curses.color_pair(55)
        elif fore == 'white':
            return curses.color_pair(56)
    elif back == 'white':
        if fore == 'black':
            return curses.color_pair(57)
        elif fore == 'red':
            return curses.color_pair(58)
        elif fore == 'green':
            return curses.color_pair(59)
        elif fore == 'yellow':
            return curses.color_pair(60)
        elif fore == 'blue':
            return curses.color_pair(61)
        elif fore == 'magenta':
            return curses.color_pair(62)
        elif fore == 'cyan':
            return curses.color_pair(63)
        elif fore == 'white':
            return curses.color_pair(64)
