import random

#random word generator:
with open("Catchphrase-Words.txt", "r") as file:
    allText = file.read()
    words = list(map(str, allText.splitlines()))

# print random string
    print(random.choice(words))

#beeper sound:
from playsound import playsound
import random
BEEPER = ('catchphrase.mp3', 'catchphrase_26_sec.mp3','catchphrase_15_sec.mp3','catchphrase_36_sec')

playsound(random.choice(BEEPER))
