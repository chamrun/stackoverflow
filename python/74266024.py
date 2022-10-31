wrong = []

print("Hi, We're gonna play a guessing game. When asked enter a number between -10 and 10.\n"
      "If not correct you'll have to guess again ^-^")

num = int(input("number: "))

# looping
while num != -1:
    wrong.append(num)
    num = int(input("Nope, guess again: "))

av = sum(wrong) / len(wrong)
print(f"You got it! The average of your wrong answers is: {av}\nThe End")
