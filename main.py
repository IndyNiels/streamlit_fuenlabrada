# This is a sample Python script.
import requests

def callApi(id):
    url = "https://secure.parkingverde.com/apicentinela.php?f=centinela_track&id=" + id + "&id_cliente=159&fecha_desde=2023-09-01"
    cookies = {
        'PHPSESSID': 'l82cabmjkdlqhf59qmep6cdlba'
    }

    response = requests.get(url, cookies=cookies)
    if response.status_code == 200:
        data = response.json()
        getData(data)
    else:
        print("error")


def getData(data):
    positions = data['positions']

    print("Número de puntos: ", len(positions))
    print("Kms recorridos: ", data['distance'])


callApi('CF5442')
