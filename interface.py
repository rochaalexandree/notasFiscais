from multiprocessing import Pool, freeze_support

from selenium import webdriver

import caminhos
import chromeOp
import crawlerPftr
import crawlerSER
import questorFiscal
import tratarDados


def rodaProcesso(processo):    
    texto = caminhos.getCaminhos()
    
    if(processo == 'crawlerSER'):
        cnpj = tratarDados.get_cnpjList()
        browserUm = chromeOp.optionsDown(texto[0].replace('\n', ''))
        crawlerSER.servirtual(browserUm, cnpj)
    else:
        browserDois = chromeOp.optionsDown(texto[1].replace('\n', ''))
        crawlerPftr.prefeitura(browserDois)

if __name__ == "__main__":
    #processos = ('crawlerSER','crawlerPftr')
    #pool = Pool(processes=2)
    #pool.map(rodaProcesso, processos)
    rodaProcesso('crawlerSER')
    caminho = caminhos.getCaminhos()
    codigos = tratarDados.codigosImportar()
    questorFiscal.importar('estadual', codigos, caminho)
    #questorFiscal.importar('Municipal', '1117', caminho)
