def UIn():
    x = input('Enter a word: ')

    return x


def numVowel(x):
    v = 0
    vowel = ['a', 'i', 'o', 'u', 'e']

    for b in x:
        for i in range(5):
            if b.lower() == vowel[i]:
                v += 1

    return print(v)


def main():
    numVowel(UIn())


main()
