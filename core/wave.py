from dataclasses import dataclass
from typing import Literal

COS_WAVE:str = "COS_WAVE"
SIN_WAVE:str = "SIN_WAVE"


@dataclass
class WaveEquation:
    A : float       # Maximum displacement of the wave
    k : float       # Spatial frequency (k)
    w : float       # Rotational speed (ω)
    q : float       # Starting phase of the wave (ϕ)
    t : Literal["COS_WAVE", "SIN_WAVE"] # type


class WaveSourceEmitter:
    P : ...             # Position of wave emitter
    W : WaveEquation    # Equation of wave to emit
    d : float           # intensity falloff

    def calculateDisplacement(self, at:...) -> float:
        ...

    def calculateIntensity(self, at:...) -> float:
        ...
