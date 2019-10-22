import tratarDados
import crawlerSER
import chromeOp
import tratarDados
import caminhos
import questorFiscal
import time
import lePlanilha
from selenium import webdriver

def rodaProcesso(lista, tipoDeNota, posicaoAtual, stop):    
    texto = caminhos.getCaminhos()

    if lista == []:
        matriz = lePlanilha.leEstaduais() 
        lista = tratarDados.get_cnpjListPlanilha(matriz)

    browserUm = chromeOp.optionsDown(texto[0].replace('\n', ''))
    crawlerSER.servirtual(browserUm, lista, tipoDeNota, posicaoAtual, stop)
    return lista

if __name__ == "__main__":
    caminhos.limparArquivos()
    posicaoAtual = int(caminhos.pontoDePartida()) # Essa função faz com que o robô inicie num ponto desejado da lista
    if(posicaoAtual > 0):
        caminhos.preencheCasasVazias(posicaoAtual)
    
    lista = []
    
    
    posicaoAtual = 0
    stop = lePlanilha.getTamanhoEstaduais() 
    
    

    parada = 100

    while posicaoAtual < parada:
        lista = rodaProcesso(lista, 'NFe', posicaoAtual, stop)
        rodaProcesso(lista, 'NFC', posicaoAtual, stop)
        parada = len(lista)
        
        caminhoNFe = caminhos.getCaminhosNFe()
        caminhoNFC = caminhos.getCaminhosNFC()
        codigos = tratarDados.codigosImportar()
        filiais = tratarDados.codigosFiliais()
        caminhoNFeEntrada = caminhos.getCaminhosNFeEntrada()
        questorFiscal.importar('estadual', codigos, caminhoNFe, caminhoNFC, caminhoNFeEntrada, filiais, posicaoAtual, stop)
        
        posicaoAtual = stop
        stop = len(lista)
        
        if posicaoAtual == len(lista):
            break
        
        time.sleep(3)