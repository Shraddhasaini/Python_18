#function takes a two-word string and returns True if both words begin with same letter
def animal_crackers(text):
    wordlist = text.split()
    firstword = wordlist[0]
    secondword = wordlist[1]
    return firstword[0] == secondword[0]
print(animal_crackers("Ankit Kundu"))
