import math
from .shape import Shape

class Triangle(Shape):
    def __init__(self, vertices):
        super().__init__(vertices)
        self.inner_angles = self.compute_inner_angles()
    
    def compute_area(self):
        #Fórmula de Herón
        a, b, c = [edge.length for edge in self.edges]
        s = (a + b + c) / 2
        return math.sqrt(s * (s - a) * (s - b) * (s - c))
    
    def compute_inner_angles(self):
        #Teorema del Coseno
        a, b, c = [edge.length for edge in self.edges]
        A = math.degrees(math.acos((b**2 + c**2 - a**2) / (2 * b * c)))
        B = math.degrees(math.acos((a**2 + c**2 - b**2) / (2 * a * c)))
        C = 180 - (A + B)
        return [A, B, C]


class Equilateral(Triangle):
    def __init__(self, vertices):
        super().__init__(vertices)
        self.is_regular = all(abs(e1.length - e2.length) < 1e-6 for e1 in self.edges for e2 in self.edges)


class Isosceles(Triangle):
    def __init__(self, vertices):
        super().__init__(vertices)
        lengths = [round(edge.length, 3) for edge in self.edges]
        self.is_regular = len(set(lengths)) <= 2


class Scalene(Triangle):
    def __init__(self, vertices):
        super().__init__(vertices)
        lengths = [round(edge.length, 3) for edge in self.edges]
        self.is_regular = len(set(lengths)) == 3

