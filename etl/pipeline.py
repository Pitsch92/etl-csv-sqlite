from extract import extract_csv
from transform import transform_data

csv_path = 'etl-csv-sqlite/data/vendas.csv'
df = extract_csv(csv_path)
df = transform_data(df)
print(df)
