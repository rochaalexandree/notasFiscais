import questorFiscalPftr
import caminhos
import tratarDados
import questorFiscal
#caminho = r'''C:\Users\rocha\Documents\ArquivosSER\10.974.579\0001-47'''
# caminhoTomado = caminhos.getCaminhosPftrTomado()
# caminhoPrestado = caminhos.getCaminhosPftrPrestado()
# codigos = tratarDados.codigosImportar()
# filiais = tratarDados.codigosFiliais()
# questorFiscalPftr.importar('municipal', codigos, caminhoTomado, caminhoPrestado, filiais, 0)

# import relatorio

# relatorio.gerarRelatorioAtual()

codigoEmpresa = ['1117', '1117']
caminhoNFe = ['D:\\', 'D:\\'] 
caminhoNFC = ['D:\\', 'D:\\']
filiais = ['1', '1'] 
caminhoNFeEntrada = ['D:\\', 'D:\\']
posicaoAtual = 0 
# questorFiscal.importar('estadual', codigoEmpresa, caminhoNFe, caminhoNFC, caminhoNFeEntrada, filiais, posicaoAtual, 2)
questorFiscalPftr.importar('municipal', codigoEmpresa, caminhoNFe, caminhoNFC, filiais, 0)