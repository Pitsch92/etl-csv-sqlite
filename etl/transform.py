import pandas as pd

def transform_data(df: pd.DataFrame) -> pd.DataFrame:
    # Padroniza as informações em forma de maiúsculas e remove espaços extras
    df['pais'] = df['pais'].str.upper().str.strip()
    df['cidade'] = df['cidade'].str.upper().str.strip()
    df['produto'] = df['produto'].str.upper().str.strip()
    df['categoria'] = df['categoria'].str.upper().str.strip()
    df['pagamento'] = df['pagamento'].str.upper().str.strip()
    df['estado'] = df['estado'].str.upper().str.strip()
    
    
    # Converte a coluna 'data' para o formato datetime
    df['data'] = pd.to_datetime(df['data'])
    
    # Substitui valores '--' por None
    df['pais'] = df['pais'].replace({'--': None})
    df['cidade'] = df['cidade'].replace({'--': None})
    df['produto'] = df['produto'].replace({'--': None})
    df['categoria'] = df['categoria'].replace({'--': None})
    df['pagamento'] = df['pagamento'].replace({'--': None})
    df['estado'] = df['estado'].replace({'--': None})
    
    # Calcula o valor bruto e o valor líquido
    df['valor_bruto'] = df['quantidade'] * df['preco_unitario']
    df['valor_liquido'] = df['valor_bruto'] - df['desconto']
    
    # Garantir que as id sejam do tipo int
    df['id'] = df['id'].astype(int)
    df['id_cliente'] = df['id_cliente'].astype(int)
    
    # Reordenar colunas para organização
    df = df[
        [
            'id', 'data', 'pais', 'estado', 'cidade', 'cliente_id',
            'produto', 'categoria', 'quantidade', 'preco_unitario',
            'desconto', 'valor_bruto', 'valor_liquido', 'pagamento'
        ]
    ]
    
    return df