vowel = "аяуюоеёэиыaeiouyбвгджзйклмнпрстфхцчшщbcdfghjklmnpqrstvwxz"
while True:
    a,b = 0,0
    word = input("Enter a word or 'exit' to quit: ")
    if word == 'exit':
        break
    else:
        for i in range (0, len(word)):
            for k in range (0, len(vowel)):
                if word.casefold()[i] == vowel[k]:
                    if 16 > k:
                        a += 1
                    else:
                        b += 1
        if a == 0 and b == 0 or word.isnumeric():
            print("no letters")
            continue
        c = a / (a+b) * 100
        print(f'Word: {word}\n' f'Number of letters: {a+b}\n' f'Consonants: {b}\n'
            f'Vowels: {a}\n' f'Vowels/Consonants: {round(c, 2)}% / {100 - round(c, 2)}%')