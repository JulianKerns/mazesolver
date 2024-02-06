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
            win
        ):

        self._x1 = x1
        self._y1 = y1
        self._num_rows = num_rows
        self._num_cols = num_cols
        self._cell_size_x = cell_size_x
        self._cell_size_y = cell_size_y
        self._win = win
        self.create_cells()
        

    def create_cells(self):
        self._num_cols = int(self._win.width/ self._cell_size_x)
        self._num_rows = int(self._win.height / self._cell_size_y)
        self._cells = [[Cell(self._win) for i in range(self._num_rows)] for j in range(self._num_cols)]
        self.draw_cells()

    def draw_cells(self):
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
        self._win.redraw()
        time.sleep(0.01)






