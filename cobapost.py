from flask import requests

mydata={"Nama":" Muhamad Amir", "Alamat" : "Bogor", "Usia" : "26"}
req=requests.post("http://127.0.0.1:5000/cobarequest", data=mydata)

print(req.text)