#! /usr/bin/env python
#
# GCD(a,b) returns the Greatest common divisor between a and b
#

import sys
import math

def GCD(a,b):
    int maggiore = 0
    int minore = 0
    #Check if a and b are positive integers
    
    #
    if a == 0:
        print "GCD(0,%d) is %d" % (b, b)
    if b == 0:
        print "GCD(%d,0) is %d" % (a, a)
    if a == b:
        print "GCD(%d,%d) is %d" % (a, b, a)
        sys.exit(2)
    if a < b:
        maggiore = b
        minore = a
    else:
        maggiore = a
        minore = b
    

def main():
    


if __name__ == '__main__':
    main()
