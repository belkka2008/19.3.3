# res = requests.post(url, headers=headers, data=data)
import requests


url = 'https://petstore.swagger.io/v2/pet'


headers = {
    'accept': 'application/json',
    'Content-Type': 'application/json'
}


data = {
    "id": 0,
    "category": {
        "id": 0,
        "name": "string"
    },
    "name": "doggie",
    "photoUrls": ["string"],
    "tags": [
        {
            "id": 0,
            "name": "string"
        }
    ],
    "status": "available"
}


response = requests.post(url, headers=headers, json=data)


print(response.status_code)
print(response.json())