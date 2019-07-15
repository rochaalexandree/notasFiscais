import questorFiscalPftr
import caminhos
import tratarDados

#caminho = r'''C:\Users\rocha\Documents\ArquivosSER\10.974.579\0001-47'''
caminhoTomado = caminhos.getCaminhosPftrTomado()
caminhoPrestado = caminhos.getCaminhosPftrPrestado()
codigos = tratarDados.codigosImportar()
filiais = tratarDados.codigosFiliais()
questorFiscalPftr.importar('municipal', codigos, caminhoTomado, caminhoPrestado, filiais, 0)