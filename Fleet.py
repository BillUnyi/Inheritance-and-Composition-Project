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
        airplane2 = SuperAirplane(x, y, 250, -300, Color.darkGray, "Black", win)
        airplane3 = SuperAirplane(x, y, -200, -400, Color.darkGray, "Black", win)
        personel1 = Personel(x, y, 300, -30, Color.lightTan, Color.darkGray1, "Blue4", "Black", win)
        personel2 = Personel(x, y, 320, -40, Color.tan, Color.darkGray1, "Blue4", "Black", win)
        personel3 = Personel(x, y, 280, -50, Color.darkTan, Color.darkGray1, "Blue4", "Black", win)
        personel4 = Personel(x, y, 275, -35, Color.lightTan, Color.darkGray1, "Blue4", "Black", win)
        personel5 = Personel(x, y, 260, -30, Color.lightTan, Color.darkGray1, "Blue4", "Black", win)
        personel6 = Personel(x, y, 240, -40, Color.tan, Color.darkGray1, "Blue4", "Black", win)
        personel7 = Personel(x, y, 220, -50, Color.darkTan, Color.darkGray1, "Blue4", "Black", win)
        personel8 = Personel(x, y, 230, -30, Color.tan, Color.darkGray1, "Blue4", "Black", win)

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
    def __init__(self, X, Y, x, y, mainColor, outline, win):
        self.drawAirplane(X, Y, x, y, mainColor, outline, win)

    def drawAirplane(self, X, Y, x, y, mainColor, outline, win):
        rightWing = Polygon(Point(X + x + 60, Y + y), Point(X + x + 135, Y + y - 5), Point(X + x + 100, Y + y - 30))
        rightWing.setFill(mainColor)
        rightWing.setOutline(outline)
        rightWing.draw(win)
        plane = Polygon(Point(X + x, Y + y), Point(X + x + 50, Y + y - 10), Point(X + x + 100, Y + y - 15), Point(X + x + 150, Y + y - 15),
                        Point(X + x + 155 , Y + y - 10), Point(X + x + 158, Y + y), Point(X + x + 150, Y + y + 9), Point(X + x + 100, Y + y + 10),
                        Point(X + x + 50, Y + y + 7))
        plane.setFill(mainColor)
        plane.setOutline(outline)
        plane.draw(win)
        window = Polygon(Point(X + x, Y + y), Point(X + x + 50, Y + y - 10),Point(X + x + 45, Y + y))
        window.setFill("Black")
        window.setOutline("Black")
        window.draw(win)
        leftWing = Polygon(Point(X + x + 75, Y + y - 2), Point(X + x + 140, Y + y - 5), Point(X + x + 180, Y + y + 15))
        leftWing.setFill(mainColor)
        leftWing.setOutline(outline)
        leftWing.draw(win)

class SuperAirplane(Airplane):
    """draws an airplane with extra detail"""
    def __init__(self, X, Y, x, y, mainColor, outline, win):
        super().__init__(X, Y, x, y, mainColor, outline, win)
        self.drawStar(X, Y, x, y, win)
        self.drawFlames(X, Y, x, y, win)

    def drawStar(self, X, Y, x, y, win):
        star = Polygon(Point(X + x + 60, Y + y - 9), Point(X + x + 62, Y + y - 4), Point(X + x + 68, Y + y + - 4), Point(X + x + 64, Y + y),
                       Point(X + x + 65, Y + y + 5), Point(X + x + 60, Y + y + 2), Point(X + x + 55, Y + y + 5), Point(X + x + 56, Y + y),
                       Point(X + x + 52, Y + y - 4), Point(X + x + 58, Y + y - 4))
        star.setFill("Red")
        star.setOutline("Black")
        star.draw(win)

    def drawFlames(self, X, Y, x, y, win):
        flames = Polygon(Point()) #left off here

class Personel(object):
    """draws personel"""
    def __init__(self, X, Y, x, y, skinColor, uniformColor, pantsColor, outline, win):
        self.drawPersonel(X, Y, x, y, skinColor, uniformColor, pantsColor, outline, win)

    def drawPersonel(self, X, Y, x, y, skinColor, uniformColor, pantsColor, outline, win):
        head = Circle(Point(X + x, Y + y), 5)
        head.setFill(skinColor)
        head.setOutline(outline)
        head.draw(win)
        hands = Polygon(Point(X + x - 10, Y + y + 6), Point(X + x + 10, Y + y + 6), Point(X + x, Y + y + 40))
        hands.setFill(uniformColor)
        hands.setOutline(outline)
        hands.draw(win)
        body = Polygon(Point(X + x - 6, Y + y + 6), Point(X + x + 6, Y + y + 6), Point(X + x + 5, Y + y + 20), Point(X + x - 5, Y + y + 20),)
        body.setFill(uniformColor)
        body.setOutline(outline)
        body.draw(win)
        legs = Polygon(Point(X + x - 5, Y + y + 20), Point(X + x + 5, Y + y + 20), Point(X + x + 4, Y + y + 40), Point(X + x - 4, Y + y + 40))
        legs.setFill(pantsColor)
        legs.setOutline(outline)
        legs.draw(win)
        line = Line(Point(X + x, Y + y + 25), Point(X + x, Y + y + 40))
        line.setOutline(outline)
        line.draw(win)

class Color(object):
    """Holds colors"""
    lightGray = color_rgb(121, 121, 121)
    darkGray = color_rgb(80, 80, 80)
    darkGray1 = color_rgb(40, 40, 40)
    lightTan = color_rgb(246, 235, 204)
    tan = color_rgb(218, 193, 125)
    darkTan = color_rgb(97, 48, 0)

def main():
    win = GraphWin("Fleet", 1900, 1040) #fits my window at home,c change if nessasary
    win.setBackground("Cyan")
    window = Window(win)
    win.getMouse()
    win.close()

main()
