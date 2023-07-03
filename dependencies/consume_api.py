import requests


def get_api_data():
    url: str = f'https://api.publicapis.org/entries'
    response = requests.get(url)

    if response.status_code == 200:
        try:
            data: dict = dict(response.json())
            print(f'JSON pedido: {data["count"]}')
            return data
        except ValueError:
            print("A resposta não contém um JSON válido")
    else:
        print(f"A solicitação retornou um erro: {response.status_code}")
        print(response.text)


datas = get_api_data()
print(type(datas['entries'][0]['API']))

