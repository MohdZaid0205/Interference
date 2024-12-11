from core.grid import Grid

import pytest
from typing import Optional


class TestGridFunctionality:

    @pytest.mark.parametrize(
        argnames="m, n, default, expected",
        argvalues=[
            (0, 0, None, 0),  # Empty grid with no dimensions.
            (1, 1, 0000, 1),  # Single cell grid with default value 0.
            (2, 3, None, 6),  # Rectangular grid with 6 cells and default value None.
            (3, 3, 0000, 9),  # Square grid with 9 cells and default value 0.
        ]
    )
    def test_initialization(self, m, n, default, expected):
        grid_: Grid[Optional[int]] = Grid[Optional[int]](m, n, default)
        count = 0
        for i in range(m):
            for j in range(n):
                try:
                    assert grid_.get(i, j) == default, f"Expected default value {default} at ({i=}, {j=})"
                    count += 1
                except IndexError:
                    assert False, f"Grid ({m=}, {n=}) but ({i=}, {j=}) doesn't exist."
        else:
            assert count == expected, f"Grid ({m=}, {n=}) expected dimensions={expected} but counted dimensions={count}"

    @pytest.mark.parametrize(
        argnames="m, n, i, j, value",
        argvalues=[
            (1, 1, 0, 0,  42),  # Setting single value in a 1x1 grid.
            (2, 2, 1, 1,  99),  # Setting a value in a small square grid.
            (3, 3, 0, 2,  -5),  # Negative value in a rectangular grid.
            (4, 4, 3, 3, 100),  # Large positive value in bottom-right cell of 4x4 grid.
        ]
    )
    def test_set_and_get(self, m, n, i, j, value):
        grid_: Grid[int] = Grid[int](m, n, default=0)
        grid_.set(i, j, value)
        assert grid_.get(i, j) == value, f"Expected {value} at ({i=}, {j=}), got {grid_.get(i, j)}"

    @pytest.mark.parametrize(
        argnames="m, n, i, j, value, modifier",
        argvalues=[
            (2, 2, 0, 0, 10, lambda x: x * 2  ), # Modifier doubles the value.
            (3, 3, 2, 2,  5, lambda x: x + 3  ), # Modifier adds 3 to the value.
            (4, 4, 1, 1, -1, lambda x: abs(x) ), # Modifier takes absolute value.
            (5, 5, 4, 4,  7, lambda x: x ** 2 ), # Modifier squares the value.
        ]
    )
    def test_set_with_modifier(self, m, n, i, j, value, modifier):
        grid_: Grid[int] = Grid[int](m, n, default=0)
        grid_.set(i, j, value, modifier=modifier)
        expected = modifier(value)
        assert grid_.get(i, j) == expected, f"Expected modified value {expected} at ({i=}, {j=}), got {grid_.get(i, j)}"

    @pytest.mark.parametrize(
        argnames="m, n, i, j, value, specifier",
        argvalues=[
            (2, 2, 0, 0, 10, lambda x: x * 2  ), # Specifier doubles the value on retrieval.
            (3, 3, 2, 2,  5, lambda x: x + 3  ), # Specifier adds 3 to the value on retrieval.
            (4, 4, 1, 1, -1, lambda x: abs(x) ), # Specifier returns absolute value.
            (5, 5, 4, 4,  7, lambda x: x ** 2 ), # Specifier squares the value on retrieval.
        ]
    )
    def test_get_with_specifier(self, m, n, i, j, value, specifier):
        grid_: Grid[int] = Grid[int](m, n, default=0)
        grid_.set(i, j, value)
        expected = specifier(value)
        assert grid_.get(i, j, specifier=specifier) == expected, f"Expected specified value {expected} at ({i=}, {j=}), got {grid_.get(i, j, specifier=specifier)}"

