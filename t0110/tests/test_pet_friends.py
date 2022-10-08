import os
from settings import email, passwrd
from api import PetFriends

PF = PetFriends()

def get_api_key_for_valid_user(email=v_email, password=passwrd):
    status,result = PF.get_api_key(email, password)
    assert status == 200
    assert "key" in result