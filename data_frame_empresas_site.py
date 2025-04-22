"""
Adiciona uma coluna de sites ao DataFrame a partir de uma coluna de nomes de empresas.

:param df: DataFrame contendo os dados das empresas.
:param coluna_nome: Nome da coluna que contém os nomes das empresas.
:return: DataFrame atualizado com a nova coluna de sites.
"""

import pandas as pd

from google_search import buscar_site


def cria_dataframe(arquivo_csv):
    df = pd.read_csv(arquivo_csv, encoding='utf-8')
    return df


def adiciona_sites_ao_dataframe(df, coluna_nome):
    if df.empty:
        return pd.DataFrame(columns=['Site'])
    df['Site'] = df[coluna_nome].apply(buscar_site)
    return df
