#true if n is within 10 of either 100 or 200
def almostthere(x):
    return (abs(100-x) <= 10) or (abs(200-x) <= 10)#absolute  value function
print(almostthere(111))
