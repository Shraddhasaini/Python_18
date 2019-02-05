#capitalizes the first and fourth letters of a name
def oldmcd(name):
    first = name[0].upper()
    inbetween = name[1:3]
    fourth = name[3].upper()
    rest = name[4:]
    return first + inbetween + fourth + rest
print(oldmcd("macdonald"))
