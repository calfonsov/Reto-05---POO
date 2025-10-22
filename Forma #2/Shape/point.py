import math

class Point:
    def __init__(self, x: float, y: float):
        self.x = x
        self.y = y
    
    def compute_distance(self, point):
        #Fórmula de la distancia Euclidiana
        return math.sqrt((self.x - point.x)**2 + (self.y - point.y)**2)
