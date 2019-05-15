#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the sockMerchant function below.
def sockMerchant(n, ar):
    while len(ar) > 0:
        ar_first = ar[0]
        if ar.count(ar_first) % 2 != 0:
            n -= 1
        ar = list(filter((ar_first).__ne__, ar))

    return int(n/2)


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    ar = list(map(int, input().rstrip().split()))

    result = sockMerchant(n, ar)

    fptr.write(str(result) + '\n')

    fptr.close()
