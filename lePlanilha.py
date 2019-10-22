import pandas as pd
import numpy as np
import tratarDados
import time

def leMunicipais():
    dfPrefeitura = pd.read_excel('planilha/logins.xlsx')
    dfPrefeitura = dfPrefeitura.rename(columns = {dfPrefeitura.columns[0] : 'Codigo', dfPrefeitura.columns[1] : 'Empresa', dfPrefeitura.columns[2] : 'CNPJ', dfPrefeitura.columns[3] : 'SenhaPrefeitura', dfPrefeitura.columns[4] : 'Estado', dfPrefeitura.columns[5] : 'SenhaEstado'})
    dfPrefeitura = dfPrefeitura.replace({'SenhaPrefeitura': {'-': np.nan}})
    dfPrefeitura = dfPrefeitura.dropna()
    dfPrefeitura = dfPrefeitura.drop('Estado', axis = 1)
    dfPrefeitura = dfPrefeitura.drop('SenhaEstado', axis = 1)
    # print(dfPrefeitura.shape)

    codigos = []
    filiais = []
    codigo = dfPrefeitura['Codigo'].values
    for i in codigo:
        atual = str(i).split('.')
        codigos.append(atual[0])
        filiais.append(atual[1])
    cnpj = dfPrefeitura['CNPJ'].values
    senha = dfPrefeitura['SenhaPrefeitura'].values
    # listaPrefeitura = np.array([dfPrefeitura['Codigo'].values, dfPrefeitura['CNPJ'].values, dfPrefeitura['SenhaPrefeitura'].values])
    lista = []
    cont = 0
    while cont < len(codigo):
        lista.append([filiais[cont], codigos[cont], cnpj[cont], senha[cont]])
        cont = cont + 1

    return lista
    
def leEstaduais():
    dfEstado = pd.read_excel('planilha/logins.xlsx')
    dfEstado = dfEstado.rename(columns = {dfEstado.columns[0] : 'Codigo', dfEstado.columns[1] : 'Empresa', dfEstado.columns[2] : 'CNPJ', dfEstado.columns[3] : 'SenhaPrefeitura', dfEstado.columns[4] : 'Estado', dfEstado.columns[5] : 'SenhaEstado'})
    dfEstado = dfEstado.replace({'SenhaEstado': {'-': np.nan}})
    dfEstado = dfEstado.dropna()
    dfEstado = dfEstado.drop('SenhaPrefeitura', axis = 1)
    dfEstado = dfEstado.sort_values(['Estado'])
    # print(dfEstado)

    codigos = []
    filiais = []
    codigo = dfEstado['Codigo'].values
    for i in codigo:
        atual = str(i).split('.')
        codigos.append(atual[0])
        filiais.append(atual[1])

    cnpj = dfEstado['CNPJ'].values
    estado = dfEstado['Estado'].values
    senha = dfEstado['SenhaEstado'].values
    # listaPrefeitura = np.array([dfPrefeitura['Codigo'].values, dfPrefeitura['CNPJ'].values, dfPrefeitura['SenhaPrefeitura'].values])
    lista = []
    cont = 0
    while cont < len(codigo):
        lista.append([filiais[cont], codigos[cont], cnpj[cont], estado[cont], senha[cont]])  
        cont = cont + 1


    # tratarDados.get_cnpjListPlanilha(lista)

    return lista

def getTamanhoEstaduais():
    matriz = leEstaduais()

    cont = 0
    while cont < len(matriz):
        if cont > 0 and (matriz[cont][4] != matriz[cont - 1][4]):
            stop = cont
            break
        
        cont = cont + 1

    return stop