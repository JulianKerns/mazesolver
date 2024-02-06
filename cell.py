from graphics import Window, Point, Line


class Cell:
    def __init__(self, win):
        self.has_left_wall = True
        self.has_right_wall = True
        self.has_top_wall = True
        self.has_bottom_wall = True
        self._x1 = None
        self._y1 = None
        self._x2 = None
        self._y2 = None
        self._win = win


    def draw_cell(self ,x1 ,y1 ,x2, y2):
        self._x1 = x1
        self._y1 = y1
        self._x2 = x2
        self._y2 = y2
        if self.has_left_wall:
            line= Line(Point(x1,y1), Point(x1,y2))
            self._win.draw_line(line)
        if self.has_right_wall:
            line= Line(Point(x2,y1), Point(x2,y2))
            self._win.draw_line(line)
        if self.has_top_wall:
            line= Line(Point(x1,y1), Point(x2,y1))
            self._win.draw_line(line)
        if self.has_bottom_wall:
            line= Line(Point(x1,y2), Point(x2,y2))
            self._win.draw_line(line)


    def draw_move(self, to_cell, undo=False):
        if self._win is None:
            return
        middle_x = self._x1 + (self._x2-self._x1)/2
        middle_y = self._y1 + (self._y2-self._y1)/2
       
        to_middle_x = to_cell._x1 + (to_cell._x2-to_cell._x1)/2
        to_middle_y = to_cell._y1 + (to_cell._y2-to_cell._y1)/2
        
        
        fill_color = "red"
        if undo:
            fill_color = "gray"
        

        # moving left, potential bug frim the given solution with the starting and end points
        if self._x1 > to_cell._x1:
            line = Line(Point(self._x1, middle_y),Point(middle_x, middle_y))
            self._win.draw_line(line, fill_color)
            line = Line(Point(to_middle_x, to_middle_y),Point(to_cell._x2, to_middle_y))
            self._win.draw_line(line, fill_color)

        # moving right
        if self._x1 < to_cell._x1:
            line = Line(Point(middle_x, middle_y),Point(self._x2, middle_y))
            self._win.draw_line(line, fill_color)
            line = Line(Point(to_cell._x1, to_middle_y),Point(to_middle_x, to_middle_y))
            self._win.draw_line(line, fill_color)

        # moving up
        if self._y1 > to_cell._y1:
            line = Line(Point(middle_x, middle_y),Point(middle_x, self._y1))
            self._win.draw_line(line, fill_color)
            line = Line(Point(to_middle_x,to_cell._y2),Point(to_middle_x, to_middle_y))
            self._win.draw_line(line, fill_color)

        # moving down
        if self._y1 < to_cell._y1:
            line = Line(Point(middle_x, middle_y),Point(middle_x, self._y2))
            self._win.draw_line(line, fill_color)
            line = Line(Point(to_middle_x, to_middle_y),Point(to_middle_x,to_cell._y1))
            self._win.draw_line(line, fill_color)




        


