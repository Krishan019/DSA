# Problem Statement
'''You are given an array arr[] of non-negative integers. 
Your task is to move all the zeros in the array to the right end while maintaining the relative order of the non-zero elements. 
The operation must be performed in place, meaning you should not use extra space for another array.'''


def pushZerosToEnd(arr):
        
    count = 0
        
    for i in range (len(arr)):
        if arr[i] != 0:
            arr[count], arr[i] = arr[i], arr[count]
            count += 1

if __name__ == "__main__":
    arr = [1, 6, 0, 4, 3, 0, 5, 0]
    pushZerosToEnd(arr)

    # Print the modified array
    for num in arr:
        print(num, end=" ")