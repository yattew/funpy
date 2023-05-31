from Funpy import FunctionalContainer as FC

l = FC([1, 2, 3, 4, 5])


def fmap(fn) -> FC:
    return FC(lambda x: list(map(fn, x)))


(
    l
    | fmap(lambda x: x**2)
    | FC(print)
)
