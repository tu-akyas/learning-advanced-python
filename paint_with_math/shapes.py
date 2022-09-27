class Square:
    def __init__(self, x, y, side, color):
        self.x = x
        self.y = y
        self.side = side
        self.color = color

    def draw(self, canvas):
        x_start = self.x
        x_end = self.x + self.side
        y_start = self.y
        y_end = self.y + self.side
        canvas.page_data[x_start:x_end, y_start:y_end] = self.color



class Rectangle:
    def __init__(self, x, y, height, width, color):
        self.x = x
        self.y = y
        self.height = height
        self.width = width
        self.color = color

    def draw(self, canvas):
        x_start = self.x
        x_end = self.x + self.width
        y_start = self.y
        y_end = self.y + self.height
        canvas.page_data[x_start:x_end, y_start:y_end] = self.color