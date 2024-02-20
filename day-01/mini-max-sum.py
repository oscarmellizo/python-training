#!/bin/python3
#
# Complete the 'miniMaxSum' function below.
#
# The function accepts INTEGER_ARRAY arr as parameter.
#

def miniMaxSum(arr):
    arr.sort()
    index = 0
    sum_min = 0
    sum_max = 0
    arr_len = len(arr) - 1
    for num in arr:
        if index == 0:
            sum_min += num
        elif index == arr_len:
            sum_max += num
        else:
            sum_min += num
            sum_max += num
        index += 1
    print(sum_min, sum_max)

if __name__ == '__main__':

    arr = list(map(int, input().rstrip().split()))

    miniMaxSum(arr)
