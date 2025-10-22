from .line import Line

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

