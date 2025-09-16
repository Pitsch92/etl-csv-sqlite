from extract import extract_csv
from transform import transform_data
from load import load_csv, load_sqlite


csv_path = 'etl-csv-sqlite/data/vendas_sujo_limpo.csv'
processed_path = 'etl-csv-sqlite/data/vendas_sujo_limpo.csv'
db_path = 'etl-csv-sqlite/data/vendas_sujo.db'

try:
    df = extract_csv(csv_path)
    print("Extração concluída. Linhas lidas:", len(df))
    df = transform_data(df)
    print("Transformação concluída.")
    load_csv(df, processed_path)
    load_sqlite(df, db_path)
    print("Pipeline executado com sucesso!")
except Exception as e:
    print("Erro no pipeline:", e)