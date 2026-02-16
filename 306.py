class Shape:
    def area(self):
        return 0
class Rectangle(Shape):
    def __init__(self,l,w):
        self.l = l
        self.w = w
    def area(self):
        print(self.l * self.w)

l,w = map(int, input().split())
a = Rectangle(l,w)
a.area()
