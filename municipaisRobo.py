from selenium import webdriver

import caminhos
import chromeOp
import crawlerPftr
import crawlerSER
import questorFiscalPftr
import tratarDados
import time
import lePlanilha


def formataCNPJ(lista):
    caracteresEspeciais = './-'
    cnpjList = []
    cnpj = ''
    for l in lista:
        for i in range(0, len(caracteresEspeciais)):
            l = l.replace(caracteresEspeciais[i], '')
        cnpjList.append(l)

    return cnpjList

def rodaProcesso(processo, posicaoAtual, lista, senha):    
    texto = caminhos.getCaminhos()
    cnpjFormatado = []
    if lista == []:
        matriz = lePlanilha.leMunicipais()
        lista = tratarDados.get_cnpjListPlanilha(matriz)
        senha = tratarDados.get_senhaListPlanilha(matriz)
        cnpjFormatado = formataCNPJ(lista)
    browserDois = chromeOp.optionsDown(texto[1].replace('\n', ''))
    crawlerPftr.prefeitura(browserDois, lista, posicaoAtual, senha, cnpjFormatado)
    
    return lista
    
if __name__ == "__main__":
    caminhos.limparArquivosPftr()
    posicaoAtual = int(caminhos.pontoDePartida()) # Essa função faz com que o robô inicie num ponto desejado da lista
    if(posicaoAtual > 0):
        caminhos.preencheCasasVaziasPftr(posicaoAtual)
    lista= []
    senha = []
    posicaoAtual = 0
    parada = 100
    while posicaoAtual < parada:
        lista = rodaProcesso('crawlerPftr', posicaoAtual, lista, senha)
        parada = len(lista)
        caminhoTomado = caminhos.getCaminhosPftrTomado()
        caminhoPrestado = caminhos.getCaminhosPftrPrestado()
        codigos = tratarDados.codigosImportar()
        filiais = tratarDados.codigosFiliais()
        questorFiscalPftr.importar('municipal', codigos, caminhoTomado, caminhoPrestado, filiais, posicaoAtual)
        posicaoAtual = parada
        
        if posicaoAtual > len(lista[0]):
            break
        time.sleep(5)   
