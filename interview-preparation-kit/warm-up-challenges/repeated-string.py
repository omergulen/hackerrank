#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the repeatedString function below.
def repeatedString(s, n):
    base_count = s.count('a')
    base_length = len(s)

    full_times = int(n/base_length)
    total_count = base_count * full_times

    remaining = n % base_length
    if remaining != 0:
        total_count += s[:remaining].count('a')

    return total_count


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    n = int(input())

    result = repeatedString(s, n)

    fptr.write(str(result) + '\n')

    fptr.close()
