#!/bin/python3
import os
#
# Complete the 'diagonalDifference' function below.
#
# The function is expected to return an INTEGER.
# The function accepts 2D_INTEGER_ARRAY arr as parameter.
#

def diagonalDifference(arr):
    left = 0
    right = len(arr) - 1
    sum_right = 0
    sum_left = 0
    for i in range(len(arr)):
        sum_left += arr[i][left]
        left += 1
        sum_right += arr[i][right]
        right -= 1

    return abs(sum_left - sum_right)

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    arr = []

    for _ in range(n):
        arr.append(list(map(int, input().rstrip().split())))

    result = diagonalDifference(arr)

    fptr.write(str(result) + '\n')

    fptr.close()
