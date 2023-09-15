import json
from pprint import pprint

with open('DATA/solar.json') as solar_in:
    solar_data = json.load(solar_in)

#  json.load(file_object)
#  json.loads(str)
pprint(solar_data)
print('-' * 60)

all_planets = (
    solar_data['innerplanets'] +
    solar_data['outerplanets'] +
    solar_data['dwarfplanets']
)

for planet in all_planets:
    print(planet['name'])
    
