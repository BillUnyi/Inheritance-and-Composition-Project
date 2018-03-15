from graphics import *
import random

class Window(object):
    """Draws water and the fleet"""
    def __init__(self, win):
        self.water1 = Water("Blue", win)
        self.fleet1 = Fleet(win)

class Water(object):
    """draws the water"""
    def __init__(self, color, win):
        self.water = None
        self.sun = None
        self.moon = None
        self.island = None
        self.rect = None
        self.rect1 = None
        self.rect2 = None
        self.line = None
        self.drawSun(win)
        self.drawWater(color, win)
        self.drawFlag(win)
        self.drawIsland(win)
        tank1 = SuperTank(0, 0, 1350, 480, Color.lightGray, Color.darkGray, win)
        tank2 = SuperTank(0, 0, 1475, 470, Color.lightGray, Color.darkGray, win)
        tank3 = SuperTank(0, 0, 1560, 480, Color.lightGray, Color.darkGray, win)

    def drawWater(self, color, win):
        self.water = Rectangle(Point(-25, 500), Point(1925, 1050))
        self.water.setFill(color)
        self.water.setOutline(color)
        self.water.draw(win)

    def drawIsland(self, win):
        self.island = Polygon(Point(1700, 500), Point(1500, 475), Point(1300, 500))
        self.island.setFill(Color.tan)
        self.island.setOutline("Black")
        self.island.draw(win)

    def drawFlag(self, win):
        self.rect = Rectangle(Point(1330, 300), Point(1530, 333))
        self.rect.setFill("White")
        self.rect.setOutline("White")
        self.rect.draw(win)
        self.rect1 = Rectangle(Point(1330, 334), Point(1530, 366))
        self.rect1.setFill("Blue")
        self.rect1.setOutline("Blue")
        self.rect1.draw(win)
        self.rect2 = Rectangle(Point(1330, 367), Point(1530, 400))
        self.rect2.setFill("Red")
        self.rect2.setOutline("Red")
        self.rect2.draw(win)
        self.line = Line(Point(1530, 300), Point(1530, 500))
        self.line.setOutline("Black")
        self.line.setWidth(3)
        self.line.draw(win)

    def drawSun(self, win):
        self.sun = Circle(Point(1700, 150), 50)
        self.sun.setFill("Yellow")
        self.sun.setOutline("Black")
        self.sun.draw(win)

    def drawMoon(self, win):
        self.moon = Circle(Point(1700, 150), 50)
        self.moon.setFill(Color.lightGray)
        self.moon.setOutline(Color.darkGray)
        self.moon.draw(win)

class Fleet(object):
    """draws everything from the fleet"""
    def __init__(self, win):
        aircraftCarrier1 = AircraftCarrier(400, 550, "Gray", "Gray3", win)
        aircraftCarrier2 = AircraftCarrier(600, 700, "Gray", "Gray3", win)
        aircraftCarrier3 = SuperAircraftCarrier(1300, 600, "Gray", "Gray3", win)

class AircraftCarrier(object):
    """Draws an aircraft carrier and it's squadron"""
    def __init__(self, x, y, color, outline, win):
        self.drawAircraftCarrier(x, y, color, outline, win)
        airplane1 = Airplane(x, y, 25, 0, Color.darkGray, "Black", win)
        airplane2 = SuperAirplane(x, y, 250, -300, Color.darkGray, "Black", win)
        airplane3 = SuperAirplane(x, y, -200, -400, Color.darkGray, "Black", win)
        personnel1 = Personnel(x, y, 300, -30, Color.lightTan, Color.darkGray1, "Blue4", "Black", win)
        personnel2 = Personnel(x, y, 320, -40, Color.tan, Color.darkGray1, "Blue4", "Black", win)
        personnel3 = Personnel(x, y, 280, -50, Color.darkTan, Color.darkGray1, "Blue4", "Black", win)
        personnel4 = Personnel(x, y, 275, -35, Color.lightTan, Color.darkGray1, "Blue4", "Black", win)
        personnel5 = Personnel(x, y, 240, -40, Color.tan, Color.darkGray1, "Blue4", "Black", win)
        personnel6 = Personnel(x, y, 220, -50, Color.darkTan, Color.darkGray1, "Blue4", "Black", win)
        personnel7 = Personnel(x, y, 230, -30, Color.tan, Color.darkGray1, "Blue4", "Black", win)
        captain = Captain(x, y, 260, -30, Color.lightTan, Color.darkGray1, "Blue4", "Black", win)
        boat1 = Boat(x, y, -200, 100, "Gray", "Gray3", win)
        boat2 = SuperBoat(x, y, -300, 200, "Gray", "Gray3", win)

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

class SuperAircraftCarrier(AircraftCarrier):
    """Includes a tank"""
    def __init__(self, x, y, color, outline, win):
        self.drawAircraftCarrier(x, y, color, outline, win)
        airplane1 = Airplane(x, y, 25, 0, Color.darkGray, "Black", win)
        airplane2 = SuperAirplane(x, y, 250, -300, Color.darkGray, "Black", win)
        airplane3 = SuperAirplane(x, y, -200, -400, Color.darkGray, "Black", win)
        personnel1 = Personnel(x, y, 300, -30, Color.lightTan, Color.darkGray1, "Blue4", "Black", win)
        personnel2 = Personnel(x, y, 320, -40, Color.tan, Color.darkGray1, "Blue4", "Black", win)
        personnel3 = Personnel(x, y, 280, -50, Color.darkTan, Color.darkGray1, "Blue4", "Black", win)
        personnel4 = Personnel(x, y, 275, -35, Color.lightTan, Color.darkGray1, "Blue4", "Black", win)
        personnel5 = Personnel(x, y, 240, -40, Color.tan, Color.darkGray1, "Blue4", "Black", win)
        personnel6 = Personnel(x, y, 220, -50, Color.darkTan, Color.darkGray1, "Blue4", "Black", win)
        personnel7 = Personnel(x, y, 230, -30, Color.tan, Color.darkGray1, "Blue4", "Black", win)
        captain = Captain(x, y, 260, -30, Color.lightTan, Color.darkGray1, "Blue4", "Black", win)
        boat1 = Boat(x, y, -200, 100, "Gray", "Gray3", win)
        boat2 = SuperBoat(x, y, -300, 200, "Gray", "Gray3", win)
        tank1 = Tank(x, y, 350, -30, Color.lightGray, Color.darkGray, win)
        tank2 = Tank(x, y, 375, -5, Color.lightGray, Color.darkGray, win)

    def drawAircraftCarrier(self, x, y, color, outline, win):
        ship = Polygon(Point(x, y), Point(x + 112, y - 37), Point(x + 450, y - 30), Point(x + 525, y + 15),
                       Point(x + 510, y + 120), Point(x + 150, y + 150))
        ship.setFill(color)
        ship.setOutline(outline)
        ship.draw(win)
        shipBase = Polygon(Point(x, y), Point(x + 112, y - 37), Point(x + 450, y - 30), Point(x + 525, y + 15),
                           Point(x + 150, y + 30))
        shipBase.setFill(color)
        shipBase.setOutline(outline)
        shipBase.draw(win)
        line = Line(Point(x + 150, y + 150), Point(x + 150, y + 30))
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
        self.drawFlames(X, Y, x, y, win)
        super().__init__(X, Y, x, y, mainColor, outline, win)
        self.drawStar(X, Y, x, y, win)

    def drawStar(self, X, Y, x, y, win):
        star = Polygon(Point(X + x + 60, Y + y - 9), Point(X + x + 62, Y + y - 4), Point(X + x + 68, Y + y + - 4), Point(X + x + 64, Y + y),
                       Point(X + x + 65, Y + y + 5), Point(X + x + 60, Y + y + 2), Point(X + x + 55, Y + y + 5), Point(X + x + 56, Y + y),
                       Point(X + x + 52, Y + y - 4), Point(X + x + 58, Y + y - 4))
        star.setFill("Red")
        star.setOutline("Black")
        star.draw(win)

    def drawFlames(self, X, Y, x, y, win):
        flames = Polygon(Point(X + x + 150, Y + y - 15), Point(X + x + 165, Y + y - 20), Point(X + x + 160, Y + y - 12), Point(X + x + 175, Y + y - 15),
                         Point(X + x + 165, Y + y - 5), Point(X + x + 180, Y + y), Point(X + x + 158, Y + y))
        flames.setFill("Red")
        flames.setOutline("Orange")
        flames.draw(win)

class Personnel(object):
    """draws personnel"""
    def __init__(self, X, Y, x, y, skinColor, uniformColor, pantsColor, outline, win):
        self.drawPersonnel(X, Y, x, y, skinColor, uniformColor, pantsColor, outline, win)

    def drawPersonnel(self, X, Y, x, y, skinColor, uniformColor, pantsColor, outline, win):
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

class Captain(Personnel):
    """draws the captain"""
    def __init__(self, X, Y, x, y, skinColor, uniformColor, pantsColor, outline, win):
        super().__init__(X, Y, x, y, skinColor, uniformColor, pantsColor, outline, win)
        self.drawHat(X, Y, x, y, uniformColor, outline, win)

    def drawHat(self, X, Y, x, y, uniformColor, outline, win):
        hat = Polygon(Point(X + x - 5, Y + y - 7), Point(X + x + 5, Y + y - 7), Point(X + x + 4, Y + y - 3), Point(X + x - 4, Y + y - 3))
        hat.setFill(uniformColor)
        hat.setOutline(outline)
        hat.draw(win)

class Boat(object):
    """draws a boat"""
    def __init__(self, X, Y, x, y, color, outline, win):
        self.drawBoat(X, Y, x, y, color, outline, win)
        personnel1 = Personnel(X + x, Y + y, 65, -40, Color.tan, Color.darkGray1, "Blue4", "Black", win)
        personnel2 = Personnel(X + x, Y + y, 80, -35, Color.darkTan, Color.darkGray1, "Blue4", "Black", win)
        personnel3 = Personnel(X + x, Y + y, 110, -43, Color.lightTan, Color.darkGray1, "Blue4", "Black", win)
        captain = Captain(X + x, Y + y, 140, -40, Color.lightTan, Color.darkGray1, "Blue4", "Black", win)

    def drawBoat(self, X, Y, x, y, color, outline, win):
        ship = Polygon(Point(X + x, Y + y), Point(X + x + 37, Y + y - 12), Point(X + x + 150, Y + y - 10), Point(X + x + 175, Y + y + 5),
                       Point(X + x + 170, Y + y + 40), Point(X + x + 50, Y + y + 50))
        ship.setFill(color)
        ship.setOutline(outline)
        ship.draw(win)
        shipBase = Polygon(Point(X + x, Y + y), Point(X + x + 37, Y + y - 12), Point(X + x + 150, Y + y - 10), Point(X + x + 175, Y + y + 5),
                           Point(X + x + 50, Y + y + 10))
        shipBase.setFill(color)
        shipBase.setOutline(outline)
        shipBase.draw(win)
        line = Line(Point(X + x + 50, Y + y + 50), Point(X + x + 50, Y + y + 10))
        line.setOutline(outline)
        line.draw(win)

class SuperBoat(Boat):
    """draws a boat with extra detail"""
    def __init__(self, X, Y, x, y, color, outline, win):
        super().__init__(X, Y, x, y, color, outline, win)
        self.drawStar(X, Y, x, y, win)

    def drawStar(self, X, Y, x, y, win):
        star = Polygon(Point(X + x + 70, Y + y + 12), Point(X + x + 74, Y + y + 22), Point(X + x + 86, Y + y + 22), Point(X + x + 78, Y + y + 30),
                       Point(X + x + 80, Y + y + 40), Point(X + x + 70, Y + y + 34), Point(X + x + 60, Y + y + 40), Point(X + x + 62, Y + y + 30),
                       Point(X + x + 54, Y + y + 22), Point(X + x + 66, Y + y + 22))
        star.setFill("Red")
        star.setOutline("Black")
        star.draw(win)

class Tank(object):
    """draws a tank"""
    TANKS = []
    def __init__(self, X, Y, x, y, color, outline, win):
        personnel1 = Personnel(X + x, Y + y, 65, -55, Color.lightTan, Color.darkGray1, "Blue4", "Black", win)
        self.rect = None
        self.rect1 = None
        self.circ = None
        self.circ1 = None
        self.line = None
        self.cannon = None
        self.turret = None
        self.body = None
        self.fire = None
        self.drawTreds(X, Y, x, y, color, outline, win)
        self.drawCannon(X, Y, x, y, color, outline, win)
        self.drawBody(X, Y, x, y, color, outline, win)
        self.drawFire(X, Y, x, y, win)
        Tank.TANKS.append(self)

    def drawTreds(self, X, Y, x, y, color, outline, win):
        self.rect = Rectangle(Point(X + x, Y + y - 5), Point(X + x + 96, Y + y))
        self.rect.setFill(color)
        self.rect.setOutline(outline)
        self.rect.draw(win)
        self.rect1 = Rectangle(Point(X + x, Y + y), Point(X + x + 96, Y + y + 15))
        self.rect1.setFill("Black")
        self.rect1.setOutline("Black")
        self.rect1.draw(win)
        self.circ = Circle(Point(X + x, Y + y + 8), 7)
        self.circ.setFill("Black")
        self.circ.setOutline("Black")
        self.circ.draw(win)
        self.circ1 = Circle(Point(X + x + 96, Y + y + 8), 7)
        self.circ1.setFill("Black")
        self.circ1.setOutline("Black")
        self.circ1.draw(win)
        for i in range(9):
            self.circ = Circle(Point(X + x + i * 12, Y + y + 8), 6)
            self.circ.setFill(outline)
            self.circ.setOutline("Black")
            self.circ.draw(win)
        self.line = Line(Point(X + x, Y + y + 8), Point(X + x + 96, Y + y + 8))
        self.line.setOutline(color)
        self.line.setWidth(2)
        self.line.draw(win)

    def drawCannon(self, X, Y, x, y, color, outline, win):
        self.cannon = Polygon(Point(X + x + 50, Y + y - 25), Point(X + x + 50, Y + y - 35), Point(X + x - 10, Y + y - 33), Point(X + x - 10, Y + y - 27))
        self.cannon.setFill(Color.darkGray)
        self.cannon.setOutline(outline)
        self.cannon.draw(win)
        self.turret = Polygon(Point(X + x + 30, Y + y - 15), Point(X + x + 50, Y + y - 40), Point(X + x + 80, Y + y - 40), Point(X + x + 90, Y + y - 15))
        self.turret.setFill(color)
        self.turret.setOutline(outline)
        self.turret.draw(win)

    def drawBody(self, X, Y, x, y, color, outline, win):
        self.body = Polygon(Point(X + x - 10, Y + y - 5), Point(X + x + 106, Y + y - 5), Point(X + x + 96, Y + y - 15), Point(X + x, Y + y - 15), )
        self.body.setFill(color)
        self.body.setOutline(outline)
        self.body.draw(win)

    def drawFire(self, X, Y, x, y, win):
        self.fire = Polygon(Point(X + x - 10, Y + y - 33), Point(X + x - 10, Y + y - 27), Point(X + x - 20, Y + y - 10), Point(X + x - 17, Y + y - 25), Point(X + x - 30, Y + y - 30), Point(X + x - 17, Y + y - 35), Point(X + x - 20, Y + y - 50))
        self.fire.setFill("Red")
        self.fire.setOutline("Orange")

class SuperTank(Tank):
    """draws the ultimate tank"""
    def __init__(self, X, Y, x, y, color, outline, win):
        super().__init__(X, Y, x, y, color, outline, win)
        self.drawStar(X, Y, x, y, win)

    def drawStar(self, X, Y, x, y, win):
        star = Polygon(Point(X + x + 63, Y + y - 36), Point(X + x + 67, Y + y - 26), Point(X + x + 79, Y + y - 26),
                       Point(X + x + 71, Y + y - 18), Point(X + x + 73, Y + y - 8), Point(X + x + 63, Y + y - 14),
                       Point(X + x + 53, Y + y - 8), Point(X + x + 55, Y + y - 18), Point(X + x + 47, Y + y - 26),
                       Point(X + x + 59, Y + y - 26))
        star.setFill("Red")
        star.setOutline("Black")
        star.draw(win)

class Nuke(object):
    """drops a nuke"""
    xValue = 0
    def __init__(self, win):
        self.nuke1 = None
        self.rocket = None
        self.rect = None
        self.rect1 = None
        self.rect2 = None
        self.rightWing = None
        self.leftWing = None
        self.x = Nuke.xValue
        self.y = -25
        self.drawNuke(win)

    def drawNuke(self, win):
        self.nuke1 = Polygon(Point(self.x, self.y), Point(self.x - 15, self.y - 50), Point(self.x - 20, self.y - 100), Point(self.x + 20, self.y - 100), Point(self.x + 15, self.y - 50))
        self.nuke1.setFill("Red4")
        self.nuke1.setOutline("Black")
        self.nuke1.draw(win)
        self.rocket = Rectangle(Point(self.x - 20, self.y - 300), Point(self.x + 20, self.y - 100))
        self.rocket.setFill(Color.darkGray)
        self.rocket.setOutline("Black")
        self.rocket.draw(win)
        self.rect = Rectangle(Point(self.x - 15, self.y - 290), Point(self.x - 6, self.y - 110))
        self.rect.setFill("Red")
        self.rect.setOutline("Red")
        self.rect.draw(win)
        self.rect1 = Rectangle(Point(self.x - 5, self.y - 290), Point(self.x + 4, self.y - 110))
        self.rect1.setFill("Blue")
        self.rect1.setOutline("Blue")
        self.rect1.draw(win)
        self.rect2 = Rectangle(Point(self.x + 5, self.y - 290), Point(self.x + 15, self.y - 110))
        self.rect2.setFill("White")
        self.rect2.setOutline("White")
        self.rect2.draw(win)
        self.rightWing = Polygon(Point(self.x - 21, self.y - 300), Point(self.x - 21, self.y - 250), Point(self.x - 35, self.y - 300), Point(self.x - 40, self.y - 350))
        self.rightWing.setFill("Red")
        self.rightWing.setOutline("Black")
        self.rightWing.draw(win)
        self.leftWing = Polygon(Point(self.x + 21, self.y - 300), Point(self.x + 21, self.y - 250), Point(self.x + 35, self.y - 300), Point(self.x + 40, self.y - 350))
        self.leftWing.setFill("Red")
        self.leftWing.setOutline("Black")
        self.leftWing.draw(win)

    def dropNuke(self):
        self.nuke1.move(0, 50)
        self.rocket.move(0, 50)
        self.rect.move(0, 50)
        self.rect1.move(0, 50)
        self.rect2.move(0, 50)
        self.rightWing.move(0, 50)
        self.leftWing.move(0, 50)
        time.sleep(.05)

class Color(object):
    """Holds colors"""
    lightGray = color_rgb(121, 121, 121)
    darkGray = color_rgb(80, 80, 80)
    darkGray1 = color_rgb(40, 40, 40)
    lightTan = color_rgb(246, 235, 204)
    tan = color_rgb(218, 193, 125)
    darkTan = color_rgb(97, 48, 0)
    darkBlue = color_rgb(0, 0, 80)

class TimeOfDay(object):
    """has day, night, and war"""

    @staticmethod
    def war(win, click):
        if click:
            click = True
            Time = 0
            while Time < 8 and click:
                win.setBackground(color_rgb(random.randrange(255), random.randrange(255), random.randrange(255)))
                if random.randrange(5) == 0:
                    index = random.randrange(len(Tank.TANKS))
                    Tank.TANKS[index].fire.draw(win)
                    time.sleep(.1)
                    Tank.TANKS[index].fire.undraw()
                coordinate = win.checkMouse()
                if coordinate is None:
                    time.sleep(.05)
                    Time += .05
                else:
                    #click = False
                    Nuke.xValue = coordinate.x
                    nuke = Nuke(win)
                    for i in range(20):
                        nuke.dropNuke()
                    Time += 1
        return click

    @staticmethod
    def day(win, window, click):
        if click:
            win.setBackground("Cyan")
            window.water1.moon.undraw()
            window.water1.drawSun(win)
            window.water1.water.setFill("Blue")
            window.water1.water.setOutline("Blue")
            click = TimeOfDay.clicked(win)
        return click

    @staticmethod
    def night(win, window, click):
        if click:
            win.setBackground(Color.darkBlue)
            window.water1.sun.undraw()
            window.water1.drawMoon(win)
            window.water1.water.setFill("Blue4")
            window.water1.water.setOutline("Blue4")
            click = TimeOfDay.clicked(win)
        return click

    @staticmethod
    def clicked(win):
        click = True
        Time = 0
        while Time < 10 and click:
            coordinate = win.checkMouse()
            if coordinate is None:
                time.sleep(.05)
                Time += .05
            else:
                #click = False
                Nuke.xValue = coordinate.x
                nuke = Nuke(win)
                for i in range(20):
                    nuke.dropNuke()
                Time += 1
        return click

def main():
    win = GraphWin("Fleet", 1900, 1040) #fits my window at home, change if nessasary
    win.setBackground("Cyan")
    window = Window(win)
    click = TimeOfDay.clicked(win)
    while click:
        click = TimeOfDay.war(win, click)
        click = TimeOfDay.night(win, window, click)
        click = TimeOfDay.war(win, click)
        click = TimeOfDay.day(win, window, click)
    win.close()

main()
