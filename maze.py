from cell import Cell
import time
import random

class Maze:
    def __init__(
            self,
            x1,
            y1,
            num_rows,
            num_cols,
            cell_size_x,
            cell_size_y,
            win = None,
            seed= None
        ):

        self._x1 = x1
        self._y1 = y1
        self._num_rows = num_rows
        self._num_cols = num_cols
        self._cell_size_x = cell_size_x
        self._cell_size_y = cell_size_y
        self._win = win
        if seed is not None:
            random.seed(seed)

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
    def break_walls_R(self,i,j):
        self._cells[i][j]._visited = True
        while True:
            to_visit = []
            if ((i+1) < self._num_rows) and self._cells[i+1][j]._visited == False:
                to_visit.append((i+1,j))
            if ((j+1) < self._num_cols) and self._cells[i][j+1]._visited == False:
                to_visit.append((i,j+1))
            if ((i-1) >= 0) and self._cells[i-1][j]._visited == False:
                to_visit.append((i-1,j))
            if ((j-1 )>= 0) and self._cells[i][j-1]._visited == False:
                to_visit.append((i,j-1))
                
            if not to_visit:
                self._draw_cell(
                            self._x1 + self._cell_size_x * i,
                            self._y1 + self._cell_size_y * j, 
                            self._x1 + self._cell_size_x * (i+1),
                            self._y1 + self._cell_size_y * (j+1)
                            )
                return

            next_i , next_j = random.choice(to_visit)
            if next_i - i == 1: # moving down
                self._cells[i][j].has_bottom_wall = False
                self._cells[next_i][next_j].has_top_wall = False
                           
            elif next_i - i == -1: # moving up
                self._cells[i][j].has_top_wall = False
                self._cells[next_i][next_j].has_bottom_wall = False

            elif next_j - j == 1: # moving right
                self._cells[i][j].has_right_wall = False
                self._cells[next_i][next_j].has_left_wall = False
                    

            elif next_j - j == -1: # moving left
                self._cells[i][j].has_left_wall = False
                self._cells[next_i][next_j].has_right_wall = False
                           
            self.break_walls_R(next_i,next_j)








        




 
