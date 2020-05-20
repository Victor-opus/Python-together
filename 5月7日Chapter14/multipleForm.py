#coding:utf-8
#多态 polymorphism 不同类具有同名函数，它们有不同的行为（可相同）
class Triangle:
    def __init__(self,width,height):
        self.width = width
        self.height = height

    def getArea(self):
        area = self.width * self.height / 2.0
        return area

class Square:
    def __init__(self,size):
        self.size = size

    def getArea(self):
        area = self.size * self.size
        return area

myTriangle = Triangle(4,5)
mySquare = Square(7)
print myTriangle.getArea()
print mySquare.getArea()
