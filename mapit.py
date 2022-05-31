import webbrowser, sys, pyperclip

sys.argv

if len(sys.argv) > 1:
    address = ' '.join(sys.argvs[1:])
else:
    address = pyperclip.paste()

#https://www.google.com/maps/search/<ADDRESS>
webbrowser.open('https://www.google.com/maps/search/' + address)
