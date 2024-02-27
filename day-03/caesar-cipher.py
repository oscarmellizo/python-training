#!/bin/python3

import os
import string

#
# Complete the 'caesarCipher' function below.
#
# The function is expected to return a STRING.
# The function accepts following parameters:
#  1. STRING s
#  2. INTEGER k
#
def getRotatedLetter(limitInf, limitSup, moves, letter):
    while moves > 25:
        moves -= 26
    tmpOrd = ord(letter)
    ord_move = tmpOrd + moves
    return chr(ord_move if ord_move <= limitSup else limitInf + ord_move - limitSup - 1)
    
def caesarCipher(s, k):
    result = ""
    
    for x in range(n):
        letter = s[x]
        orde = ord(letter)
        
        if letter in string.ascii_letters:
            if orde >= 65 and orde <= 90:
                result += getRotatedLetter(65, 90, k, letter)
            else:
                result += getRotatedLetter(97, 122, k, letter)
        else:
            result += letter
    
    return result

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    s = input()

    k = int(input().strip())

    result = caesarCipher(s, k)

    fptr.write(result + '\n')

    fptr.close()
