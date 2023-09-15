import lxml.etree as et
from collections import Counter

doc = et.parse('DATA/presidents.xml')

root = doc.getroot()
print(f"root: {root}")

# E.find()  E.findall()

pres_counter = Counter()
for state_element in doc.findall('.//birthstate'):
    state = state_element.text
    print(state)
    pres_counter[state] += 1

print('-' * 60)

print(pres_counter)

print('-' * 60)

for pres_element in doc.findall('president'):
    name_element = pres_element.find('name')
    print(name_element.findtext('first'), name_element.findtext('last'))
