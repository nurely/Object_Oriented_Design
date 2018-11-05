class shape():
    types = ""

    def __init__(self, types=None):
        self.types = types

    def draw(self):
        pass


class circle(shape):
    def __init__(self, types=None):
        super().__init__()
        self.types = types

    def draw(self):
        print("Drawing the Circle...!")


class rectangle(shape):
    def __init__(self, types=None):
        super().__init__()
        self.types = types

    def draw(self):
        print("Drawing the Rectangle...!")


class v1Rectangle(rectangle):
    def __init__(self,):
        super().__init__()
        self.types = "rectangle"

    def drawline(self):
        print("Method 1 drawing rectangle")


class v2Rectangle(rectangle):
    def __init__(self):
        super().__init__()
        self.types= "rectangle"

    def drawline(self):
        print("Method 2 drawing rectangle")


class v1Circle(circle):
    def __init__(self):
        super().__init__()
        self.types = "circle"

    def drawcircle(self):
        print("Method 1 drawing circle")


class v2Circle(circle):
    def __init__(self):
        super().__init__()
        self.types = "circle"

    def drawcircle(self):
        print("Method 2 drawing circle")


class DP1(v1Circle, v1Rectangle):
    def __init__(self):
        super().__init__()
        self.drawline()
        self.drawcircle()


class DP2(v2Circle, v2Rectangle):
    def __init__(self):
        super().__init__()
        self.drawline()
        self.drawcircle()


if __name__ == '__main__':

    DP = str(input("What design pattern is requested: "))
    if DP == 'DP1':
        DP1()
    else:
        DP2()
