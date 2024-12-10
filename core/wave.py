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

