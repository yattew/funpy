from typing import Any, TypeVar, Callable, Union
T = TypeVar('T')



# adding a pipe operator in python
# using the | to display the piping
class ApplicationChain:
    pass


class FunctionalContainer:
    def __init__(self, val:T) -> None:
        self.val = val

    def __or__(self, other: Union[Callable, ApplicationChain]) -> "FunctionalContainer":
        res = other(self.val)
        return FunctionalContainer(res)

    def __call__(self, other = None) -> T:
        if other:
            return self.val(other)
        return self.val
