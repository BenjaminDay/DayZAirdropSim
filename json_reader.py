import json
with open('AirdropSettings.json', 'r') as file:
    data = json.load(file)

for container in data['Containers']:
    for item in container['Loot']:
        item['Chance'] = round(item['Chance'], 2)

with open('your_file.json', 'w') as file:
    json.dump(data, file, indent=2)
