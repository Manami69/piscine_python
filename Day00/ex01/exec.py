import sys

texte=""
j = len(sys.argv) - 1
for i in range(1, len(sys.argv)):
    if i < j:
        texte += sys.argv[i]+" "
    else:
        texte += sys.argv[i]
texte=texte[::-1].swapcase()
print(texte)
