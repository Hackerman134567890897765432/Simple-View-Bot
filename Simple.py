# This is made by Code.x #0001 so if you need help dm me.

# The number in the 8th line is the amount of views btw.

import webbrowser, time
url = input("Enter url: ")
duration = input("Enter duration: ")
for i in range(5):
    webbrowser.open_new(url)
    time.sleep(int(duration))