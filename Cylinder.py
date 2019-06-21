import math
class Cylinder:

    def __init__(self,height=1,radius=1):
        self.height= height
        self.radius= radius

    def volume(self):
        return (self.radius ** 2) * math.pi * self.height

    def surface_area(self):
        return (2 * math.pi * self.radius * self.height) + ((self.radius ** 2) *2*math.pi)

c = Cylinder(2,3)
print("The Volume is %s "%(c.volume()))
print("The area is %s "%(c.surface_area()))
