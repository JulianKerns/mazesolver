from cell import Cell
import time

class Maze:
    def __init__(
            self,
            x1,
            y1,
            num_rows,
            num_cols,
            cell_size_x,
            cell_size_y,
            win= None
        ):

        self._x1 = x1
        self._y1 = y1
        self._num_rows = num_rows
        self._num_cols = num_cols
        self._cell_size_x = cell_size_x
        self._cell_size_y = cell_size_y
        self._win = win

        self.create_cells()
        self.break_entrance_and_exit()
        #self._num_cols = int(self._win.width/ self._cell_size_x)
        #self._num_rows = int(self._win.height / self._cell_size_y)
    def create_cells(self):
        
        self._cells = [[Cell(self._win) for i in range(self._num_rows)] for j in range(self._num_cols)]
        self.draw_cells()

    def draw_cells(self):
        if self._win is None:
            return
        i= self._x1
        j= self._y1

        for x in range(self._num_cols):
            for y in range(self._num_rows):
                self._cells[x][y].draw_cell(i, j, i + self._cell_size_x, j + self._cell_size_y)
                j += self._cell_size_y
                self.animate()
            i += self._cell_size_x
            j = self._y1
          
             

    def animate(self):
        if self._win is None:
            return
        self._win.redraw()
        time.sleep(0.01)

    def break_entrance_and_exit(self):
        self._cells[0][0].has_top_wall = False
        self._cells[0][0].draw_cell(self._x1, self._y1, self._x1 + self._cell_size_x, self._y1 + self._cell_size_y)
        self._cells[-1][-1].has_bottom_wall = False
        self._cells[-1][-1].draw_cell(
                                    self._x1 + self._cell_size_x * (self._num_cols-1),
                                    self._y1 + self._cell_size_y * (self._num_rows-1), 
                                    self._x1 + self._cell_size_x * self._num_cols,
                                    self._y1 + self._cell_size_y * self._num_rows
        )

        





