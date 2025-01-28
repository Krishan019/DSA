def reverse(arr, start, end):
    while start < end:
        arr[start], arr[end] = arr[end], arr[start]
        start += 1
        end -= 1

def rotateArr(arr, d):
        n = len(arr)
        
        #Handling the cases where d > size of an array
        d %= n
        
        # Reverse the first d element
        reverse(arr, 0, d-1)
        
        #Reverse the remaining (n-d) element
        reverse(arr, d, n-1)
        
        #Reverse the entire array
        reverse(arr, 0, n-1)
        
if __name__ == "__main__":
    arr = [1, 2, 3, 4, 5, 6]
    d = 2

    rotateArr(arr, d)

    for i in range(len(arr)):
        print(arr[i], end=" ")