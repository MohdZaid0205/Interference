from core.vector import Vector2D


# Test for distance method of Vector2D
def test_vector2d_distance_same_point():
    v1 = Vector2D(0, 0)
    v2 = Vector2D(0, 0)
    distance = Vector2D.distance(v1, v2)
    expected_distance = 0.0  # Distance between the same point is 0
    assert abs(distance - expected_distance) < 1e-6, f"Expected distance {expected_distance}, got {distance}"

def test_vector2d_distance_horizontal():
    v1 = Vector2D(0, 0)
    v2 = Vector2D(3, 0)  # 3 units apart horizontally
    distance = Vector2D.distance(v1, v2)
    expected_distance = 3.0  # Euclidean distance (3,0) from (0,0) is 3
    assert abs(distance - expected_distance) < 1e-6, f"Expected distance {expected_distance}, got {distance}"

def test_vector2d_distance_vertical():
    v1 = Vector2D(0, 0)
    v2 = Vector2D(0, 4)  # 4 units apart vertically
    distance = Vector2D.distance(v1, v2)
    expected_distance = 4.0  # Euclidean distance (0,4) from (0,0) is 4
    assert abs(distance - expected_distance) < 1e-6, f"Expected distance {expected_distance}, got {distance}"

def test_vector2d_distance_diagonal():
    v1 = Vector2D(0, 0)
    v2 = Vector2D(3, 4)  # 3 units horizontal, 4 units vertical
    distance = Vector2D.distance(v1, v2)
    expected_distance = 5.0  # Euclidean distance sqrt(3^2 + 4^2) = 5
    assert abs(distance - expected_distance) < 1e-6, f"Expected distance {expected_distance}, got {distance}"

def test_vector2d_distance_negative_coordinates():
    v1 = Vector2D(-3, -4)
    v2 = Vector2D(3, 4)  # Testing with negative coordinates
    distance = Vector2D.distance(v1, v2)
    expected_distance = 10.0  # sqrt((-3 - 3)^2 + (-4 - 4)^2) = sqrt(36 + 64) = 10
    assert abs(distance - expected_distance) < 1e-6, f"Expected distance {expected_distance}, got {distance}"
