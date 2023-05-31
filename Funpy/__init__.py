from typing import Any, TypeVar, Callable
T = TypeVar('T')



# adding a pipe operator in python
# using the >> to display the piping

class FunctionalContainer:
    def __init__(self, val:T) -> None:
        self.val = val

    def __or__(self, other: Callable) -> "FunctionalContainer":
        res = other(self.val)
        if other.keep == True:
            self.val = res
            return self
        return FunctionalContainer(res)

    def __call__(self) -> T:
        return self.val

class ApplicationChain:
    pass