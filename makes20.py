#Given two integers, return True if the sum of the integers is 20 or if one of the integers is 20. If not, return False
def makes20(a,b):
    if a==20 or b==20:
        return True
    elif sum((a,b)) == 20:
        return True
    else:
        return False
print(makes20(12,8))
