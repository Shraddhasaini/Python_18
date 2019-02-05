#if an array has two 3 together
def three(nums):
    for i in range(0,len(nums)-1):
        if nums[i:i+2] == [3,3]:
            return True

    return False
print(three([1,2,3,3,4]))
