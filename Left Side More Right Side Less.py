#Left Side More Right Side Less

# We have an array, we have to find an element before which all elements are less than it, and after which all are greater than it. Finally, return the index of the element, if there is no such element, then return -1: Time complexity O(n) and Space Complexity O(n)

# Example:
# Input: arr[] = {5, 1, 4, 3, 6, 8, 10, 7, 9};
# Output: 4
# Explanation: All elements on the left of arr[4] are smaller than it
# and all elements on right are greater.

# Problem level: Medium

import unittest
def findElement(array, n): 
	#Write your code here
    left = [None]*n
    left[0] = float('-inf')
    for i in range(1,n):
        left[i] = max(array[i-1], left[i-1])
    right = float('inf')
    for i in range(n-1, -1, -1):
        if (left[i] < array[i]) and (right > array[i]):
            return i
        right = min(array[i], right)
    return -1

#ok for all test cases required
class Test(unittest.TestCase):
    def test_findElement1(self):
        actual = findElement([5, 1, 4, 3, 6, 8, 10, 7, 9],9)
        expected = 4
        self.assertEqual(actual, expected)

    def test_findElement2(self):
        actual = findElement([6, 2, 5, 4, 7, 9, 11, 8, 10],9)
        expected = 4
        self.assertEqual(actual, expected)

    def test_findElement3(self):
        actual = findElement([5, 1, 4, 4],4)
        expected = -1
        self.assertEqual(actual, expected)

unittest.main(verbosity=2)

