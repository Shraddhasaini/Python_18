#if an array has two 3 together
def three(arr):
    for i in range(0,len(arr)-1):
        if arr[i] == 3 and arr[i+1] == 3:
            return True
    return False
print(three([1,2,3,4]))
