#! /usr/bin/env python
#
# GCD(a,b) returns the Greatest Common Divisor between a and b
#

import sys


def GCD(a, b):
    """Return GCD between a and b."""
    if a > b:
        maxnum = a
        minnum = b
    elif a == b:
        return a
    else:
        maxnum = b
        minnum = a

    # Base cases
    if maxnum == 0 and minnum == 0:
        return 0

    # Standard case
    if maxnum != 0 and minnum == 0:
        return maxnum
    else:
        return GCD(minnum, maxnum % minnum)


if __name__ == '__main__':

    print "This program calculates the Greatest Common Divisor between a and b"

    try:
        a = int(raw_input("Insert a: "))
        b = int(raw_input("Insert b: "))
    except ValueError:
        print "Please, only positive integers!"
        sys.exit(1)

    result = GCD(a, b)
    print ""
    print "* The GCD between %s and %s is: %s\n" % (a, b, result)
