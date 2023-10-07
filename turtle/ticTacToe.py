import turtle


class Board(turtle.Turtle):
    def __init__(self, shape: str = "classic", undobuffersize: int = 1000,
                 visible: bool = False) -> None:
        super().__init__(shape, undobuffersize, visible)
        turtle.setworldcoordinates(0, 100, 100, 0)
        self.hideturtle()
        self.up()
        self.goto(10, 33)
        self.down()
        self.goto(90, 33)
        self.up()
        self.goto(10, 66)
        self.down()
        self.goto(90, 66)
        self.up()
        self.goto(33, 10)
        self.down()
        self.goto(33, 90)
        self.up()
        self.goto(66, 10)
        self.down()
        self.goto(66, 90)
