from tkinter import filedialog
import base64
import requests


# select image to upload
def select_image():
    filename = filedialog.askopenfilename(initialdir="Images")
    return filename


# convert image file to base64 string
def convert_image_file_to_base_64_string(filename):
    with open(filename, "rb") as image_file:
        b64_bytes = base64.b64encode(image_file.read())
    b64_string = str(b64_bytes, encoding='utf-8')
    return b64_string


# upload base64 string to server
def upload_b64_string(b64_string):
    out_json = {"image": b64_string,
                "net_id": "vt51",
                "id_no": 2}
    r = requests.post("http://vcm-21170.vm.duke.edu/add_image", json=out_json)
    print(r.text)


# download watermark-ed image
def download_image():
    r = requests.get("http://vcm-21170.vm.duke.edu/get_image/vt51/2")
    print(r.text)
    return r.text


def main():
    filename = select_image()
    if filename == "":
        return
    b64_image = convert_image_file_to_base_64_string(filename)
    print(b64_image)
    upload_b64_string(b64_image)
    newb64 = download_image()
    image_bytes = base64.b64decode(newb64)
    with open("watermark.jpg", "wb") as out_file:
        out_file.write(image_bytes)


if __name__ == '__main__':
    main()
