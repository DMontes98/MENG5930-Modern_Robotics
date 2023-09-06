import math
class Shape2D: # superclass, base class, parent class

    def __init__(self, leng = 1, wid = 1):
        print('Shape 2D, init')
        self.__len = leng
        self.__wid = wid

    def area(self):
        area = self.__len * self.__wid
        return area

    def getLen(self):
        return self.__len
    
    def getWid(self):
        return self.__wid

    def set(self, leng, wid):
        self.__len = leng
        self.__wid = wid

    def circumference(self):
        return 2*self.__len + 2*self.__wid
    
    def __str__(self):
        outputStr = 'Dimension 1 = ' + str(self.__len)
        outputStr += ' Dimension 2 = ' + str(self.__wid)
        # outputStr = str(self.__len) + ' ' + str(self.__wid)
        return outputStr

class Triangle(Shape2D): # subclass, derived class, child class
    # inherits data attributes and methods from superclass

    # add a data attribute called angle
    def __init__(self, leng = 1, wid = 1, ang = 90):
        # call superclass init method in order to set length and width
        Shape2D.__init__(self, leng, wid)
        # add angle attribute
        self.__angle = ang
        
    def setAngle(self, ang):
        self.__angle = ang
        
    def area(self):
        #area = self.getLen() * self.getWid() * 0.5
        area = Shape2D.area(self) * 0.5 # call area() from Shape class
        #area = super().area() * 0.5
        return area

    def getAngle(self):
        return self.__angle

# add a circle class
class Circle(Shape2D):

    def __init__(self, radius = 1):
        Shape2D.__init__(self, radius, 0)
        self.__name = 'pointless'

    def __str__(self):
        return self.__name + ' has radius of ' + str(self.getLen())

    def area(self):
        return math.pi * self.getLen()*self.getLen()

    def circumference(self):
        return 2*(math.pi)*(self.getLen())

def main():
    square = Shape2D(3,3)
    tri = Triangle(2,4)
    circ = Circle(5.5)
    print(circ)
    print('Circle has area of = ',circ.area())
    print(circ.circumference())
    print('Square = ',square)
    print('Square has area of = ',square.area())
    tri.setAngle(85)
    # want to change the base and height of the triangle
    tri.set(3,6) # or just use tri = Triangle(3,6)
    # change the angle of the triangle to 110
    #tri.setAngle(110)
    print('Triangle = ',tri, 'with angle = ',tri.getAngle())
    print('Area of triangle = ', tri.area()) # calls area() from Triangle class

main()
