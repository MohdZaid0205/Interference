from core.grid import Grid
from core.particle import Particle
from core.wave import WaveEquation, WaveSourceEmitter

from typing import Callable, Generator


class Interference:

    def __init__(self, grid:Grid[Particle], sources:list[WaveSourceEmitter]) -> None:
        self.grid = grid
        self.sorc = sources

    def __iter__[T](self, provider:Callable[[Particle], T]=None) -> Generator[T, None, None]:
        for i in range(self.grid.m):
            for j in range(self.grid.n):
                yield (i, j, self.grid.get(i, j, provider))
    
    def update(self, time:float) -> None:
        for i in range(self.grid.m):
            for j in range(self.grid.n):
                particle = self.grid.get(i, j)
                if particle is None:
                    continue
                particle.d = 0
                for source in self.sorc:
                    particle.d += source.calculateDisplacement(particle.P, time)
        ...