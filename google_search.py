"""
Buscar site de uma empresa a partir do nome da empresa.

:param
nome_empresa: Nome da empresa a ser buscada.
returns
resultado: URL do site encontrado ou mensagem de erro.
"""

from googlesearch import search


def buscar_site(nome_empresa):
    try:
        resultados = search(nome_empresa)
        for resultado in resultados:
            return resultado
    except Exception as error:
        return f'Erro ao buscar o site {nome_empresa} : {error}'
