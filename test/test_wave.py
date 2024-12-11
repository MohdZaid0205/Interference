from core.vector import Vector2D  # Assuming this is already implemented
from core.wave import WaveEquation, WaveSourceEmitter, COS_WAVE, SIN_WAVE

from math import sin, cos, pi
import pytest


class TestWaveEquation:

    @pytest.mark.parametrize(
        "A, k, w, q, t_func, x, t, expected_displacement",
        [
            (1.0, 2.0, pi    , 0.0   , SIN_WAVE, 0.0, 1.0, sin(pi)),  # Basic sine wave
            (1.0, 0.0, 0.0   , 0.0   , COS_WAVE, 0.0, 0.0, 1.0    ),  # Static wave
        ]
    )
    def test_displacement(self, A, k, w, q, t_func, x, t, expected_displacement):
        wave = WaveEquation(A=A, k=k, w=w, q=q, t=t_func)
        displacement = wave.displacement(x, t)
        assert abs(displacement - expected_displacement) < 1e-9, \
            f"Expected displacement={expected_displacement}, got {displacement}"
