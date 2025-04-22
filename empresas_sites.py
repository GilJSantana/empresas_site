"""
Baseado em um arquivo CSV com uma lista de empresas,
é retornado o site dessas empresas na internet.
Parmetros:
"""

from data_frame_empresas_site import cria_dataframe, \
    adiciona_sites_ao_dataframe

caminho_arquivo = 'dados/empresas_site.csv'

df = cria_dataframe(caminho_arquivo)
empresa_site = adiciona_sites_ao_dataframe(df, 'Empresa')

print(empresa_site)
