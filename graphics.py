from tkinter import Tk, BOTH, Canvas

class Window:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.__root = Tk()
        self.__root.title("Maze")
        self.__root.protocol("WM_DELETE_WINDOW", self.close)
        self.__canvas = Canvas(self.__root, bg= "white", width = self.width, height=self.height)
        self.__canvas.pack(fill=BOTH, expand=1)
        self.__running = False
        


    def redraw(self):
        self.__root.update_idletasks()
        self.__root.update()

    
    def wait_for_close(self):
        self.__running = True
        while self.__running:
            self.redraw()
        print("window closed...")

    def close(self):
        self.__running = False
    
    def draw_line(self, line, fill_color= "black"):
        line.draw(self.__canvas,fill_color)

class Point:
    def __init__(self, pos_x, pos_y):
        self.pos_x = pos_x
        self.pos_y = pos_y
        

class Line:
    def __init__(self, point1, point2):
        self.point1 = point1
        self.point2 = point2

    def draw(self, canvas, fill_color= "black"):
        canvas.create_line(self.point1.pos_x, self.point1.pos_y,self.point2.pos_x,self.point2.pos_y,
         fill= fill_color,width=2 )
        canvas.pack(fill=BOTH, expand=1)


            






        
