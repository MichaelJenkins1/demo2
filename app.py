import pandas as pd
import requests

print("HIHSDOPOSDHFLJKSDHFLKJSFHLKSDFH*************************")
url = 'http://localhost:3005/v1/api/ludisurl/00d1a00'
headers = {'x-api-key': 'equ6MU4l4AGiOoB'}

response = requests.get(url, headers=headers)
if response.status_code == 200:
    data = pd.read_csv(response.content)
    # Use the 'data' DataFrame for further processing
    print(data.head())
else:
    print('Failed to retrieve data. Status code:', response.status_code)

if __name__ == '__main__':
    app.run_server(host='0.0.0.0', debug=True, port=8050)