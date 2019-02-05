#for every character in the original there are three characters
def paperdoll(text):
    result = ''
    for char in text:
        result += char*3
    return result
print(paperdoll("wish"))
