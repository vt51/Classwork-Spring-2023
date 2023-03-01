import requests


r = requests.get("https://api.github.com/repos/vt51/Classwork_Spring2023/branches")
print(r)
print(type(r))
print(r.status_code)
print(r.text)
branches = r.json()
print(branches)
for branch in branches:
    print(branch["name"])