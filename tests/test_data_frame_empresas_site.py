import pandas as pd
import pytest

from data_frame_empresas_site import cria_dataframe, adiciona_sites_ao_dataframe

def mock_buscar_site(nome_empresa):
    # Função mockada para simular o comportamento de buscar_site
    return f'http://www.{nome_empresa.lower()}.com'

def test_cria_dataframe_sucesso():
    # Testa a criação do DataFrameP a partir de um arquivo CSV
    arquivo_csv = '../dados/teste.csv'
    df = cria_dataframe(arquivo_csv)
    assert isinstance(df, pd.DataFrame)
    assert len(df) == 2
    assert 'Empresa' in df.columns

def test_cria_dataframe_arquivo_nao_existe():
    with pytest.raises(FileNotFoundError):
        cria_dataframe('arquivo_inexistente.csv')

def test_adiciona_sites_ao_dataframe(mocker):
    mocker.patch('data_frame_empresas_site.buscar_site', mock_buscar_site)
    data = '../dados/teste.csv'
    df = pd.read_csv(data)

    df_com_sites = adiciona_sites_ao_dataframe(df, 'Empresa')
    assert 'Site' in df_com_sites.columns
    assert not df_com_sites['Site'].empty

def test_adiciona_sites_ao_dataframe_vazio():
    df = pd.DataFrame()
    df_com_sites = adiciona_sites_ao_dataframe(df, 'Empresa')
    assert 'Site' in df_com_sites.columns
    assert len(df_com_sites) == 0

def test_adiciona_sites_ao_dataframe_coluna_nao_existe():
    data = '../dados/teste.csv'
    df = pd.read_csv(data)
    with pytest.raises(KeyError):
        adiciona_sites_ao_dataframe(df, 'Setor')