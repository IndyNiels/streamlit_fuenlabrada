# This is a sample Python script.
import requests
from datetime import datetime

def callApi(id):
    url = "https://secure.parkingverde.com/apicentinela.php?f=centinela_track&id=" + id + "&id_cliente=159&fecha_desde=2023-09-01"
    cookies = {
        'PHPSESSID': 'l82cabmjkdlqhf59qmep6cdlba'
    }

    response = requests.get(url, cookies=cookies)
    if response.status_code == 200:
        data = response.json()
        getData(data, id)
    else:
        print("error")


def getData(data, id):
    stop_positions = {}
    positions = data['positions']

    for i in range(len(positions)):
        if positions[i]['velocidad_instantanea'] == 0 and i<len(positions):
            date1 = datetime.strptime(positions[i]['fecha'], "%Y/%m/%d %H:%M:%S")
            date2 = datetime.strptime(positions[i+1]['fecha'], "%Y/%m/%d %H:%M:%S")
            stop_positions[i] = (date2-date1).total_seconds()

    max_id = max(stop_positions, key=stop_positions.get)

    print("Bicicleta nº", id)
    print("Número de puntos:", len(positions))
    print("Kms recorridos:", data['distance'])
    print("Donde ha pasado más tiempo la bici: " + str(positions[max_id]['latitud']) + ", " + str(positions[max_id]['longitud']))
    print("------------------------------------")

callApi('CF5442')
