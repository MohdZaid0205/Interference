from dataclasses import dataclass
from math import sin, cos
from typing import Callable

from core.vector import Vector2D

# definitions for types of waves.
COS_WAVE:str = cos
SIN_WAVE:str = sin


@dataclass
class WaveEquation:
    A : float       # Maximum displacement of the wave
    k : float       # Spatial frequency (k)
    w : float       # Rotational speed (ω)
    q : float       # Starting phase of the wave (ϕ)
    t : Callable[[float], float] # type

    def displacement(self, x:float, t:float) -> float:
        return self.A*self.t(self.w*t - self.k*x + self.q)
    
    def intensity(self, x:float) -> float:
        return (self.A**2) / x


@dataclass
class WaveSourceEmitter:
    P : Vector2D        # Position of wave emitter
    W : WaveEquation    # Equation of wave to emit
    d : float           # intensity falloff

    def calculateDisplacement(self, at:Vector2D, t:float) -> float:
        return self.W.displacement(
            x=Vector2D.distance(self.P, at),
            t=t
        )

    def calculateIntensity(self, at:Vector2D) -> float:
        return self.W.intensity(
            x=Vector2D.distance(self.P, at)
        )/self.d
