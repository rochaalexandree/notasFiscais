import fdb
import pandas as pd

def connect_FDB(tipo):
    
    parametros = estadualOuMunicipal(tipo)
    
    try:
        con = fdb.connect(host=parametros[0], database='/nQuestor/base/QUESTOR.FDB', user='SYSDBA', password='masterkey')
    except:
        #con = fdb.connect(dsn=host + '/nQuestor/base/QUESTOR.FDB', user='SYSDBA', password='masterkey')
        con = fdb.connect(dsn='D:/nQuestor/base/QUESTOR_EMPRESA_1117.FDB', user='SYSDBA', password='masterkey')
    cur = con.cursor()
    cur.execute(parametros[1])

    
    lista = []
    lista1 = []
    fieldIndices = range(len(cur.description))
    x = 0
    for row in cur:
        for fieldIndex in fieldIndices:
            fieldValue = str(row[fieldIndex])
            fieldMaxWidth = cur.description[fieldIndex][fdb.DESCRIPTION_DISPLAY_SIZE]  
            lista.append(fieldValue.ljust(fieldMaxWidth))
            x = x + 1    
        lista1.append([lista[x - 4],lista[x - 3], lista[x - 2], lista[x - 1]])
    
    return lista1

def estadualOuMunicipal(tipo):
    arq = open('base.txt', 'r')
    texto = arq.readlines()    
    arq.close()
    host = texto[0].replace('\n', '')
    if tipo == 'estadual':
        arq = open('sql.txt', 'r')
        texto = arq.readlines()    
        arq.close()
        sql = texto[0].replace('\n', '')
    else:
        arq = open('sql.txt', 'r')
        texto = arq.readlines()    
        arq.close()
        sql = texto[1].replace('\n', '')
    
    return [host, sql]

def connect_relatorio(dataInicial, dataFinal):
    parametros = estadualOuMunicipal('estadual')
    try:
        con = fdb.connect(host=parametros[0], database='/nQuestor/base/QUESTOR.FDB', user='SYSDBA', password='masterkey')
    except:
        #con = fdb.connect(dsn=host + '/nQuestor/base/QUESTOR.FDB', user='SYSDBA', password='masterkey')
        con = fdb.connect(dsn='D:/nQuestor/base/QUESTOR_EMPRESA_1117.FDB', user='SYSDBA', password='masterkey')
        cur = con.cursor()
        cur.execute('SELECT l.CODIGOEMPRESA, l.DATAHORALCTOFIS, e.NOMEESTAB, l.ESPECIENF FROM lctofissai l JOIN estab e on l.CODIGOEMPRESA = e.CODIGOEMPRESA WHERE l.datalctofis BETWEEN ' + "'" + str(dataInicial) + "'" + 'AND' + "'" + str(dataFinal) + "'" + 'ORDER BY l.CODIGOEMPRESA')

    lista = []
    lista1 = []
    fieldIndices = range(len(cur.description))
    x = 0
    for row in cur:
        for fieldIndex in fieldIndices:
            fieldValue = str(row[fieldIndex])
            fieldMaxWidth = cur.description[fieldIndex][fdb.DESCRIPTION_DISPLAY_SIZE]  
            lista.append(fieldValue.ljust(fieldMaxWidth))
            x = x + 1    
        lista1.append([lista[x - 4],lista[x - 3], lista[x - 2], lista[x - 1]])
   
    return lista1