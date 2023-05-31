from Funpy import FunctionalContainer as FC
import Funpy.functions as F

# take a list as input and print evens
print(
    " ".join(
        map(str,
            filter(lambda x: x % 2 == 0,
                   map(int,
                       input("enter a list of numbers:").split())))))

(
    FC("enter a list of numbers: ")
    | FC(input)
    | F.split()
    | F.map(int)
    | F.filter(lambda x: x % 2 == 0)
    | F.map(str)
    | F.join(" ")
    | FC(print)
)
