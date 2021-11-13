# Distribute Candy
# Asked In: FlipkartAmazonMicrosoft
# There are N children standing in a line with some rating value. You want to distribute a minimum number of candies to these children such that: Each child must have at least one candy. The children with higher ratings will have more candies than their neighbors. You need to write a program to calculate the minimum candies you must give.

# Example:

# Input: arr[] = [1, 5, 2, 1]
# Output: 7
# Explanation: Candies given = [1, 3, 2, 1]


class Main:
    def candy(self,ratings):
      if (ratings == None or len(ratings) == 0):
         return 0
         
      left = [0] * len(ratings)
      left[0] = 1
      right= [0] * len(ratings)
      right[len(ratings)-1] = 1
      result = 0

      for i in range(1,len(ratings),1):
        if (ratings[i] > ratings[i - 1]):
         left[i] = left[i - 1] + 1
      else:
         left[i] = 1
 
      for i in range(len(ratings) - 2,-1,-1):
        cur = 1
        if (ratings[i] > ratings[i + 1]):
          right[i] = right[i + 1] + 1
        else:
          right[i] = 1
			
      for i in range(0,len(ratings),1):
        result += max(right[i], left[i])
		    
      return result
	
m = Main()
ratings = [1,5,2,1]
result = m.candy(ratings)
print(result)
