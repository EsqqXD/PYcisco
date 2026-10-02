from urllib.request import urlopen
from urllib.parse import quote
from json import load

cidade = input("digite uma cidade: ")

# buscar coordenadas
url = f"https://geocoding-api.open-meteo.com/v1/search?name={quote(cidade)}&count=1"
dados = load(urlopen(url))

if "results" not in dados:
    print("Cidade não encontrada.")
    exit()

local = dados["results"][0]
lat = local["latitude"]
lon = local["longitude"]
nome = local["name"]

# buscar clima
url = (
    f"https://api.open-meteo.com/v1/forecast"
    f"?latitude={lat}&longitude={lon}"
    f"&current=temperature_2m,precipitation,weather_code"
)
clima = load(urlopen(url))["current"]

print(f"\ncidade: {nome}")
print(f"temperatura: {clima['temperature_2m']}°C")
print(f"chuva: {clima['precipitation']}mm")
print(f"codigo do tempo: {clima['weather_code']}")
