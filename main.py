from graphics import *

if __name__ == "__main__":
    win = GraphWin("Sup", 500, 500)
    txt = Text(Point(250, 250), "Heeeeyyy")
    txt.draw(win)

    win.getMouse()
    win.close()