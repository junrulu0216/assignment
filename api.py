import requests
data = {
    "Nanme": '1111',
    "Client Id": "f67fc450722190595f12",
    "Client Secret": "dddd29d3a9b5b709dd8a9b7d8ae70bd5"
}
def get_artsy_data(endpoint):
    auth_response = requests.post(
        "https://api.artsy.net/api/tokens/xapp_token",
        json={"client_id": data['Client Id'], "client_secret": data["Client Secret"]}
    )
    if auth_response.status_code != 201:
        raise Exception(f"fail: {auth_response.text}")
    
    token = auth_response.json()["token"]
    

    response = requests.get(
        f"https://api.artsy.net/api/{endpoint}",
        headers={"X-Xapp-Token": token}
    )
    return response.json() if response.status_code == 200 else None


if __name__ =='__main__':
    print(get_artsy_data("search?q=Andy"))
