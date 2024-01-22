#  generate random word
print("# WellCome to guss my name game\n\n")
import random
words = ["ermias","samuel","esrael","abrham","mike"]
word = words[int(len(words)*random.random())-1]
# hangman
hangman1="  ----*"
hangman2="  |   |"
hangman3="      |"
hangman4="      |"
hangman5="      |"
hangman6="______|"
# replece with dash
dashed = ''
for i in range (len(word)):
    dashed = dashed + '*'
print(dashed)

# ask user for a letter
count = 4
while count != 0 and "*" in dashed:
    letter = input("guss letter: ")
    if letter in word:
        dashed = dashed[:(word.index(letter))] + letter + dashed[((word.index(letter))+1):]
        word = word[:(word.index(letter))] + "*" + word[((word.index(letter))+1):]
        print(dashed)
        print(f"you have {count} lives out of 4.")
        if "*" not in dashed:
            print("u win")
            exit()
    else :
        count = count - 1 
        print(dashed)
        print(f"you have {count} lives out of 4.\n\n")
        if count == 0:
            print("game over")  
            if count == 3:
                hangman3="  O   |"
            elif count == 2:
                hangman4=" /|\  |"
            elif count == 1:
                hangman5=" /    |"
            else :
                hangman5=" / \  |"
            print(hangman1+'\n'+hangman2+'\n'+hangman3+'\n'+hangman4+'\n'+hangman5+'\n'+hangman6)
            print('_____________________________________'+'\n\n')
            exit()
    if count == 3:
        hangman3="  O   |"
    elif count == 2:
        hangman4=" /|\  |"
    elif count == 1:
        hangman5=" /    |"
    elif count == 0 :
        hangman5=" / \  |"
    print(hangman1+'\n'+hangman2+'\n'+hangman3+'\n'+hangman4+'\n'+hangman5+'\n'+hangman6+'\n\n')
    print('_____________________________________'+'\n\n')