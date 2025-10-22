# Reto-03---POO
Desarrollo del ejercicio del reto 03:

## Reto 5: 
1. Crea un paquete con todo el código de la clase *Shape*, este ejercicio debe realizarse de dos maneras:
 - Un módulo único dentro del paquete *Shape*.
 - Los módulos individuales que importan *Shape* heredan de él.

## Forma #1:
En este primer paquete se crearon 3 módulos; el primero "shapes.py" donde se escuentra todo el codigo base de las clases, "main.py" en el que están los casos de prueba, y por último el "__init__.py", que en este
caso se encuentra vacío.

La jerarquía luce de esta manera:
```sh
Reto 05/
└── Forma #1/
    └── Shape/
        ├── __init__.py       # vacío
        ├── shapes.py         # Contiene TODAS las clases: Point, Line, Shape, Rectangle, Triangle, etc.
        └── main.py           # Contiene los casos de prueba
```

Y se debe ejecutar en la terminal:
```sh
python -m Shape.main
```

## Forma #2:
En este segundo paquete se generaron varios módulos; el principal "shape.py" que contiene la clase *Shape*, luego están "line.py" y "point.py" que contienen el codigo de la clase que le corresponde a cada uno; luego,
estan los módulos "rectangle.py", "square.py" y "triangle.py" que heredan de *Shape*. Por último, tenemos el "main.py" donde están los casos de prueba, y el "__init__.py" que en este caso contiene las exportaciones
de las clases correspondientes, para permitir una mejor ejecución.

La jerarquía luce de esta manera:
```sh
Reto 05/
└── Forma #2/
    └── Shape/
        ├── __init__.py          # Importa clases clave
        ├── point.py             # Clase Point
        ├── line.py              # Clase Line
        ├── shape.py             # Clase base Shape
        ├── rectangle.py         # Clase Rectangle hereda de Shape
        ├── square.py            # Clase Square hereda de Rectangle
        ├── triangle.py          # Clase Triangle hereda de Shape
        └── main.py              # Casos de prueba
```

Y se debe ejecutar en la terminal:
```sh
python -m Shape.main"
```

Pd: Adjunto las carpetas con los paquetes y modulos correspondientes para no saturar de texto y codigo el README.
