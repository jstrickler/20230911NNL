import requests

URL = "https://navalnuclearlab.energy.gov/"

response = requests.get(URL)

if response.status_code == requests.codes.OK:
    html = response.text
    print(html)
