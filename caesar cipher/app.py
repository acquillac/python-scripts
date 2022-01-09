# Source:
# https://www.youtube.com/watch?v=JEsUlx0Ps9k
# NeuaralNine
import sys
import string

# get user input
message = input("Enter your message: ")

# setting charaters to shift by
shift = 1

# if contains numbers exit
textonly = message.isalpha()
if textonly == False:
  print("Message must only contain alphabetic characters")
  sys.exit()

# mapping alphabet to shifted alphabet
alphabet = string.ascii_lowercase
shifted = alphabet[shift:] + alphabet[:shift]
table = str.maketrans(alphabet, shifted)

# translating message to shifted charaters
encrypted = message.translate(table)

# printing encrypted message
print(encrypted)
