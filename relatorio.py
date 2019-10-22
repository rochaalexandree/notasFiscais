import connectFDB
import getData
import time

def relatorioPftr(mensagem):
    try:
        arquivo = open('relatorioPftr.txt', 'r')
        conteudo = arquivo.readlines()

        conteudo.append(mensagem)

        arquivo = open('relatorioPftr.txt', 'w')
        arquivo.writelines(conteudo)
        arquivo.close()
    except:
        conteudo = mensagem
        arquivo = open('relatorioPftr.txt', 'w')
        arquivo.writelines(conteudo)
        arquivo.close()

def relatorioSER(mensagem):
    try:
        arquivo = open('relatorioSER.txt', 'r')
        conteudo = arquivo.readlines()

        conteudo.append(mensagem)

        arquivo = open('relatorioSER.txt', 'w')
        arquivo.writelines(conteudo)
        arquivo.close()
    except:
        conteudo = mensagem
        arquivo = open('relatorioSER.txt', 'w')
        arquivo.writelines(conteudo)
        arquivo.close()

def gerarRelatorioAtual():
    dataInicial = getData.get_dataInicial(4)
    dataFinal = getData.get_dataFinal(3)
    print(str(dataInicial) + '\t' + str(dataFinal))
    # time.sleep(60)
    lista = connectFDB.connect_relatorio(dataInicial, dataFinal)
    codigosEmpresa = []
    nomeRelatorio = str(dataInicial) + ":a:" + str(dataFinal)
    try:
        for sql in lista:
            if sql[0] in codigosEmpresa:
                pass
            else:
                codigoEmpresa.append(sql[0])
                adicionaAoRelatorio(nomeRelatorio, 'Nome: ' + sql[2] + '\t' + 'Data/Hora Importação: ' + sql[1] + 'Tipo da Nota: ' + sql[3] + '\n') 
    except:
        print('Sem importações')
    
    print(lista)

def adicionaAoRelatorio(nomeRelatorio, mensagem):
    try:
        arquivo = open('relatorios/Importados-'+ nomeRelatorio + '.txt', 'r')
        conteudo = arquivo.readlines()

        conteudo.append(mensagem)

        arquivo = open('relatorios/Importados-' + nomeRelatorio + '.txt', 'w')
        arquivo.writelines(conteudo)
        arquivo.close()
    except:
        conteudo = mensagem
        arquivo = open('relatorios/Importados-' + nomeRelatorio + '.txt', 'w')
        arquivo.writelines(conteudo)
        arquivo.close()