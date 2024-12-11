from core.vector import Vector2D

from math import sqrt
import pytest

class TestVector2D:

    @pytest.mark.parametrize(
        "x, y, expected_x, expected_y",
        [
            ( 0,   0,  0,   0), # Default origin vector
            (10,   5, 10,   5), # Positive coordinates
            (-5, -10, -5, -10), # Negative coordinates
            ( 0, -15,  0, -15), # Mixed zero and negative coordinates
        ]
    )
    def test_initialization(self, x, y, expected_x, expected_y):
        vector = Vector2D(x, y)
        assert vector.x == expected_x, f"Expected x={expected_x}, got x={vector.x}"
        assert vector.y == expected_y, f"Expected y={expected_y}, got y={vector.y}"


    @pytest.mark.parametrize(
        "v1, v2, expected_distance",
        [
            (Vector2D( 0, 0), Vector2D(0, 0), 0.0),     # Same point
            (Vector2D( 0, 0), Vector2D(3, 4), 5.0),     # 3-4-5 triangle
            (Vector2D(-3,-4), Vector2D(0, 0), 5.0),     # Negative coordinates
            (Vector2D( 1, 2), Vector2D(4, 6), 5.0),     # Positive coordinates
            (Vector2D(-1,-1), Vector2D(1, 1), sqrt(8)), # Across quadrants
        ]
    )
    def test_distance(self, v1, v2, expected_distance):
        distance = Vector2D.distance(v1, v2)
        assert abs(distance - expected_distance) < 1e-9, \
            f"Expected distance={expected_distance}, got distance={distance}"

    @pytest.mark.parametrize(
        "v1, v2, expected_distance",
        [
            (Vector2D(     0,      0), Vector2D(   1000,    1000),    1414.213), # Large values
            (Vector2D(123456, 654321), Vector2D(-123456, -654321), 1331731.737), # Extremely large values
        ]
    )
    def test_large_values(self, v1, v2, expected_distance):
        distance = Vector2D.distance(v1, v2)
        assert abs(distance - expected_distance) < 1e-3, \
            f"Expected distance={expected_distance}, got distance={distance}"