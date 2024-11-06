import requests

link = 'https://csf101-server-cap1.onrender.com/get/input/336'
request_file = requests.get(link)
with open('336.txt', 'wb') as file:
    file.write(request_file.content)

print("Download 336.txt")