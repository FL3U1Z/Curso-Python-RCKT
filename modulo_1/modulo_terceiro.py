print("uso e import de modulo de terceiros")
import requests

url = "https://www.example.com"
response = requests.get(url)
print(f"solicitação HTTP para {url} retornou o status {response.status_code}")