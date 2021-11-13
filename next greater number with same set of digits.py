# Digit rearrangement method to find next greater number with same set of digits
# Write an algorithm to find out next greater number to given number with the same set of digits Asked in : Morgan Stanley, Makemytrip, Amazon
# Example:

#Input 1:
#A = [1, 2, 3]
#Output 1:
#[1, 3, 2]
#Input 2:
#A = [3, 2, 1]
#Output 2:
#[1, 2, 3]
#Hint 1 : Start comparing from right most Integer value with left one
#Hint2 : You need to find immediate higher Number from given number

from typing import List

def findNextNumber(array : List[int], n):
      
     # Start from the right most digit and find the first
     # digit that is smaller than the digit next to it
     for i in range(n-1,0,-1):
         if (array[i] >= array[i-1]):
             break
              
     # If no such digit found,then all arrays are in
     # descending order, no greater array is possible
     if i == 1 and array[i] <= array[i-1]:
         print ("Next array not possible")
         return
          
     # Find the smallest digit on the right side of
     # (i-1)'th digit that is greater than array[i-1]
     element = array[i-1]
     minimum = i
     for j in range(i+1,n):
         if array[j] > element and array[j] < array[minimum]:
             minimum = j
          
     # Swapping the above found smallest digit with (i-1)'th
     # you can also use swap library method directly 
     array[minimum],array[i-1] = array[i-1], array[minimum]
      
     # X is the final array, in integer datatype
     element = 0
     # Converting list upto i-1 into array
     for j in range(i):
         element = element * 10 + array[j]
      
     # Sort the digits after i-1 in ascending order
     array = sorted(array[i:])
     # converting the remaining sorted digits into array
     for j in range(n-i):
         element = element * 10 + array[j]
      
     return element


import unittest

class Test(unittest.TestCase):
    def test_printfrequency_1(self):
        actual = findNextNumber([2,1,8,7,6,5],6)
        expected = 251678
        self.assertEqual(actual, expected)

    def test_printfrequency_2(self):
        actual = findNextNumber([1,2,3,4],4)
        expected = 1243
        self.assertEqual(actual, expected)

    def test_printfrequency_3(self):
        actual = findNextNumber([5,3,4,9,7,6],6)
        expected = 536479
        self.assertEqual(actual, expected)

    def test_printfrequency_4(self):
        actual = findNextNumber([6,9,3,8,6,5,2],7)
        expected = 6952368
        self.assertEqual(actual, expected)

unittest.main(verbosity=2)
