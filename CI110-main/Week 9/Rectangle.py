class Rectangle:
    def __init__(self, h=1, w=2):
        self.height = h
        self.width = w

    def getArea(self):
        return self.height * self.width

    def getPerimeter(self):
        return (self.height * 2) + (self.width * 2)
