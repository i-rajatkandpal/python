
from abc import ABC,abstractmethod
class Shape():
    @abstractmethod
    def area(self):
        pass


class circle(Shape):
    def __init__(self,radius):
        self.radius = radius

    def area(self):
        return 3.14 * self.radius ** 2
    
class square(Shape):
    def __init__(self,side):
        self.side = side
#ji
    def area(self):
        return 3.14 * self.side ** 2
    
class pizza(circle):
    def __init__(self, toppings ,radius):
        super().__init__(radius)
        self.toppings = toppings
    




    
shapes = [circle(4),square(5),pizza("peperoni",15)]

for shape in shapes:
    print(f"{shape.area()}cm²")

        