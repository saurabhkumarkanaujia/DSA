# Count frequencies of array elements in O(n) time complexity
# Asked In: PayTmVmWareAmazon
# Array of length n having integers 1 to n with some elements being repeated. Count frequencies of all elements from 1 to n in Time Complexity O(n) and Space Complexity O(1) Asked in : : PayTm, VmWare, Amazon

# Example:

# Input array elements: 5, 1, 2, 5, 5, 5, 1, 1, 2, 2
# Output
# Frequency of 5 = 4
# Frequency of 2 = 3
# Frequency of 1 = 3
# Hint1 : All the numbers are between 1 to n in the given array
# Hint2: Think of updating index of array for given number

# Function to find counts of all elements present in arr[0..n-1]. The array  elements must be range from 1 to n
def printfrequency(arr, n): 
    #Practise Yourself :  Write your code Here 
    
    for i in range(0, n):
        arr[i] -= 1
        
    for i in range(0, n):
        arr[arr[i] % n] = n + (arr[arr[i] % n])
        
    for i in range(0, n):
        print("Frequency of ", i+1, " = ", (arr[i]//n))
        
    return None 
  
arr = [2, 3, 3, 2, 5] 
n = len(arr) 
printfrequency(arr, n) 