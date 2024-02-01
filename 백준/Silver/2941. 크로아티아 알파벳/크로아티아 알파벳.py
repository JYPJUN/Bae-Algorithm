sentence = input()

croatia_lang = ['c=', 'c-', 'dz=', 'd-', 'lj', 'nj', 's=', 'z=']

for i in croatia_lang:
    sentence = sentence.replace(i, '*')

print(len(sentence))