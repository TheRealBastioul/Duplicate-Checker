#This is used for missing_letters() to search for missing letters
alphabet = "abcdefghijklmnopqrstuvwxyz"
#This function is utilized in missing_letters() it creates a dictionary that is used to count how many times a key appears in the specified parameter.
def histogram(s):
    d = dict()
    for c in s:
        if c not in d:
            d[c] = 1
        else:
            d[c] += 1
    return d
#This function is used to test a string for duplicate characters. It prints to the console which characters are repeated, and how many times it is repeated.
def has_duplicates(b):
    testdupe = []
    for i in b:
        testdupe.append(i)
    whichdupe = {i:testdupe.count(i) for i in testdupe}
    t = 0
    for i in whichdupe:
        if whichdupe[i] > 1:
            t += 1
            print(f'{word} has {whichdupe[i]} "{i}" characters ')
        else:
            pass
    if t > 0:
        print(f'{word} has duplicates')
    else:
        print(f'{word} does not have duplicates')
#This function is used to test which characters are missing in a string.
def missing_letters(runit):
    alphadict = histogram(alphabet)
    missing = ()
    for i in runit:
        for key, value in alphadict.items():
            if key == i:
                alphadict[i] += 1
    for key, value in alphadict.items():
        if value > 1:
            pass
        else:
            missing += key,
    return ', '.join(missing)
#Below is used to initiate the algorithm in the console.
word = str(input('Please enter a word to test for duplicates and missing letters:'))
whatmissing = missing_letters(word)
if whatmissing == '':
    print(f'{word} uses all the letters')
else:
    print(f'{word} is missing letters {whatmissing}')
    has_duplicates(word)