
class shape():
    def __init__(self):
        #self.shape = shape
        self.shape = str(input("Which SHAPE do you want, circle or rectangle?  : "))
        #return self.shape
    def draw(self):
        return

class circle(shape):
    def draw(self):
        print("Which TYPE of circle 1 or 2? : ")

class rectangle(shape):
    def draw(self):
        print("Which TYPE of rectangle 1 or 2? : ")

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

class DP1(v1Circle,v1Rectangle):
    drawline(v1Rectangle)
    drawcircle(v1Circle)

class DP2(v2Circle,v2Rectangle):
    drawline(v2Rectangle)
    drawcircle(v2Circle)




#def circle():
    #type_circle = int(input("Which type circle 1 or 2? : "))
    #return type_circle

#def draw(type_circle):
    #if shape() == 1:
        #print("Draw circle with Type 1 method")
    #else:
     #   print("Draw circle with Type 2 method")
#type_rectangle = int(input("Which type rectange 1 or 2"))
#if type_rectangle == 1:
    #print("Draw rectangle with Tpye 1 method")
#else:
    #print("Draw rectangle with Tpye 2 method")


circle()


