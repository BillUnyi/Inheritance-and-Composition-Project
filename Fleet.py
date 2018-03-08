from Graphics import *

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
    def __init__(self, x, y, color, background, win):
        self.drawAircraftCarrier(x, y, color, background, win)

    def drawAircraftCarrier(self, x, y, color, background, win):
        ship = Polygon(Point(x, y), Point(x + 350, y), Point(x + 340, y + 100), Point(x + 75, y + 100))
        ship.setFill(color)
        ship.setOutline(background)
        ship.draw(win)

def main():
    win = GraphWin("Fleet", 1900, 1040)
    win.setBackground("Cyan")
    window = Window(win)
    win.getMouse()
    win.close()

main()

