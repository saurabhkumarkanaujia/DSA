#Given an array nums, write a function to move all 0's to the end of it while maintaining the relative order of the non-zero elements in O(n) Time complexity and O(1) Space complexity with single traversal allowed

#Input: [0,1,0,3,12]
#Output: [1,3,12,0,0]

#Note:
#You must do this in-place without making a copy of the array.
#Hint : Single traversal Movement

import unittest
def MoveZeroToEnd(array, n): 
    #try your self
    c = 0
    i = 0
    while i < n:
        if (array[i] != 0):
            array[c] = array[i]
            c+=1
        i+=1
    while (c <= n-1):
        array[c] = 0
        c+=1
    return array

 #ok for all test cases required 
class Test(unittest.TestCase):
  
    def test_MoveZeroToEnd1(self):
        actual = MoveZeroToEnd([1,3,0,0,4,0,9],7)
        expected = [1,3,4,9,0,0,0]
        self.assertEqual(actual, expected)

    def test_MoveZeroToEnd2(self):
        actual = MoveZeroToEnd([0,1,0,3,12],5)
        expected = [1,3,12,0,0]
        self.assertEqual(actual, expected)

    def test_MoveZeroToEnd3(self):
        actual = MoveZeroToEnd([0, 1, 9, 8, 4, 0, 0, 2, 7, 0, 6, 0, 9],13)
        expected = [1,9,8,4,2,7,6,9,0,0,0,0,0]
        self.assertEqual(actual, expected)

unittest.main(verbosity=2)