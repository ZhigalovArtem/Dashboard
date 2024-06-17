import pandas as pd
import json

file_path = 'merged_data.xlsx'
df = pd.read_excel(file_path)
with open('russia copy.geojson','r',encoding='UTF-8') as response:
        counties = json.loads(response.read())
