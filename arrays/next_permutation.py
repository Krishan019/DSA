'''Problem Statement: Given an array of integers arr[] representing a permutation, implement the next permutation that rearranges the numbers into the lexicographically next greater permutation. 
If no such permutation exists, rearrange the numbers into the lowest possible order (i.e., sorted in ascending order).
Note - A permutation of an array of integers refers to a specific arrangement of its elements in a sequence or linear order.'''

def nextPermutation(arr):
    # code here
    n = len(arr)
        
    # Pivot index
    pivot = -1
        
    for i in range (n-2, -1, -1):
        if arr[i] < arr[i+1]:
            pivot = i
            break
        
    # If no pivot found then reverse the whole array 
    if pivot == -1:
        arr.reverse()
        return
        
    # Find the element form right that is greater than pivot element
    for j in range (n-1, pivot, -1):
        if arr[j] > arr[pivot]:
            arr[j], arr[pivot] = arr[pivot], arr[j]
            break
        
    # Reverse all the next elements from the pivot 
    left, right = pivot+1, n-1
        
    while left < right:
        arr[left], arr[right] = arr[right], arr[left]
            
        left += 1
        right -= 1
        
if __name__ == "__main__":
    arr = [2, 4, 1, 7, 5, 0]
    nextPermutation(arr)
    print(" ".join(map(str, arr)))