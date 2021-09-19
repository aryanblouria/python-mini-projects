import random
import pyperclip


def leetify(message):
    leet = ""
    leetmap = {
        'a': ['4', '@'],
        'b': ['13', '6'],
        'c': ['(', '{'],
        'd': ['[)', '|)'],
        'e': ['3', '[-'],
        'f': ['|=', ']='],
        'g': ['9', '(_+'],
        'h': ['#', '|-|'],
        'i': ['!', '|'],
        'j': ['_|', '_)'],
        'k': ['|<', '|{'],
        'l': ['1', '|_'],
        'm': ['|\/|', '44'],
        'n': ['|\|', '/\/'],
        'o': ['0', '()'],
        'p': ['|>', '|o'],
        'q': ['(,)', '0,'],
        'r': ['|2', '/2'],
        's': ['$', '5'],
        't': ['-|-', '+'],
        'u': ['(_)', '[_]'],
        'v': ['\/'],
        'w': ['\/\/', 'vv'],
        'x': ['><', '}{'],
        'y': ['`/', '`('],
        'z': ['2', '3']
    }

    for char in message:
        if char.lower() in leetmap.keys() and random.random() < 0.5:
            leet += random.choice(leetmap[char.lower()])
        else:
            leet += char
    return leet


while True:
    original = input("\nEnter the message: ")
    leeted = leetify(original)
    pyperclip.copy(leeted)
    print(f"Leetspeak for \"{original}\" is \"{leeted}\"")

    to_continue = input("Would you like to leetify another message? (y/n): ")
    while to_continue.lower() == 'n':
        print("\nWhy would you not want to leetify all day every day? Please reconsider.")
        to_continue = input("Would you like to leetify another message? (y/n): ")
