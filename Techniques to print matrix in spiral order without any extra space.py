# Techniques to print matrix in spiral order without any extra space
# Asked In: MicrosoftOLAPayTmOracle
# you are given a matrix of m x n elements (m rows, n columns), Print all elements of the matrix in spiral order in O(m*n) Time Complexity and O(1) Space Complexity Asked in: Microsoft, OLA, PayTm, Oracle

# Example:

# Input:
# [
# [ 1, 2, 3 ],
# [ 4, 5, 6 ],
# [ 7, 8, 9 ]
# ]
# Output: [1,2,3,6,9,8,7,4,5]

# Hint 1 : Divide the matrix in different layers and print numbers from outer to inner layer

def spiralPrint(m, n, matrix) : 
    #Practise Yourself :  Write your code Here 
    k = p = 0
    n = n - 1
    m = m - 1
    while (p<m and k<n):
        for i in range(k, n):
            print(matrix[p][i], end = " ")
        k += 1
        for i in range(p, m):
            print(matrix[i][n], end = " ")
        p += 1
        for i in range(n, k-1, -1):
            print(matrix[m][i], end = " ")
        n -= 1
        for i in range(m, p-1, -1):
            print(matrix[i][k-1], end = " ")
        m -= 1
    
    return None
  
matrix = [ [1, 2, 3, 4], 
      [5,6,7,8], 
      [9, 10, 11, 12],
      [13, 14, 15, 16] ] 
        
R = 4; C = 4
spiralPrint(R, C, matrix)