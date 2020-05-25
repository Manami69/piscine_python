import sys



if  len(sys.argv) != 3:
    print("ERROR")
    sys.exit()

string = sys.argv[1]
if  (string.isdigit() == True):
    print("ERROR")
    sys.exit()

try:
    nb = int(sys.argv[2])
except:
    print("ERROR")
    sys.exit()

text = ""
for i in range(len(string)):
    if (string[i].isalpha() == True):
        text+= string[i]
    else:
        text+= '#'

liste = text.split('#')
result = []
for i in range(len(liste)):
    l = len(liste[i])
    if l > nb:
        result.append(liste[i])

print(result)