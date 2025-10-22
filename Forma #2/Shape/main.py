from .point import Point
from .rectangle import Rectangle
from .square import Square
from .triangle import Equilateral, Isosceles, Scalene

if __name__ == "__main__":
    
#Rectángulo
    p1 = Point(0, 0)
    p2 = Point(4, 0)
    p3 = Point(4, 3)
    p4 = Point(0, 3)
    rect = Rectangle([p1, p2, p3, p4])
    print("-----Rectangulo:-----")
    print("Perímetro:", rect.compute_perimeter())
    print("Área:", rect.compute_area())
    print("Ángulos internos:", rect.compute_inner_angles())
    print("¿Es regular?:", rect.is_regular)

#Cuadrado
    q1 = Point(0,0)
    q2 = Point(4,0)
    q3 = Point(4,4,)
    q4 = Point(0,4)
    squ = Square([q1, q2, q3, q4])
    print("\n-----Cuadrado:-----")
    print("Perímetro:", squ.compute_perimeter())
    print("Área:", squ.compute_area())
    print("Ángulos internos:", squ.compute_inner_angles())
    print("¿Es regular?:", squ.is_regular)

#Triángulo equilátero
    a = Point(0, 0)
    b = Point(3, 0)
    c = Point(1.5, 2.598)  #Altura ≈ sqrt(3)/2 * 3
    equ = Equilateral([a, b, c])
    print("\n----Triángulo Equilátero:----")
    print("Perímetro:", equ.compute_perimeter())
    print("Área:", equ.compute_area())
    print("Ángulos internos:", equ.compute_inner_angles())
    print("¿Es regular?", equ.is_regular)

#Triángulo Isósceles
    i1 = Point(0,0)
    i2 = Point(4,0)
    i3 = Point(2,3)
    iso = Isosceles([i1, i2, i3])
    print("\n----Triángulo Isósceles:----")
    print("Perímetro:", iso.compute_perimeter())
    print("Área:", iso.compute_area())
    print("Ángulos internos:", iso.compute_inner_angles())
    print("¿Es regular?", iso.is_regular)

#Triángulo Escaleno
    s1 = Point(0,0)
    s2 = Point(4,0)
    s3 = Point(2,1)
    esc= Scalene([s1, s2, s3])
    print("\n----Triángulo Escaleno:----")
    print("Perímetro:", esc.compute_perimeter())
    print("Área:", esc.compute_area())
    print("Ángulos internos:", esc.compute_inner_angles())
    print("¿Es regular?", esc.is_regular)