#%%
import requests
from tools import Sign

URL = "http://localhost:5000/stats"


def get_stats(name: str):  # get
    response = requests.get(URL, json={"name": name})
    if response.status_code == 200:
        return response.json()
    return None


def create_ifn_exist(name: str):  # put
    response = requests.put(URL, json={"name": name})
    if response.status_code == 200:
        return response.json()["message"] == "True"
    return None


def add_value(name: str, sign: Sign):  # patch
    response = requests.patch(URL, json={"name": sign.name, "sign": sign.name})
    if response.status_code == 200:
        return response.json()["message"] == "True"
    return None


def use_DSGVO(name: str):  # put
    response = requests.delete(URL, json={"name": name})
    if response.status_code == 200:
        return response.json()["message"] == "True"
    return None
