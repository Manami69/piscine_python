import sys

texte = ""
j = len(sys.argv) - 1
for i in range(1, len(sys.argv)):
    if i < j:
        texte += sys.argv[i]+" "
    else:
        texte += sys.argv[i]

    for i in range(len(texte)):
        if not(texte[i].isalnum() is True or texte[i].isspace() is True):
            print("ERROR")
            sys.exit()

MORSE_CODE_DICT = {'A': '.-', 'B': '-...',
                   'C': '-.-.', 'D': '-..', 'E': '.',
                   'F': '..-.', 'G': '--.', 'H': '....',
                   'I': '..', 'J': '.---', 'K': '-.-',
                   'L': '.-..', 'M': '--', 'N': '-.',
                   'O': '---', 'P': '.--.', 'Q': '--.-',
                   'R': '.-.', 'S': '...', 'T': '-',
                   'U': '..-', 'V': '...-', 'W': '.--',
                   'X': '-..-', 'Y': '-.--', 'Z': '--..',
                   '1': '.----', '2': '..---', '3': '...--',
                   '4': '....-', '5': '.....', '6': '-....',
                   '7': '--...', '8': '---..', '9': '----.',
                   '0': '-----', ', ': '--..--', '.': '.-.-.-',
                   '?': '..--..', '/': '-..-.', '-': '-....-',
                   '(': '-.--.', ')': '-.--.-'}

for i in range(len(texte)):
    letter = texte[i].upper()
    if letter.isspace() is True:
        print("/", end=" ")
    else:
        print("{}".format(MORSE_CODE_DICT[letter]), end=" ")
print("")
