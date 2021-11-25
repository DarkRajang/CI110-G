#
def UIn():
    return input('Enter a character: ')


def isVowel(x):
    # checking character
    vowel = ['a', 'i', 'o', 'u', 'e']
    for i in range(6):
        if x.lower() == vowel[i]:
            return True
        else:
            return False


def main():
    print(isVowel(UIn()))


main()
