from typing import Callable, Optional, Union


class Grid[Member]:
    # A class representing a grid structure with a generic member type.

    def __init__(self, m: int, n: int, default: Optional[Member] = None) -> None:
        self.m = m
        self.n = n
        self.__grid = [[default for _ in range(n)] for _ in range(m)]

    def set[T](self, i: int, j: int, value: Optional[Member] = None, modifier: Optional[Callable[[Member],T]] = None) -> Optional[T]:
        if modifier is not None:
            return modifier(self.__grid[i][j])
        self.__grid[i][j] = value

    def get[T](self, i: int, j: int, specifier: Optional[Callable[[Member],T]] = None) -> Union[T, Member]:
        if specifier is not None:
            return specifier(self.__grid[i][j])
        return self.__grid[i][j]
