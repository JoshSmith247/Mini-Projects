import json
import string

with open('Alphabet/dictionary.json', 'r') as file:
    output = file.read()
    data = json.loads(output)


#print(data.keys())

num = 0

for word in data:
    num += 1
    lastletterindex = 0
    #print(word)

    for letter in word:
        index = 0

        if (index == 0):
            print(letter)

        for obj in string.ascii_lowercase:
            if obj == letter:
                continue
            index += 1

        if (index >= lastletterindex):
            lastletterindex = index
            #if (lastletterindex == len(word)):
                #print(word)
        else:
            continue



print(num, "words total.")