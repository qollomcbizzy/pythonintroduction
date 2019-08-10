# naming a class we capitalize first letter of every letter i.e pascal way of naming

class Point:
    # constructor
    def __init__(self, x, y):
        self.x = x
        self.y = y

    # methods
    def move(self):
        print("move")

    def draw(self):
        print("draw")


point1 = Point(10, 20);
point1.draw()
print(point1.x)
print(point1.y )
