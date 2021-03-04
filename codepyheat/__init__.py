"""

    @author: Nicolas Flipo
    @date: 14.02.2021

    Init file of the codepyheat package
    Defines the path towards the JSON files
    Defines CONST values
    Defines printing functions that translate the name of CONST and printing
        templates.

"""
import pathlib

JSONPATH = str(pathlib.Path(__file__).parent.absolute()) + '/json/'

X = 0  # defines the int value of X direction
Z = 1  # defines the int value of Z direction
NDIM = 2  # defines the number of dimensions

# Cardinal directions are associated to int value in order to tabulate faces
# easily
E = 1  # int value of east
W = 0  # int value of west
S = 0  # int value of south
N = 1  # int value of north
ONE = 0  # int value of the first object in a direction
TWO = 1  # int value of the second object in a direction

EPS = 0.0000000001

CODE_GEOM = -6666


def printDir(dir):
    if dir == X:
        str = 'X'
    else:
        str = 'Z'
    return str


def printDirCard(dir, num):
    val = CODE_GEOM
    if dir == X:
        if num == E:
            val = 'E'
        elif num == W:
            val = 'W'
    elif dir == Z:
        if num == N:
            val = 'N'
        elif num == S:
            val = 'S'
    else:
        "Unknown face number {} in the {} direction".format(num, dir)
    return val


def complement(dir):
    if dir == 0:
        val = 1
    else:
        val = 0
    return val


caracParamTemplate = "{}: {:4.3e} {}"

caracItSteadyTemplate = "{:3.2e}_{:3.2f}_{:5.4f}"
