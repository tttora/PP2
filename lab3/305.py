class Shape:
    def area(self):
        return 0
class Square(Shape):
    def __init__(self,l):
        self.l = l
    def area(self):
        print(self.l**2)

a = Square(int(input()))
a.area()


