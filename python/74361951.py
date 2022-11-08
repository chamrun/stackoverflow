import random

pin = []
length = random.randrange(8, 15)

for i in range(length):
    pin.append(chr(random.randint(97, 122)))

number_of_uppercase_chars = random.randint(0, length)

for i in range(number_of_uppercase_chars):
    char_index = random.randint(0, length - 1)
    pin[char_index] = pin[char_index].upper()


pin = "".join(pin)
print(pin)
