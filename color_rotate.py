from fabric.api import run
from fabric.api import local
from fabric.api import env
from fabric.colors import blue, cyan, green, magenta, red, white, yellow

import sys

def color_rotate(s):
    """Print every character in the given string in a different color.
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

color_rotate('abcdefghijklmnopqrstuvewkfphwevnror')
