import sys

texte=""
for arg in sys.argv[1::]:
    texte+=arg+" "
texte=texte[::-1].swapcase()
print(texte)
print(len(sys.argv))