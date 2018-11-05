
class shape():
    def __init__(self,type):
        self.type = type
        
    def draw(self):
        pass

class circle(shape):
    def draw(self,type):
        print("Drawing the Circle...!")

class rectangle(shape):
    def draw(self, rectangle):
        print("Drawing the Rectangle...!")

class v1Rectangle(rectangle):
    def drawline(self):
        print("Method 1 drawing rectangle")

class v2Rectangle(rectangle):
    def drawline(self):
        print("Method 2 drawing rectangle")

class v1Circle(circle):
    def drawcircle(self):
        print("Method 1 drawing circle")

class v2Circle(circle):
    def drawcircle(self):
        print("Method 2 drawing circle")

class DP1(self,v1Circle,v1Rectangle):
    self.drawline(v1Rectangle)
    self.drawcircle(v1Circle)

class DP2(v2Circle,v2Rectangle):
    self.drawline(v2Rectangle)
    self.drawcircle(v2Circle)


if __name__ == '__main__':

    DP = str(input("What design pattern is requested: "))
    if DP == 'DP1'
        DP1()
    else:
        DP2()


