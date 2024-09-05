# This is a sample Python script.
import requests
from datetime import datetime
import pandas as pd

# CF5459
# CF5419
# CF5420
# CF5421
# CF5422
# CF5424
# CF5430
# CF5432
# CF5433
# CF5434
# CF5442
# CF5448
# CF5450
# CF5452
# CF5453
# CF5456
# CF5457
# CF5463
# CF5466
# CF5472
# CF5474
# CF5490
# CF5491
# CF5587
# CF5503
# CF5504
# CF5601
# CF5603
# CF5604
# CF5611
# CF5612
# CF5615
# CF5616
# CF5617
# CF5619
# CF5622
# CF5625
# CF5626
# CF5630
# CF5632
# CF5634
# CF5635
# CF5636
# CF5637
# CF5642
# CF5646
# CF5650
# CF5657
# CF5657



def callApi(id):
    url = "https://secure.parkingverde.com/apicentinela.php?f=centinela_track&id=" + id + "&id_cliente=159&fecha_desde=2023-09-01"
    cookies = {
        'PHPSESSID': '5joqavifejjnaamenjqfdd9f3s'
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

# List of all IDs
ids = [
    'CF5459', 'CF5419', 'CF5420', 'CF5421', 'CF5422', 'CF5424', 'CF5430', 'CF5432', 'CF5433', 'CF5434',
    'CF5442', 'CF5448', 'CF5450', 'CF5452', 'CF5453', 'CF5456', 'CF5457', 'CF5463', 'CF5466', 'CF5472',
    'CF5474', 'CF5490', 'CF5491', 'CF5587', 'CF5503', 'CF5504', 'CF5601', 'CF5603', 'CF5604', 'CF5611',
    'CF5612', 'CF5615', 'CF5616', 'CF5617', 'CF5619', 'CF5622', 'CF5625', 'CF5626', 'CF5630', 'CF5632',
    'CF5634', 'CF5635', 'CF5636', 'CF5637', 'CF5642', 'CF5646', 'CF5650', 'CF5657'
]

# Create an empty list to store results
results = []

# Loop through all IDs
for id in ids:
    url = f"https://secure.parkingverde.com/apicentinela.php?f=centinela_track&id={id}&id_cliente=159&fecha_desde=2023-09-01"
    cookies = {
        'PHPSESSID': '5joqavifejjnaamenjqfdd9f3s'
    }

    response = requests.get(url, cookies=cookies)
    if response.status_code == 200:
        data = response.json()
        result = getData(data, id)
        results.append(result)
    else:
        print(f"Error for ID: {id}")

# Create a pandas DataFrame from the results
df = pd.DataFrame(results)

# Calculate average battery life for each ID
average_battery = df.groupby('id')['bateria'].mean().reset_index()
average_battery.columns = ['ID', 'Average Battery']

# Display the average battery life for each ID
print("Average Battery Life for each ID:")
print(average_battery)

# Optionally, save the average battery life to a CSV file
average_battery.to_csv('average_battery_life.csv', index=False)

print("Average battery life for each ID saved to 'average_battery_life.csv'")

# Get a sample of 2000 random rows
sample_df = df.sample(n=2000, random_state=42)

# Save the sample DataFrame to a new CSV file
sample_df.to_csv('bicycle_data_sample.csv', index=False)

print("Sample of 2000 random rows saved to 'bicycle_data_sample.csv'")

# Optionally, save the DataFrame to a CSV file
# df.to_csv('bicycle_data.csv', index=False)

# Read the CSV file
df = pd.read_csv('bicycle_data.csv')

# Calculate average battery life for each ID
average_battery = df.groupby('id')['bateria'].mean().reset_index()
average_battery.columns = ['ID', 'Average Battery']

# Display the average battery life for each ID
print("Average Battery Life for each ID:")
print(average_battery)

# Optionally, save the average battery life to a CSV file
average_battery.to_csv('average_battery_life.csv', index=False)

print("Average battery life for each ID saved to 'average_battery_life.csv'")
