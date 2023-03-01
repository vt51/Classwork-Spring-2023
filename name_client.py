import requests

# out_data = {"name": "Vanessa Tam", "net_id": "vt51",
#             "e-mail": "vanessa.tam@duke.edu"}
# r = requests.post("http://vcm-21170.vm.duke.edu:5000/student", json=out_data)
# print(r.status_code)
# print(r.text)
#
# r = requests.get("http://vcm-21170.vm.duke.edu:5000/list")
# print(r.text)


out_data = {"user": "rdh46", "message": "hi"}
r = requests.post("http://vcm-21170.vm.duke.edu:5001/add_message", json=out_data)
print(r.text)

retrieve = requests.get("http://vcm-21170.vm.duke.edu:5001/get_messages/vt51")
print(retrieve)
print(type(retrieve))
print(retrieve.text)
list = retrieve.json()
print(list)