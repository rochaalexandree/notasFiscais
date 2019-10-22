import numpy as np 
import pandas as pd
import connectFDB

def get_cnpjList():
    lista = connectFDB.connect_FDB('estadual')
    cnpjList = []
    for y in lista:
        cnpjList.append(y[2])
        addList_UniCode_All(y[1])
        addList_filialCode_All(y[0])    

    return cnpjList

def get_cnpjListPlanilha(lista):
    
    cnpjList = []
    for y in lista:
        cnpjList.append(y[2])
        addList_UniCode_All(y[1])
        addList_filialCode_All(y[0])    

    return cnpjList

def get_senhaListPlanilha(lista):
    
    senhaList = []
    for y in lista:
        senhaList.append(y[3])    

    return senhaList

def get_inscricaoMunic():
    lista = connectFDB.connect_FDB('municipal')
    inscricaoMunic = []
    cnpjList = []
    for y in lista:
        inscricaoMunic.append(y[3])
        addList_UniCode_All(y[1])
        addList_filialCode_All(y[0])
        cnpjList.append(y[2])
    lista = [inscricaoMunic, cnpjList]

    return lista

def get_codigo():
    lista = connectFDB.connect_FDB('estadual') 
    codigoList = []
    for y in lista:
        codigoList.append(y[0])

    return codigoList

def addList_UniCode_All(codigo):
    try:
        arquivo = open('codigos.txt', 'r')
        conteudo = arquivo.readlines()

        conteudo.append(codigo + '\n')

        arquivo = open('codigos.txt', 'w')
        arquivo.writelines(conteudo)
        arquivo.close()
    except:
        conteudo = codigo + '\n'
        arquivo = open('codigos.txt', 'w')
        arquivo.writelines(conteudo)
        arquivo.close()
        
def addList_filialCode_All(codigo):
    try:
        arquivo = open('numFilial.txt', 'r')
        conteudo = arquivo.readlines()

        conteudo.append(codigo + '\n')

        arquivo = open('numFilial.txt', 'w')
        arquivo.writelines(conteudo)
        arquivo.close()
    except:
        conteudo = codigo + '\n'
        arquivo = open('numFilial.txt', 'w')
        arquivo.writelines(conteudo)
        arquivo.close()
            

def addList_UniCode(posicao):
    codigoList = get_codigo()
    if not(posicao == 'vazio'):    
        try:
            arquivo = open('codigos.txt', 'r')
            conteudo = arquivo.readlines()
            for cur in conteudo:
                if cur == (codigoList[posicao] + '\n'):
                    return

            conteudo.append(codigoList[posicao] + '\n')

            arquivo = open('codigos.txt', 'w')
            arquivo.writelines(conteudo)
            arquivo.close()
        except:
            conteudo = codigoList[posicao] + '\n'
            arquivo = open('codigos.txt', 'w')
            arquivo.writelines(conteudo)
            arquivo.close()
    elif posicao == 'vazio':
        arquivo = open('codigos.txt', 'r')
        conteudo = arquivo.readlines()

        conteudo.append(posicao + '\n')

        arquivo = open('codigos.txt', 'w')
        arquivo.writelines(conteudo)
        arquivo.close()
def addList_UniCodePftr(codigo):
    try:
        arquivo = open('codigosPftr.txt', 'r')
        conteudo = arquivo.readlines()

        conteudo.append(codigo + '\n')

        arquivo = open('codigosPftr.txt', 'w')
        arquivo.writelines(conteudo)
        arquivo.close()
    except:
        conteudo = codigo + '\n'
        arquivo = open('codigosPftr.txt', 'w')
        arquivo.writelines(conteudo)
        arquivo.close()


## caminhos para importar ##
def criarlistaImportar(cnpj):
    try:
        arquivo = open('caminhosParaImportar.txt', 'r')
        conteudo = arquivo.readlines()

        conteudo.append(cnpj + '\n')

        arquivo = open('caminhosParaImportar.txt', 'w')
        arquivo.writelines(conteudo)
        arquivo.close()
    except:
        conteudo = cnpj
        arquivo = open('caminhosParaImportar.txt', 'w')
        arquivo.writelines(conteudo)
        arquivo.close()

def codigosImportar():
    try:
        arquivo = open('codigos.txt', 'r')
        conteudo = arquivo.readlines()
        lista = []
        for i in conteudo:
            lista.append(i.replace('\n', ''))
        arquivo.close()
        return lista
    except:
        print("Nao ha nenhum codigo para importar")
        return None

def codigosFiliais():
    try:
        arquivo = open('numFilial.txt', 'r')
        conteudo = arquivo.readlines()
        lista = []
        for i in conteudo:
            lista.append(i.replace('\n', ''))
        arquivo.close()
        
        return lista
    except:
        print("Nao ha nenhum codigo de filial para importar")
        return None


def codigosImportarPftr():
    try:
        arquivo = open('codigosPftr.txt', 'r')
        conteudo = arquivo.readlines()
        lista = []
        for i in conteudo:
            lista.append(i.replace('\n', ''))
        arquivo.close()
        
        return lista
    except:
        print("Nao ha nenhum codigo para importar")
        return None