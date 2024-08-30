from random import randint
from math import sqrt,ceil

class Point2D:
    "Définition d'un point dans l'espace 2D"
    def __init__(self,x,y,name=None):
        self.name = name
        self.pos = {"x": x, "y": y}

    def distance(self,target):
        return sqrt(pow(target.pos["x"]-self.pos["x"],2)+pow(target.pos["y"]-self.pos["y"],2))
    #Test si les maisons sont stackées dans un rayon de au moins 3 de distance
    def is_stack(self, *point):
        points_dist = []
        stacked = []
        for i in range(len(point)):
            if self != point[i]:
                points_dist.append(self.distance(point[i]))
                                   
        for dist in points_dist:
            stacked.append(ceil(dist) <= 3)

        return stacked.count(True) > 0, stacked.count(True)

    def move(self,x,y,mode="move"):
        if mode.lower() == "move":
            self.pos["x"]+=x
            self.pos["y"]+=y
        elif mode.lower() == "set":
            self.pos["x"] = x 
            self.pos["y"] = y

    @classmethod
    def translate(cls,dx,dy,point):
        return cls(point.pos["x"]+dx,point.pos["y"]+dy,point.name+"'")


        
def get_distance(v):
    for item in v:
        _, stack_number = item.is_stack(*v)
        print(f"The point {[x for x in item.pos.values()] if item.name == None else item.name} is in range of 3 with {stack_number} other(s) point(s)") 


#randint(-3,3),randint(-3,2)
points = [
    Point2D(-1,2,"A"),
    Point2D(1,0, "B"),
    Point2D(3,1, "C"),
    Point2D(-3,4)
    ]
get_distance(points)
new_point = Point2D.translate(2,5,points[0])
_, stack_number = new_point.is_stack(*points)
print(f"The point {[x for x in new_point.pos.values()] if new_point.name == None else new_point.name} is in range of 3 with {stack_number} other(s) point(s)")
print(points[0].distance(new_point))

    
