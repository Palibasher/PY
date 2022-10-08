from requests_toolbelt.multipart.encoder import MultipartEncoder
class PetFriends:
    def __int__(self):
        self.base_url = "https://petfriends.skillfactory.ru/"

    def get_api_key(self, email, password):
        headers = {
            'email': email,
            'password': passwrd,
        }
        res = requests.get(f"{self.base_url}api/key", headers=headers)
        status = res.status_code
        try:
            result = res.json()
        except json.decoder.JSONDecodeError:
            result = res.text
        return status, result