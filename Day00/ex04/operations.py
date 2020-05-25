import sys


def printerror(texte=""):
    print("{0}Usage: python operations.py <number1> <number2>\nExample:\n\t\
python operations.py 10 3".format(texte))


if len(sys.argv) > 3:
    printerror("InputError: too many arguments\n\n")
elif len(sys.argv) == 1:
    printerror()
elif len(sys.argv) < 3:
    printerror("InputError: too few arguments\n\n")
else:
    try:
        nb1 = int(sys.argv[1])
        nb2 = int(sys.argv[2])
        print("Sum:\t\t{0}\nDifference:\t{1}\nProduct:\t{2}".format(
            nb1+nb2, nb1-nb2, nb1*nb2))
        if nb2 == 0:
            print("Quotient:\tERROR (div by zero)\nRemainder:\t\
ERROR (modulo by zero)")
        else:
            print("Quotient:\t{0}\nRemainder:\t{1}".format(nb1/nb2, nb1 % nb2))
    except ValueError:
        printerror("InputError: only numbers\n\n")
