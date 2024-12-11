from core.vector import Vector2D

import pytest

class TestVector2D:
    """Test suite for the Vector2D class."""

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
        """Test initialization of Vector2D objects."""
        vector = Vector2D(x, y)
        assert vector.x == expected_x, f"Expected x={expected_x}, got x={vector.x}"
        assert vector.y == expected_y, f"Expected y={expected_y}, got y={vector.y}"
