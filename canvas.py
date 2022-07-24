import characters
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
            shape = [(line.x1, line.y1), (line.x2, line.y2)]
            ImageDraw.Draw(canvas_image).line(shape, fill=line.color)

        canvas_image = canvas_image.resize((width, height), Image.ANTIALIAS)

        canvas_string = ""
        for y in range(height):
            for x in range(width):
                canvas_string += characters.convert_value(canvas_image.getpixel((x, y)))
            canvas_string += "\n"

        return canvas_string

class Line:
    def __init__(self, x1, y1, x2, y2, color):
        self.x1 = x1
        self.y1 = y1
        self.x2 = x2
        self.y2 = y2
        self.color = color
