class Shape:
    def __init__(self, base, height):
        """
        Initializes the Car object with a color and max speed.
        """
        self.base = base  
        self.height = height

    def area(self):
        print("calculating area")

    

class Triangle(Shape):
    def area(self):
        print(self.base * self.height/2)    

# How can I use this, in conjunction with "random" to only get probabilites of points within a shape?

class OriginBasedShape:
    """
    This is only for regular polygons centered around the origin.
    """
    def __init__(self, apothem):
        self.apothem = apothem 
    
    def generate_point():
        
    
triangle = Triangle(3, 4)
triangle.area()