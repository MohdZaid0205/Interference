from dataclasses import dataclass

from core.vector import Vector2D


@dataclass
class Particle:
    P: Vector2D     # position in coordinate(grid).
    d: float        # current particle displacement/gridDistance
    i: float        # current intensity of particle (for dampening)
