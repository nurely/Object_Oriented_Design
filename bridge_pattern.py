

class shape():
    def __init__(self,types):
        self.types = types
        
    def draw(self):
        pass

class circle(shape):
    def draw(self,types):
        print("Drawing the Circle...!")

class rectangle(shape):
    def draw(self, types):
        print("Drawing the Rectangle...!")

class v1Rectangle(rectangle):
    def __init__(self):
        super().__init__(types = rectangle)
    def drawline(self):
        print("Method 1 drawing rectangle")

class v2Rectangle(rectangle):
    def __init__(self):
        super().__init__(types = rectangle)
    def drawline(self):
        print("Method 2 drawing rectangle")

class v1Circle(circle):
    def __init__(self):
        super().__init__(types = circle)
    def drawcircle(self):
        print("Method 1 drawing circle")

class v2Circle(circle):
    def __init__(self):
        super().__init__(types = circle)
    def drawcircle(self):
        print("Method 2 drawing circle")


class DP1(v1Circle,v1Rectangle):
    def __init__(self,v1Circle,v1Rectangle):
        super().__init__(v1Circle,v1Rectangle)
        self.drawline(v1Rectangle)
        self.drawcircle(v1Circle)

class DP2(v2Circle,v2Rectangle):
    def __init__(self,v2Circle,v2Rectangle):
        super().__init__(v2Circle,v2Rectangle)

        self.drawline(v2Rectangle)
        self.drawcircle(v2Circle)


if __name__ == '__main__':

    DP = str(input("What design pattern is requested: "))
    if DP == 'DP1':
        DP1()
    else:
        DP2()
