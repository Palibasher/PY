import requests

def get_api_key(email: str, passwd: str):
   headers = {
       'email': email,
       'password': passwd,
   }
   res = requests.get('https://petfriends.skillfactory.ru/api/key', headers=headers)
   status = res.status_code
   try:
       result = res.json()
   except json.decoder.JSONDecodeError:
       result = res.text
   return status, result


apikey = get_api_key('vasya@mail.com','12345')
# print(apikey[1]["key"])
headers2 = {
    'auth_key': apikey[1]["key"]
}

respons = requests.get('https://petfriends.skillfactory.ru/api/pets', headers=headers2)
print(respons.text)

