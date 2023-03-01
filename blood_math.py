import requests


server = "http://vcm-7631.vm.duke.edu:5002"

r = requests.get(server + "/get_patients/vt51")
# print(r)
# print(type(r))
# print(r.status_code)
# print(r.text)
branches = r.json()
print(branches)

r_pat1 = requests.get(server + "/get_blood_type/F7")
print(r_pat1.text)

r_pat2 = requests.get(server + "/get_blood_type/F4")
print(r_pat2.text)

# NOT an acceptable match -- Donor is AB+ and can receive any blood type;
# Recipient is B- and can only receive B- and O-

out_data = {"Name": "vt51", "Match": "No"}
r2 = requests.post(server + "/match_check", json=out_data)
print(r2.text)
