import requests
import base64

a = requests.post("https://www.hackthebox.eu/api/invite/generate")
b = a.json()
print(b)
if b["success"] == 1:
	password = b["data"]["code"]
	print(base64.b64decode(password).decode())
else:
	print("Failed")