#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the countingValleys function below.
def countingValleys(n, s):
    counter = 0
    altitute = 0

    for i in s:
        if i == "D":
            altitute -= 1
        else:
            altitute += 1
            if altitute == 0:
                counter += 1
        
    return counter

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    s = input()

    result = countingValleys(n, s)

    fptr.write(str(result) + '\n')

    fptr.close()
