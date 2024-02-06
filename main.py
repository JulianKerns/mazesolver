from graphics import Window , Line, Point

def main():
    win = Window(800,600)
    point1 = Point(400,400)
    point2 = Point(100,100)
    line= Line(point1,point2)
    win.draw_line(line,"black")
    win.wait_for_close()

main()





