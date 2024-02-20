#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'plusMinus' function below.
#
# The function accepts INTEGER_ARRAY arr as parameter.
#

def plusMinus(arr):
    zero_quantity = 0
    negative_quantity = 0
    positive_quantity = 0
    for num in arr:
        if num == 0:
            zero_quantity += 1
        elif num > 0:
            positive_quantity += 1
        elif num < 0:
            negative_quantity += 1

    print('{:.6f}'.format(positive_quantity / n))
    print('{:.6f}'.format(negative_quantity / n))
    print('{:.6f}'.format(zero_quantity / n))
            
if __name__ == '__main__':
    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    plusMinus(arr)
