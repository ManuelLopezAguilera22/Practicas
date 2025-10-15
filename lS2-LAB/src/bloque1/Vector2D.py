from __future__ import annotations
from dataclasses import dataclass
from math import sqrt, atan2

@dataclass (frozen=False, order=True)
class Vector2D:
    x: float
    y: float
    
    
    @staticmethod
    def of(x: float, y: float) -> Vector2D:
        return Vector2D(x, y)



    @staticmethod
    def parse(txt: str)-> Vector2D:
        x, y = txt.split(',')
        txt=txt[1:-1]
        return Vector2D(float(x), float(y))
   
    
    @property
    def module(self):
        return sqrt(self.x**2 + self.y**2)


    @property
    def angulo(self):
        return atan2(self.y, self.x)
    @property
    def copy(self):
        return Vector2D(self.x, self.y)
    @property
    def ortogonal(self):
        return Vector2D.of(-self.y, self.x)
    
    @property
    def unitario(self):
        return Vector2D.of(self.x / self.module, self.y / self.module)

if __name__ == "__main__":
    v1= Vector2D.of(3,7)
    print(v1)
    v1= Vector2D.of(3,4)
    print(v1)
    v2= Vector2D.of(1,2)
    print(v2)
    print("hola")
    print(Vector2D.of(1,7))
    print(Vector2D.parse("3.5,4.2"))
    print(Vector2D.of(3,4).module)
    print(Vector2D.of(1,1).angulo)
    print(Vector2D.of(45,1.5).copy)
    print(Vector2D.of(1,2).ortogonal)
    print(Vector2D.of(3,4).unitario)