from graphics import Window
from cell import Cell 

def main():
    win = Window(800,600)
    cell = Cell(win)
    cell.draw_cell(50,50,100,100)

    cell = Cell(win)
    cell.has_left_wall = False
    cell.draw_cell(150,150,200,200)

    cell = Cell(win)
    cell.has_right_wall = False
    cell.draw_cell(120,120,400,400)

    cell = Cell(win)
    cell.has_left_wall = False
    cell.has_top_wall = False
    cell.draw_cell(200,200,500,500)

    

    
    
    
    
    
    win.wait_for_close()

main()


#line1= Line(Point(500,50), Point(500,500))
 #   win.draw_line(line1,"black")
  #  line2= Line(Point(200,50), Point(300,300))
    
   # win.draw_line(line2,"black")


