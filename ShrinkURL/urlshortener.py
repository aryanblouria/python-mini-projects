from pyshorteners import Shortener
import config
import pyperclip

shortener = Shortener(api_key=config.API_key)

finish = False
while not finish:
    choice = int(input(
        '''\nWelcome to the URL Shortener Service.
    1. Enter the URL Manually
    2. Automatically Get URL from Clipboard
    3. Get me out of this goddamn loop
    \nYou choose: '''))

    if choice == 1:
        url = input("Enter URL: ")
    elif choice == 2:
        url = pyperclip.paste()
    elif choice == 3:
        finish = True
        break

    short_url = shortener.bitly.short(url)
    print("The shortened URL: " + short_url)

    long_url = shortener.bitly.expand(short_url)
    print("The expanded URL: " + long_url)

print("Hmph, what kinda dude gives up on shortening URLs?")

