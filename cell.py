from graphics import Line, Point


class Cell:
    def __init__(self, win):
        self.has_left_wall = True
        self.has_right_wall = True
        self.has_top_wall = True
        self.has_bottom_wall = True
        self._x1 = None
        self._x2 = None
        self._y1 = None
        self._y2 = None
        self._win = win

    def draw(self, x1, y1, x2, y2):
        self._x1 = x1
        self._x2 = x2
        self._y1 = y1
        self._y2 = y2
        if self.has_left_wall:
            line = Line(Point(x1, y1), Point(x1, y2))
            self._win.draw_line(line)
        if self.has_top_wall:
            line = Line(Point(x1, y1), Point(x2, y1))
            self._win.draw_line(line)
        if self.has_right_wall:
            line = Line(Point(x2, y1), Point(x2, y2))
            self._win.draw_line(line)
        if self.has_bottom_wall:
            line = Line(Point(x1, y2), Point(x2, y2))
            self._win.draw_line(line)
    
    def draw_move(self, to_cell, undo=False):
        #  calculate the center coordinates of the current cell.
        from_x = self.x + self.width / 2
        from_y = self.y + self.height / 2

        # calculate the center coordinates of the destination cell.
        to_x = to_cell.x + to_cell.width / 2
        to_y = to_cell.y + to_cell.height / 2

        # determine the colour of the line based on undo flag 
        color = "gray" if undo else "red"

        # Draw the line between the centers of the two cells.
        self.canvas.create_line(from_x,from_y,to_x,to_y,fill=color,width=2)
        