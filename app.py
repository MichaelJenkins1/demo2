import pandas as pd

# Read the CSV file
airbnb_data = pd.read_csv("http://localhost:3005/v1/api/ludisurl/9e3a5f8")

# View the first 5 rows
print(airbnb_data.head())

if __name__ == '__main__':
    app.run_server(host='0.0.0.0', debug=True, port=8050)