from graphics import Window
from cell import Cell
from maze import Maze

def main():
    win = Window(800,800)
    maze= Maze(2,2,0,0,50,50,win)
    
    

   
    win.wait_for_close()
main()  

"""main()
    cell1 = Cell(win)
    cell1.has_right_wall = False
    cell1.draw_cell(50,50,100,100)

    cell2 = Cell(win)
    cell2.has_left_wall = False
    cell2.has_bottom_wall = False
    cell2.draw_cell(100,50,150,100)

    cell1.draw_move(cell2)

    cell3 = Cell(win)
    cell3.has_top_wall = False
    cell3.has_right_wall = False
    cell3.draw_cell(100,100,150,150)

    cell2.draw_move(cell3)

    cell4 = Cell(win)
    cell4.has_left_wall = False
    cell4.draw_cell(150,100,200,150)

    cell3.draw_move(cell4,True)

#line1= Line(Point(500,50), Point(500,500))
 #   win.draw_line(line1,"black")
  #  line2= Line(Point(200,50), Point(300,300))
    
   # win.draw_line(line2,"black")"""


