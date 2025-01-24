'''Problem Statement:
Given an array of positive integers arr[], return the second largest element from the array. If the second largest element doesn't exist then return -1.
Note: The second largest element should not be equal to the largest element.'''


# Approach 1
# class Solution:
#     def getSecondLargest(self, arr):
#         # Code Here
#         n = 2
#         if len(arr)<n:
#             return -1
        
#         arr.sort(reverse = True)
        
#         for i in range (1, len(arr)):
#             if arr[i] != arr[0]:
#                 return arr[i]
        
#         return -1

# Approach 2
def getSecondLargest(arr):
        
    if len(arr)<2:
        return -1
            
    first = second = float("-inf")
        
    for num in arr:
        if num > first:
            second = first
            first = num
        elif num > second and num != first:
            second = num
                
    if second == float("-inf"):
        return -1
    else:
        return second 

if __name__ == "__main__":
    arr = [12, 35, 1, 10, 34, 1]
    print(getSecondLargest(arr))
