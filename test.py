import pandas as pd

# Read the CSV file
airbnb_data = pd.read_csv("http://localhost:3005/v1/datasets/cloud/3sh2ps6v")

# View the first 5 rows
airbnb_data.head()