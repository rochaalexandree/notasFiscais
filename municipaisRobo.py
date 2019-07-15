from selenium import webdriver

import caminhos
import chromeOp
import crawlerPftr
import crawlerSER
import questorFiscalPftr
import tratarDados
import time


def rodaProcesso(processo, posicaoAtual, lista):    
    texto = caminhos.getCaminhos()
    
    if lista == []:
        lista = tratarDados.get_inscricaoMunic()

    browserDois = chromeOp.optionsDown(texto[1].replace('\n', ''))
    crawlerPftr.prefeitura(browserDois, lista[0], lista[1], posicaoAtual)
    
    return lista
    
if __name__ == "__main__":
    caminhos.limparArquivosPftr()
    lista= []
    posicaoAtual = 0
    parada = 10
    while posicaoAtual < parada:
        lista = rodaProcesso('crawlerPftr', posicaoAtual, lista)
        parada = len(lista[0])
        caminhoTomado = caminhos.getCaminhosPftrTomado()
        caminhoPrestado = caminhos.getCaminhosPftrPrestado()
        codigos = tratarDados.codigosImportar()
        filiais = tratarDados.codigosFiliais()
        questorFiscalPftr.importar('municipal', codigos, caminhoTomado, caminhoPrestado, filiais, posicaoAtual)
        posicaoAtual = posicaoAtual + 10
        
        if posicaoAtual > len(lista[0]):
            break
        time.sleep(5)   
