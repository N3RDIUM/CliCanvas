import curses
import characters
import colors
from PIL import Image, ImageDraw
import numpy as np

class Canvas:
    def __init__(self):
        self.lines = []

    def add_line(self, line):
        self.lines.append(line)

    def ret(self, width, height):
        canvas_image = Image.new('1', (width, height))
        
        # Draw lines
        for line in self.lines:
            shape = [(line.x1, line.y1/2), (line.x2, line.y2/2)]
            ImageDraw.Draw(canvas_image).line(shape, fill=line.color)

        canvas_image = canvas_image.resize((width, height), Image.ANTIALIAS)

        canvas_string = []
        for pixel in range(len(canvas_image.getdata()) - 1):
            _pixel = canvas_image.getdata()[pixel]
            if _pixel > 0 and pixel < (255/3)*1:
                _ = curses.A_DIM
            elif _pixel > (255/3)*1 and pixel < (255/3)*2:
                _ = curses.A_NORMAL
            elif _pixel > (255/3)*2 and pixel < 255:
                _ = curses.A_BOLD
            else:
                _ = curses.A_NORMAL
            
            # get character position
            x = pixel % width
            y = int(pixel / width)

            canvas_string.append((characters.convert_value(_pixel), colors.convert_color('white', 'black'), _, (x, y)))

        return canvas_string

class Line:
    def __init__(self, x1, y1, x2, y2, color):
        self.x1 = x1
        self.y1 = y1
        self.x2 = x2
        self.y2 = y2
        self.color = color
