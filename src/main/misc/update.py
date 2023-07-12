import requests

r = requests.get('https://raw.githubusercontent.com/MrWalper/mega-walper-gamer/main/src/main/misc/versions')
r.text()

print(r)

