import random

# random word generator:
with open ("Catchphrase-Words.txt", "r") as file:
    allText = file.read ()
    words = list (map (str, allText.splitlines ()))
    # print random string
    print (random.choice (words))
