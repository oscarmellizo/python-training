#!/bin/python3
import os
#
# Complete the 'timeConversion' function below.
#
# The function is expected to return a STRING.
# The function accepts STRING s as parameter.
#

def timeConversion(s):
    hour = int(s[0:2])
    meridian = s[8:10]
    if hour == 12:
        new_hour = 0 if meridian == "AM" else hour
    else:
        new_hour = hour + 12 if meridian == "PM" else hour
        
    return "{:02d}".format(new_hour) + s[2:8]

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = timeConversion(s)

    fptr.write(result + '\n')

    fptr.close()
