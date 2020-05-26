import sys


if len(sys.argv) != 3:
    print("ERROR")
    sys.exit()

string = sys.argv[1]
if (string.isdigit() is True):
    print("ERROR")
    sys.exit()

try:
    nb = int(sys.argv[2])
except ValueError:
    print("ERROR")
    sys.exit()

text = ""
for i in range(len(string)):
    if (string[i].isalpha() is True):
        text += string[i]
    else:
        text += '#'

liste = text.split('#')
result = []
for i in range(len(liste)):
    lenw = len(liste[i])
    if lenw > nb:
        result.append(liste[i])

print(result)
