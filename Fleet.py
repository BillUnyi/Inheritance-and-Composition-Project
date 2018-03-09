from graphics import *

class Window(object):
    """Draws water and the fleet"""
    def __init__(self, win):
        water = Water("Blue", win)
        fleet = Fleet(win)

class Water(object):
    """draws the water"""
    def __init__(self, color, win):
        self.color = color
        self.drawWater(color, win)

    def drawWater(self, color, win):
        water = Rectangle(Point(-25, 500), Point(1925, 1050))
        water.setFill(color)
        water.setOutline(color)
        water.draw(win)

class Fleet(object):
    """draws everything from the fleet"""
    def __init__(self, win):
        aircraftCarrier1 = AircraftCarrier(400, 550, "Gray", "Gray3", win)
        aircraftCarrier2 = AircraftCarrier(600, 700, "Gray", "Gray3", win)
        aircraftCarrier3 = AircraftCarrier(1300, 600, "Gray", "Gray3", win)

class AircraftCarrier(object):
    """Draws an aircraft carrier and it's squadron"""
    def __init__(self, x, y, color, outline, win):
        self.drawAircraftCarrier(x, y, color, outline, win)
        airplane1 = Airplane(x, y, 25, 0, Color.darkGray, "Black", win)
        airplane2 = Airplane(x, y, 250, -300, Color.darkGray, "Black", win)
        airplane3 = Airplane(x, y, -200, -400, Color.darkGray, "Black", win)

    def drawAircraftCarrier(self, x, y, color, outline, win):
        ship = Polygon(Point(x, y), Point(x + 75, y - 25), Point(x + 300, y - 20), Point(x + 350, y + 10), Point(x + 340, y + 80), Point(x + 100, y + 100))
        ship.setFill(color)
        ship.setOutline(outline)
        ship.draw(win)
        shipBase = Polygon(Point(x, y), Point(x + 75, y - 25), Point(x + 300, y - 20), Point(x + 350, y + 10), Point(x + 100, y + 20))
        shipBase.setFill(color)
        shipBase.setOutline(outline)
        shipBase.draw(win)
        line = Line(Point(x + 100, y + 100), Point(x + 100, y + 20))
        line.setOutline(outline)
        line.draw(win)

class Airplane(object):
    """Draws a fighter jet"""
    def __init__(self, X, Y, x, y, color, outline, win):
        self.drawAirplane(X, Y, x, y, color, outline, win)

    def drawAirplane(self, X, Y, x, y, color, outline, win):
        rightWing = Polygon(Point(X + x + 60, Y + y), Point(X + x + 135, Y + y - 5), Point(X + x + 100, Y + y - 30))
        rightWing.setFill(color)
        rightWing.setOutline(outline)
        rightWing.draw(win)
        plane = Polygon(Point(X + x, Y + y), Point(X + x + 50, Y + y - 10), Point(X + x + 100, Y + y - 15), Point(X + x + 150, Y + y - 15),
                        Point(X + x + 155 , Y + y - 10), Point(X + x + 158, Y + y), Point(X + x + 150, Y + y + 5), Point(X + x + 100, Y + y + 5),
                        Point(X + x + 50, Y + y + 2))
        plane.setFill(color)from graphics import *

class Window(object):
    """Draws water and the fleet"""
    def __init__(self, win):
        water = Water("Blue", win)
        fleet = Fleet(win)

class Water(object):
    """draws the water"""
    def __init__(self, color, win):
        self.color = color
        self.drawWater(color, win)

    def drawWater(self, color, win):
        water = Rectangle(Point(-25, 500), Point(1925, 1050))
        water.setFill(color)
        water.setOutline(color)
        water.draw(win)

class Fleet(object):
    """draws everything from the fleet"""
    def __init__(self, win):
        aircraftCarrier1 = AircraftCarrier(400, 550, "Gray", "Gray3", win)
        aircraftCarrier2 = AircraftCarrier(600, 700, "Gray", "Gray3", win)
        aircraftCarrier3 = AircraftCarrier(1300, 600, "Gray", "Gray3", win)

class AircraftCarrier(object):
    """Draws an aircraft carrier and it's squadron"""
    def __init__(self, x, y, color, outline, win):
        self.drawAircraftCarrier(x, y, color, outline, win)
        airplane1 = Airplane(x, y, 25, 0, Color.darkGray, "Black", win)
        airplane2 = Airplane(x, y, 250, -300, Color.darkGray, "Black", win)
        airplane3 = Airplane(x, y, -200, -400, Color.darkGray, "Black", win)
        boat1 = Boat(x, y, -200, 100, "Gray", "Gray3", win)

    def drawAircraftCarrier(self, x, y, color, outline, win):
        ship = Polygon(Point(x, y), Point(x + 75, y - 25), Point(x + 300, y - 20), Point(x + 350, y + 10), Point(x + 340, y + 80), Point(x + 100, y + 100))
        ship.setFill(color)
        ship.setOutline(outline)
        ship.draw(win)
        shipBase = Polygon(Point(x, y), Point(x + 75, y - 25), Point(x + 300, y - 20), Point(x + 350, y + 10), Point(x + 100, y + 20))
        shipBase.setFill(color)
        shipBase.setOutline(outline)
        shipBase.draw(win)
        line = Line(Point(x + 100, y + 100), Point(x + 100, y + 20))
        line.setOutline(outline)
        line.draw(win)

class Airplane(object):
    """Draws a fighter jet"""
    def __init__(self, X, Y, x, y, color, outline, win):
        self.drawAirplane(X, Y, x, y, color, outline, win)

    def drawAirplane(self, X, Y, x, y, color, outline, win):
        rightWing = Polygon(Point(X + x + 60, Y + y), Point(X + x + 135, Y + y - 5), Point(X + x + 100, Y + y - 30))
        rightWing.setFill(color)
        rightWing.setOutline(outline)
        rightWing.draw(win)
        plane = Polygon(Point(X + x, Y + y), Point(X + x + 50, Y + y - 10), Point(X + x + 100, Y + y - 15), Point(X + x + 150, Y + y - 15),
                        Point(X + x + 155 , Y + y - 10), Point(X + x + 158, Y + y), Point(X + x + 150, Y + y + 5), Point(X + x + 100, Y + y + 5),
                        Point(X + x + 50, Y + y + 2))
        plane.setFill(color)
        plane.setOutline(outline)
        plane.draw(win)
        leftWing = Polygon(Point(X + x + 75, Y + y - 2), Point(X + x + 140, Y + y - 5), Point(X + x + 180, Y + y + 15))
        leftWing.setFill(color)
        leftWing.setOutline(outline)
        leftWing.draw(win)


class Boat(object):

    def __init__(self, X, Y, x, y, color, outline, win):
        self.drawBoat(X, Y, x, y, color, outline, win)

    def drawBoat(self, X, Y, x, y, color, outline, win):
        boat = Polygon(Point(X+x,Y+y),Point(X + x + 175, Y + y), Point(X + x + 125, Y + y + 50),Point(X + x + 75,Y + y + 50),Point(X + x,Y + y),Point(X + x + 75, Y + y - 25),Point(X + x + 100, Y + y))
        boat.setFill(color)
        boat.setOutline(outline)
        boat.draw(win)




class Color(object):
    """Holds colors"""
    lightGray = color_rgb(121, 121, 121)
    darkGray = color_rgb(80,80,80)

def main():
    win = GraphWin("Fleet", 1900, 1040) #fits my window at home change if nessasary
    win.setBackground("Cyan")
    window = Window(win)
    win.getMouse()
    win.close()

main()

        plane.setOutline(outline)
        plane.draw(win)
        leftWing = Polygon(Point(X + x + 75, Y + y - 2), Point(X + x + 140, Y + y - 5), Point(X + x + 180, Y + y + 15))
        leftWing.setFill(color)
        leftWing.setOutline(outline)
        leftWing.draw(win)

class Color(object):
    """Holds colors"""
    lightGray = color_rgb(121, 121, 121)
    darkGray = color_rgb(80,80,80)

def main():
    win = GraphWin("Fleet", 1900, 1040) #fits my window at home change if nessasary
    win.setBackground("Cyan")
    window = Window(win)
    win.getMouse()
    win.close()

main()
