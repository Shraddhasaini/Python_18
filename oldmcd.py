#capitalizes the first and fourth letters of a name
def oldmcd(name):
    firstpart = name[:3].capitalize()
    secondpart = name[3:].capitalize()
    return firstpart + secondpart
print(oldmcd("macdonald"))
