
def getMostTimeStopped(data, id):
    stop_positions = {}
    positions = data['positions']

    for i in range(len(positions) - 1):
        if positions[i]['velocidad_instantanea'] == 0:
            date1 = datetime.strptime(positions[i]['fecha'], "%Y/%m/%d %H:%M:%S")
            date2 = datetime.strptime(positions[i+1]['fecha'], "%Y/%m/%d %H:%M:%S")
            stop_positions[i] = (date2-date1).total_seconds()

    max_id = max(stop_positions, key=stop_positions.get) if stop_positions else 0

    return {
        "ID": id,
        "Número de puntos": len(positions),
        "Kms recorridos": data['distance'],
        "Latitud más tiempo": positions[max_id]['latitud'],
        "Longitud más tiempo": positions[max_id]['longitud']
    }