#! /usr/bin/env python
#
# GCD(a,b) returns the Greatest common divisor between a and b
#

import sys
import math

def GCD(a,b):
    int major = 0
    int minor = 0
    #Check if a and b are positive integers
    if a== 0 or b == 0:
        print "GCD(%d,%d) is 0" % (a, b)
    if a == b:
        print "GCD(%d,%d) is %d" % (a, b, a)
        sys.exit
    if a < b:
        major = b
        minor = a
    else:
        major = a
        minor = b
    

def main():
    


if __name__ == '__main__':
    main()
