# There are N children standing in a line with some rating value. You want to distribute a minimum number of candies to these children such that: Each child must have at least one candy. The children with higher ratings will have more candies than their neighbors. You need to write a program to calculate the minimum candies you must give.

# Example:

# Input: arr[] = [1, 5, 2, 1]
# Output: 7
# Explanation: Candies given = [1, 3, 2, 1]
# Problem level: Medium

class Point: 
    def __init__(self, x, y): 
        self.x = x 
        self.y = y 
# Returns true if two rectangles(S, P) and (S1, P1) overlap   
def checkOverlapRectangle(S, P, S1, P1): 
    # If one rectangle is on left side of other 
    #Practise Yourself :  Write your code Here 
    if ((S.x < P1.x) and (S.y > P1.y)) or ((S1.x < P.x) and (S1.y > P.y)):
        return True
    return False
  
if __name__ == "__main__": 
    S = Point(0, 10) 
    P = Point(10, 0) 
    S1 = Point(5, 5) 
    P1 = Point(15, 0) 
  
    if(checkOverlapRectangle(S, P, S1, P1)): 
        print("Rectangles Overlap") 
    else: 
        print("Rectangles Don't Overlap") 