from . import *

original_map = map
def map(fn) -> FunctionalContainer:
    return FunctionalContainer(lambda x: original_map(fn, x))

original_filter = filter
def filter(fn) -> FunctionalContainer:
    return FunctionalContainer(lambda x: original_filter(fn, x))

def split(sp = " ") -> FunctionalContainer:
    return FunctionalContainer(lambda x: x.split(sp))

def join(sp = "") -> FunctionalContainer:
    return FunctionalContainer(lambda x: sp.join(x))