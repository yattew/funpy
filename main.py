from Funpy import FunctionalContainer as FC
from Funpy import functions as F

a = FC(10)

(
    a
    | F.sq()
    | F.print()
)

a | F.print()


(
    a
    | F.sq(keep=True)
    | F.print()
)
