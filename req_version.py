import requests
r = requests.get("https://raw.githubusercontent.com/luketk97/cmput404lab1/master/req_version.py")
print(r.content)