import random
import pyperclip
from leetmap import leetmap


def leetify(message):
    leet = ""
    for char in message:
        if char.lower() in leetmap.keys() and random.random() < 0.5:
            leet += random.choice(leetmap[char.lower()])
        else:
            leet += char
    return leet


stop = False
while not stop:
    original = input("\nEnter the message: ")
    leeted = leetify(original)
    pyperclip.copy(leeted)
    print(f"Leetspeak for \"{original}\" is \"{leeted}\"")

    to_continue = input("Would you like to leetify another message? (y/n): ")
    while to_continue.lower() == 'n':
        print("\nWhy would you not want to leetify all day every day? Please reconsider.")
        to_continue = input("Would you like to leetify another message? (y/n): ")

