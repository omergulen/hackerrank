#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the jumpingOnClouds function below.
def jumpingOnClouds(c):
    counter = 0
    current = 0
    while current != (len(c) - 1):
        if (len(c) - 1) >= (current + 2) and c[current + 2] == 0:
            current += 2
        else:
            current += 1
        counter += 1

    return counter

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    c = list(map(int, input().rstrip().split()))

    result = jumpingOnClouds(c)

    fptr.write(str(result) + '\n')

    fptr.close()
