#Array consist of only 0's, 1's and 2's. Write an algorithm to sort  this array in O(n) time complexity and O(1) Space complexity with only one traversal Asked in : : Amazon, Microsoft, Adobe, WalmartLabs

#Input : [0 1 2 0 1 2]
#Modify array so that it becomes : [0 0 1 1 2 2]
#Hint1 : You are not suppose to use any extra space
#Hint2 : You need change the same array with single traversal with O(n) time complexity

# Utility function to swap elements `array[i]` and `array[j]` in the list
def swap(array, i, j):
 
    temp = array[i]
    array[i] = array[j]
    array[j] = temp
 
 
# Linear time partition routine to sort a list containing 0, 1, and 2.
# It is similar to 3–way partitioning for the Dutch national flag problem.
def sort_0_1_2(array):
 
    low = mid = 0
    high = len(array) - 1
 
    while mid <= high:
        if array[mid] == 0:      # current element is 0
            swap(array, low, mid)
            low = low + 1
            mid = mid + 1
        elif array[mid] == 2:    # current element is 2
            swap(array, mid, high)
            high = high - 1
        else:                   # current element is 1
            mid = mid + 1
 
 
if __name__ == '__main__':
 
    array = [0, 1, 2, 2, 1, 0, 0, 2, 0, 1, 1, 0]
    sort_0_1_2(array)
    print(array)

