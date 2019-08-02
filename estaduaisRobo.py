import tratarDados
import crawlerSER
import crawlerPftr
import chromeOp
import tratarDados
import caminhos
import questorFiscal
import time
from selenium import webdriver

def rodaProcesso(lista, tipoDeNota, posicaoAtual):    
    texto = caminhos.getCaminhos()
    
    if lista == []:
        lista = tratarDados.get_cnpjList()

    browserUm = chromeOp.optionsDown(texto[0].replace('\n', ''))
    crawlerSER.servirtual(browserUm, lista, tipoDeNota, posicaoAtual)
    return lista

if __name__ == "__main__":
    caminhos.limparArquivos()
    posicaoAtual = int(caminhos.pontoDePartida()) # Essa função faz com que o robô inicie num ponto desejado da lista
    lista = []
    #posicaoAtual = 0
    parada = posicaoAtual + 10
    while posicaoAtual < parada:
        lista = rodaProcesso(lista, 'NFe', posicaoAtual)
        rodaProcesso(lista, 'NFC', posicaoAtual)
        parada = len(lista)
        caminhoNFe = caminhos.getCaminhosNFe()
        caminhoNFC = caminhos.getCaminhosNFC()
        codigos = tratarDados.codigosImportar()
        filiais = tratarDados.codigosFiliais()
        #questorFiscal.importar('estadual', codigos, caminhoNFe, caminhoNFC, filiais, posicaoAtual)
        posicaoAtual = posicaoAtual + 10
        if posicaoAtual > len(lista):
            break
        time.sleep(3)