import string


def text_analyzer(*texte):
    """This function counts the number of upper characters, lower characters,
    punctuation and spaces in a given text."""
    if len(texte) > 1:
        print("ERROR")
    else:
        if len(texte) == 0:
            texte = input("What is the text to analyse?\n>> ")
        nbupper = 0
        nblower = 0
        nbponct = 0
        nbspace = 0
        for i in range(len(texte)):
            if texte[i].isupper():
                nbupper += 1
            elif texte[i].islower():
                nblower += 1
            elif texte[i] == " ":
                nbspace += 1
            elif texte[i] in string.punctuation:
                nbponct += 1
        print("The text contains {0} characters:\n- {1} upper letters\n\
- {2} lower letters\n- {3} punctuation marks\n- {4} spaces\
".format(len(texte), nbupper, nblower, nbponct, nbspace))
