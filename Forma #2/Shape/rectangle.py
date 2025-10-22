from .shape import Shape

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
