import requests

url = "https://"
url += "\x65"
url += "\x78"
url += "\x61"
url += "\x6D"
url += "\x70"
url += "\x6C"
url += "\x65."
url += "\x63"
url += "\x6F"
url += "\x6D"

print(url)
r = requests.get(url)
if 'domain' in r.text.lower():
	print(":)")
else:
	print(":(")