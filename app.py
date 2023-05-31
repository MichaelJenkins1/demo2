import pandas as pd
import requests

print("HIHSDOPOSDHFLJKSDHFLKJSFHLKSDFH*************************")
url = 'https://staging-backend.ludisanalytics.com/v1/api/ludisurl/9389395'
headers = {'x-api-key': 'vitz-EY7bLeGARQ'}

response = requests.get(url, headers=headers)
if response.status_code == 200:
    data = pd.read_csv(response.content)
    # Use the 'data' DataFrame for further processing
    print(data.head())
else:
    print('Failed to retrieve data. Status code:', response.status_code)

if __name__ == '__main__':
    app.run_server(host='0.0.0.0', debug=True, port=8050)