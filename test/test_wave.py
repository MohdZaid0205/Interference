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

    @pytest.mark.parametrize(
        "A, x, expected_intensity",
        [
            (1.0, 1.0, 1.0),  # Standard case
            (2.0, 2.0, 2.0),  # Double amplitude, double x
            (3.0, 1.0, 9.0),  # Triple amplitude
        ]
    )
    def test_intensity(self, A, x, expected_intensity):
        wave = WaveEquation(A=A, k=0, w=0, q=0, t=SIN_WAVE)
        intensity = wave.intensity(x)
        assert abs(intensity - expected_intensity) < 1e-9, \
            f"Expected intensity={expected_intensity}, got {intensity}"