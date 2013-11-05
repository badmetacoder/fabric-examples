from fabric.api import local
from fabric.colors import blue, cyan, green, magenta, red, white, yellow

import sys

"""color-rotate.py -- Rotates colors turning any string into a rainbow
explosion
"""


def color_rotate(s):

    """return the ANSI color-rotated version of the given string.
    """

    n = len(s)
    m = 0
    while (m < n):
        if (m % 7) == 0:
            sys.stdout.write(blue(s[m:m+1]))
        elif (m % 7) == 1:
            sys.stdout.write(cyan(s[m:m+1]))
        elif (m % 7) == 2:
            sys.stdout.write(green(s[m:m+1]))
        elif (m % 7) == 3:
            sys.stdout.write(magenta(s[m:m+1]))
        elif (m % 7) == 4:
            sys.stdout.write(red(s[m:m+1]))
        elif (m % 7) == 5:
            sys.stdout.write(white(s[m:m+1]))
        elif (m % 7) == 6:
            sys.stdout.write(yellow(s[m:m+1]))
        m += 1


def color_top():

    """color the output of top -b -n 1 | head
    """

    local_output = local('top -b -n 1 | head', capture=True)
    color_rotate(local_output)
    print
