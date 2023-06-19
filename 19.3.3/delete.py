import requests


url = 'https://petstore.swagger.io/v2/store/order/123123'


headers = {
    'accept': 'application/json',
}


response = requests.delete(url, headers=headers)


print(response.status_code)
print(response.json())
