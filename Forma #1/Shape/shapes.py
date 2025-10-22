import math

class Point:
    def __init__(self, x: float, y: float):
        self.x = x
        self.y = y
    
    def compute_distance(self, point):
        #Fórmula de la distancia Euclidiana
        return math.sqrt((self.x - point.x)**2 + (self.y - point.y)**2)


class Line:
    def __init__(self, start_point: Point, end_point: Point):
        self.start_point = start_point
        self.end_point = end_point
        self.length = start_point.compute_distance(end_point)


class Shape:
    def __init__(self, vertices: list):
        self.vertices = vertices
        self.is_regular = False
        self.edges = self.make_edges()
        self.inner_angles = []

    def make_edges(self):
        edges = []
        for i in range(len(self.vertices)):
            start = self.vertices[i]
            end = self.vertices[(i + 1) % len(self.vertices)]  #Conecta el último con el primero
            edges.append(Line(start, end))
        return edges

    def compute_area(self):
        raise NotImplementedError("Define el método en la subclase.")
    
    def compute_perimeter(self):
        perimeter = 0
        for edge in self.edges:
            perimeter += edge.length
        return perimeter
    
    def compute_inner_angles(self):
        raise NotImplementedError("Define el método en la subclase.")


class Rectangle(Shape):
    def __init__(self, vertices):
        super().__init__(vertices)
        self.is_regular = True
        
    def compute_area(self):
        base = self.edges[0].length
        height = self.edges[1].length
        return base * height

    def compute_inner_angles(self):
        return [90.0, 90.0, 90.0, 90.0]


class Square(Rectangle):
    def __init__(self, vertices):
        super().__init__(vertices)
        self.is_regular = True


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

