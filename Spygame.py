def spy(nums):
    code = [0,0,7,'x']
    for num in nums:
        if num == code[0]:
            code.pop(0)
    return len(code) == 1
print(spy([1,2,3,0,23,0,67,7,0]))
