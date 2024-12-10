from dataclasses import dataclass
from math import sqrt


@dataclass
class Vector2D:
    x : int     # Horizontal Component of screen
    y : int     # Vertical Component of screen
    
    @staticmethod
    def distance( v1:'Vector2D', v2:'Vector2D') -> float:
        return sqrt( (v1.x-v2.x)**2 + (v1.y-v2.y)**2)
    