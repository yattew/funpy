from typing import Any, TypeVar, Callable, Union
T = TypeVar('T')

# adding a pipe operator in python
# using the | to display the piping


class FunctionalContainer:
    def __init__(self, val: Union[T, Callable]) -> None:
        self.val = val

    def __or__(self,
               other: Callable[[Union[T, Callable]], "FunctionalContainer"]
               ) -> "FunctionalContainer":
        if callable(self.val):
            res = FunctionalContainer(lambda x: other.val(self.val(x)))
            return res
        else:
            res = other(self.val)
            return FunctionalContainer(res)

    def __call__(self, other=None) -> T:
        if other:
            return self.val(other)
        return self.val
