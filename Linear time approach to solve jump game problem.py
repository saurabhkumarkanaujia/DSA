#You have an array of non-negative integers,you are initially positioned at the first index of the array.Each element in the array represents your maximum jump length at that position.Determine if you are able to reach the last index in O(n) Time complexity and O(1) Space Complexity Asked in: Adobe, Intuit

#Example:

#Input 1:
#A = [2,3,1,1,4]
#Input 2:
#A = [3,2,1,0,4]

#Output 1:
#2
#Explanation 1:
#Index 0 -> Index 2 -> Index 4 

#Output 2:
#0
#Explanation 2:
#There is no possible path to reach the last index return -1

def minJumpsToEnd(array, n): 
    #Practise Yourself
    a = array[0]
    b = array[0]
    jump = 1
    for i in range(1, len(array)):
        if i==len(array):
            return jump
        a = a-1
        b = b-1
        if array[i] > b :
            b = array[i]
        if a==0:
            a=b
            jump += 1
    return jump
   
  

array1 = [2,3,1,1,4] 
size = len(array1) 
   
# Calling the minJumpsToEnd function 
print("Minimum number of jumps to reach end is " ,minJumpsToEnd(array1, size)) 
   


