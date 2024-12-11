from core.vector import Vector2D
from core.wave import WaveEquation, WaveSourceEmitter, COS_WAVE, SIN_WAVE

from math import sin, cos, pi, sqrt
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
        

class TestWaveSourceEmitter:
    """Test suite for the WaveSourceEmitter class."""

    @pytest.mark.parametrize(
        "source_position, wave, target_position, t, expected_displacement",
        [
            (Vector2D(0, 0), WaveEquation(1, 1, pi, 0, SIN_WAVE), Vector2D(1, 1), 1,
             sin(pi - sqrt(2))),  # Sine wave displacement
            (Vector2D(0, 0), WaveEquation(2, 0, pi / 2, pi / 2, COS_WAVE), Vector2D(0, 2), 2,
             2 * cos(pi / 2)),  # Cosine wave with no spatial frequency
        ]
    )
    def test_calculate_displacement(self, source_position, wave, target_position, t, expected_displacement):
        emitter = WaveSourceEmitter(P=source_position, W=wave, d=1.0)
        displacement = emitter.calculateDisplacement(at=target_position, t=t)
        assert abs(displacement - expected_displacement) < 1e-9, \
            f"Expected displacement={expected_displacement}, got {displacement}"

    @pytest.mark.parametrize(
        "source_position, wave, target_position, falloff, expected_intensity",
        [
            (Vector2D(0, 0), WaveEquation(1, 0, 0, 0, SIN_WAVE), Vector2D(3, 4), 2.0, 0.1 ),  # Intensity with falloff
            (Vector2D(0, 0), WaveEquation(2, 0, 0, 0, COS_WAVE), Vector2D(6, 8), 1.0, 0.4 ),  # Double amplitude
        ]
    )
    def test_calculate_intensity(self, source_position, wave, target_position, falloff, expected_intensity):
        emitter = WaveSourceEmitter(P=source_position, W=wave, d=falloff)
        intensity = emitter.calculateIntensity(at=target_position)
        assert abs(intensity - expected_intensity) < 1e-9, \
            f"Expected intensity={expected_intensity}, got {intensity}"
