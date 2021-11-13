# Majority Number
# Asked In: YahooLinkedin
# Given an array of integer, write an efficient algorithm to find majority number in that array in Time Complexity O(n) and Space Complexity O(1)

# Example:

# [Majority Number : The only number in the integer array which appears more than n/2 times if the length of the array is n]
# Input : [1, 8, 7, 4, 1, 2, 2, 2, 2, 2, 2 ]
# Output: 2 ( 2 appears in this integer array more than 5 times] 
# [Hint: Think of using the hint, element appears more than half

import unittest
# Function to return majority element present in given list
def majorityElement(A):
 
    #Write Your Code Here
 
    majority = A[0]
    count = 1
    for i in range(1, len(A)):
        if (majority == A[i]):
            count += 1
        else:
            count -= 1
        if count == 0:
            majority = A[i]
            count = 1
    return majority
#ok for all test cases required 
class Test(unittest.TestCase):
    def test_majorityElement1(self):
        actual = majorityElement([1, 3, 3, 4, 3, 2, 2, 2, 2, 2, 2])
        expected = 2
        self.assertEqual(actual, expected)

    def test_majorityElement2(self):
        actual = majorityElement([1, 8, 7, 4, 1, 2, 2, 2, 2, 2, 2])
        expected = 2
        self.assertEqual(actual, expected)

    def test_majorityElement3(self):
        actual = majorityElement([3,2,3])
        expected = 3
        self.assertEqual(actual, expected)

    def test_majorityElement4(self):
        actual = majorityElement([2,2,1,1,1,2,2])
        expected = 2
        self.assertEqual(actual, expected)
unittest.main(verbosity=2)