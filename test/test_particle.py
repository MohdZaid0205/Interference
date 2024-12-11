from core.vector import Vector2D
from core.particle import Particle

from math import sqrt
import pytest


class TestParticle:

    @pytest.mark.parametrize(
        "position, displacement, intensity, expected_position, expected_displacement, expected_intensity",
        [
            (Vector2D(  0,   0),  0.0, 1.0, Vector2D(  0,   0),  0.0, 1.0), # Default state
            (Vector2D( 10,  15),  5.5, 0.9, Vector2D( 10,  15),  5.5, 0.9), # Positive values
            (Vector2D( -5, -10), 12.3, 0.0, Vector2D( -5, -10), 12.3, 0.0), # Negative position with zero intensity
            (Vector2D(100, 200), 20.0, 1.5, Vector2D(100, 200), 20.0, 1.5), # Large values
        ]
    )
    def test_initialization(self, position, displacement, intensity, expected_position, expected_displacement, expected_intensity):
        particle = Particle(P=position, d=displacement, i=intensity)
        assert particle.P == expected_position, f"Expected position={expected_position}, got {particle.P}"
        assert particle.d == expected_displacement, f"Expected displacement={expected_displacement}, got {particle.d}"
        assert particle.i == expected_intensity, f"Expected intensity={expected_intensity}, got {particle.i}"

    @pytest.mark.parametrize(
        "p1, p2, expected_distance",
        [
            (Particle(P=Vector2D( 0,  0), d=0, i=1.0), Particle(P=Vector2D( 3,  4), d=0, i=1.0), 5.0),      # Classic 3-4-5 triangle
            (Particle(P=Vector2D(10, 15), d=0, i=1.0), Particle(P=Vector2D(13, 19), d=0, i=1.0), 5.0),      # Nearby points
            (Particle(P=Vector2D(-5, -5), d=0, i=1.0), Particle(P=Vector2D( 5,  5), d=0, i=1.0), sqrt(200)),# Across quadrants
        ]
    )
    def test_particle_distance(self, p1, p2, expected_distance):
        distance = Vector2D.distance(p1.P, p2.P)
        assert abs(distance - expected_distance) < 1e-9, \
            f"Expected distance={expected_distance}, got {distance}"
