import requests
import json

class ConversionExeptions(Exception):
    pass

class Converter:
    @staticmethod
    def get_ammount(what_we_need: str, what_we_have: str, ammount: int):
        url = f"https://api.apilayer.com/exchangerates_data/convert?to={what_we_need}&from={what_we_have}&amount={ammount}"
        payload = {}
        headers = {
            "apikey": "GXHkU6a8iufOWo8nYKkXcLJETEQz8QyK"
        }
        response = requests.request("GET", url, headers=headers, data=payload)
        status_code = response.status_code
        result = response.text
        result_py = json.loads(response.content)
        print(status_code, result_py)
        if result_py['success'] == True:
            return result_py['result']
        else:
            return "Ошибка сервера"