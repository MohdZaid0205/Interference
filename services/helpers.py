from core.grid import Grid
from core.particle import Particle
from core.vector import Vector2D
from core.wave import WaveEquation, WaveSourceEmitter

def iGridInitHelper(m:int, n:int, sources:list[WaveSourceEmitter]) -> Grid:
    _grid:Grid[Particle] = Grid[Particle](m, n)
    for i in range(m):
        for j in range(n):

            net_position = Vector2D(i, j)
            net_displacement = 0
            net_intensity = 0

            for source in sources:
                net_displacement += source.calculateDisplacement(at=net_position, t=0)
                net_intensity += source.calculateIntensity(at=net_position, t=0)

            particle:Particle = Particle(net_position,net_displacement,net_intensity)
            _grid.set(i, j, particle)
    return _grid


def iSourceInitHelper():...
