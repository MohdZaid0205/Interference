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

