import json

data= """{
    "name":"Adarsh Kumar",
    "mobile no.":"xxxxxxxxxx",
    "address":{
            "door no.":"xoxoxo",
            "pincode":"3l3l3l3"
            }
    }"""
#Mulltpile json 
data2 = """[
          {"id":"01",
            "name":"chuck"
          },
            {
            "id":"01",
            "name":"sony"
            }
            ]"""


info = json.loads(data)
info2 = json.loads(data2)

print("Name :",info["name"])
print("door no.",info["address"]["door no."])
p1=info2[0]["id"]
p2=info2[0]["name"]
print(f"ID {p1} ,name : {p2}")

    