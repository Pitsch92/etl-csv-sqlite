import pandas as pd

def extract_csv(filepath: str):
    df = pd.read_csv(filepath, encoding='latin1',on_bad_lines="skip")
    # garantir que todas as colunas existam
    df = df.reindex(columns=["id","data","pais","estado","cidade","cliente_id","produto","categoria","quantidade","preco_unitario","desconto","valor_bruto","valor_liquido","pagamento"])
    return df

    