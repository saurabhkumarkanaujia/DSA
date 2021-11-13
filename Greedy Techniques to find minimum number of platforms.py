# Greedy Techniques to find minimum number of platforms
# Asked In:
# List of arrival and departure time is given, Find the minimum number of platforms are required for the railway as no train waits

# Example:

# Input ? The list of arrival time and the departure times, and the number of items in the list
# Input:  arr[]  = {9:00,  9:40, 9:50,  11:00, 15:00, 18:00}
# dep[]  = {9:10, 12:00, 11:20, 11:30, 19:00, 20:00}
# Output ? The number of minimum platforms is needed to solve the problem.
# Output: 3
# Hint1: The minimum number of platforms is nothing but the maximum number of trains that rest in the given railway station from the time limit between the arrival of the first train to the departure of the last train
# Hint2: Think of sorting Arrival or Departure timing of train 


def minimumNumberPlatform(arrival, departure, n): 
    
    #Practise Yourself :  Write your code Here 
    
    arrival.sort()
    departure.sort()
    i=j=platforms_needed=minPlatforms=0
    while(i<n and j<n):
        if (arrival[i] < departure[j]):
            platforms_needed+=1
            i+=1
            if (platforms_needed > minPlatforms):
                minPlatforms = platforms_needed
        else:
            platforms_needed-=1
            j+=1
    
    return minPlatforms
  
arrival = [100, 140, 150, 200, 215, 400] 
departure = [110, 300, 220, 230, 315, 600] 
n = len(arrival) 
  
print("Minimum Number Platforms = ", minimumNumberPlatform(arrival, departure, n))  