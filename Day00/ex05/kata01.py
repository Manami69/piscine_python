languages = {
'Python': 'Guido van Rossum',
'Ruby': 'Yukihiro Matsumoto',
'PHP': 'Rasmus Lerdorf',
}

for key in languages.keys():
    print("{:s} was created by {:s}".format(key, languages[key]))
