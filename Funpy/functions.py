from . import *

original_print = print


class sq:
    def __init__(self, keep=False) -> None:
        self.keep = keep

    def __call__(self, item: T) -> T:
        return item**2


class print:
    def __init__(self, keep=False) -> None:
        self.keep = keep

    def __call__(self, item: T, sep='\n') -> T:
        original_print(item)
        return item
