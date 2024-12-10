from core.grid import Grid
import pytest


def test_grid_initialization():
    grid = Grid[int](3, 3, default=0)
    for i in range(3):
        for j in range(3):
            assert grid.get(i, j) == 0, f"[Error] Default value mismatch at ({i}, {j}): Expected 0, Got {grid.get(i, j)}"

def test_grid_set_without_modifier():
    grid = Grid[int](2, 2, default=0)
    grid.set(0, 0, 5)
    grid.set(1, 1, 10)

    assert grid.get(0, 0) == 5, f"[Error] Value mismatch at (0, 0): Expected 5, Got {grid.get(0, 0)}"
    assert grid.get(1, 1) == 10, f"[Error] Value mismatch at (1, 1): Expected 10, Got {grid.get(1, 1)}"
    assert grid.get(0, 1) == 0, f"[Error] Default value mismatch at (0, 1): Expected 0, Got {grid.get(0, 1)}"

def test_grid_set_with_modifier():
    grid = Grid[int](2, 2, default=0)
    grid.set(0, 0, 5, modifier=lambda x: x * 2)
    grid.set(1, 1, 3, modifier=lambda x: x + 7)

    assert grid.get(1, 1) == 10, f"[Error] Modifier value mismatch at (1, 1): Expected 10, Got {grid.get(1, 1)}"
    assert grid.get(0, 0) == 10, f"[Error] Modifier value mismatch at (0, 0): Expected 10, Got {grid.get(0, 0)}"

def test_grid_get_with_specifier():
    grid = Grid[str](2, 2, default="hello")
    grid.set(0, 0, "world")
    length_specifier = lambda x: len(x)

    assert grid.get(0, 0, specifier=length_specifier) == 5, \
        f"[Error] Specifier mismatch at (0, 0): Expected 5, Got {grid.get(0, 0, specifier=length_specifier)}"
    assert grid.get(1, 1, specifier=length_specifier) == 5, \
        f"[Error] Specifier mismatch at (1, 1): Expected 5, Got {grid.get(1, 1, specifier=length_specifier)}"

def test_grid_get_without_specifier():
    grid = Grid[float](2, 2, default=1.5)
    grid.set(0, 0, 3.0)

    assert grid.get(0, 0) == 3.0, f"[Error] Value mismatch at (0, 0): Expected 3.0, Got {grid.get(0, 0)}"
    assert grid.get(1, 1) == 1.5, f"[Error] Default value mismatch at (1, 1): Expected 1.5, Got {grid.get(1, 1)}"

def test_edge_cases():
    grid = Grid[int](0, 0)
    
    with pytest.raises(IndexError):
        grid.set(0, 0, 1)
    
    with pytest.raises(IndexError):
        grid.get(0, 0)

def test_large_grid():
    grid = Grid[int](1000, 1000, default=-1)
    grid.set(999, 999, 42)

    assert grid.get(999, 999) == 42, f"[Error] Value mismatch at (999, 999): Expected 42, Got {grid.get(999, 999)}"
    assert grid.get(0, 0) == -1, f"[Error] Default value mismatch at (0, 0): Expected -1, Got {grid.get(0, 0)}"
