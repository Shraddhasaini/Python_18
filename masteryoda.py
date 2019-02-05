#sentence with the words reversed
def masteryoda(sentence):
    wordlist = sentence.split()
    reversedwordlist = wordlist[::-1]
    return ' '.join(reversedwordlist)
print(masteryoda("shraddha loves dog"))
