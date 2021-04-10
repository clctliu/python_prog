import string
import random

letters = string.ascii_lowercase
print(letters)

for i in range(5):
    #create a new random filename
    filename = ''
    for j in range(5):
        filename = filename + random.choice(letters)
    filename = filename + '.txt'
    f = open(filename, "a")
    f.write("I am a dummy file")
    f.close