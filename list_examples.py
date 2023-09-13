cities = []

cities.append('Albany')
cities.append("Schenectady")
cities.append("Mckeesport")
cities.append("Homestead")
print(f"cities: {cities}")
print(f"len(cities): {len(cities)}")
cities.insert(0, "Saratoga")
print(f"cities: {cities}")
cities.insert(3, "Moon")
print(f"cities: {cities}")
more_cities = ["Raleigh", "Durham", 'Chapel Hill', 'Apex']
cities.extend(more_cities)
print(f"cities: {cities}")

#  LIST.append(obj)   LIST.insert(pos, obj)   LIST.extend(iterable)

stuff = [1, 2, 3]
cities.append(stuff)
print(f"cities: {cities}")
print(f"cities[-1]: {cities[-1]}")
print(f"cities[-2]: {cities[-2]}")
print(f"cities[-1][1]: {cities[-1][1]}")

del cities[-1]
print(f"cities: {cities}")

del cities[2]
print(f"cities: {cities}")

cities.remove('Raleigh')
print(f"cities: {cities}")

city = cities.pop(2)
print(f"city: {city}")
print(f"cities: {cities}")

city = cities.pop()
print(f"city: {city}")
print(f"cities: {cities}")

#  del LIST[pos]   LIST.remove(value)   LIST.pop(pos)


