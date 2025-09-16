import pandas as pd
import sqlite3
from pathlib import Path

def load_csv(df: pd.DataFrame, path: str):
    """
    Salva o DataFrame em CSV.
    :param df: DataFrame transformado
    :param path: caminho do arquivo CSV de saída
    """
    # Garante que o diretório existe
    Path(path).parent.mkdir(parents=True, exist_ok=True)
    
    # Salva CSV com UTF-8 para manter acentos
    df.to_csv(path, index=False, encoding="utf-8")
    print(f"CSV salvo em: {path}")

def load_sqlite(df: pd.DataFrame, db_path: str, table_name: str = "vendas"):
    """
    Salva o DataFrame em um banco SQLite.
    :param df: DataFrame transformado
    :param db_path: caminho do arquivo SQLite
    :param table_name: nome da tabela no SQLite
    """
    # Garante que o diretório existe
    Path(db_path).parent.mkdir(parents=True, exist_ok=True)
    
    # Forçar colunas como string (texto)
    colunas_texto = ["produto", "categoria", "pagamento", "cidade", "estado", "pais"]
    for col in colunas_texto:
        df[col] = df[col].astype(str)

    # Forçar colunas numéricas
    colunas_numericas = ["quantidade", "preco_unitario", "desconto", "valor_bruto", "valor_liquido"]
    for col in colunas_numericas:
        df[col] = pd.to_numeric(df[col], errors="coerce")
    
    
    # Conecta no banco (cria se não existir)
    conn = sqlite3.connect(db_path)
    
     # Salva a tabela, substituindo se já existir
    df.to_sql(table_name, conn, if_exists='replace', index=False, dtype={
    "produto": "TEXT",
    "categoria": "TEXT",
    "pagamento": "TEXT",
    "cidade": "TEXT",
    "estado": "TEXT",
    "pais": "TEXT",
    "quantidade": "REAL",
    "preco_unitario": "REAL",
    "desconto": "REAL",
    "valor_bruto": "REAL",
    "valor_liquido": "REAL"
    })

    conn.close()
    print(f"SQLite salvo em: {db_path}, tabela: {table_name}")