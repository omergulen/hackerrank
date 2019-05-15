#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the minimumBribes function below.
def minimumBribes(q):
    counter = 0
    for i,e in enumerate(q):
        e -= 1
        if e - i  > 2:
            return "Too chaotic"
        
        for j in range(max(e-1,0), i):
            if q[j] > e:
                counter += 1

    return counter

if __name__ == '__main__':
    t = int(input())
    lines = []
    for t_itr in range(t):
        n = int(input())

        q = list(map(int, input().rstrip().split()))

        lines.append(str(minimumBribes(q)))
    
    print("\n".join(lines))
