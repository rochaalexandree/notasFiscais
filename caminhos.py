## Passe como argumento a linha do caminho do arquivo ##

def getCaminho(posicaoCaminho):
    arq = open('caminhos.txt', 'r')
    texto = arq.readlines()    
    arq.close()
    tx = texto[posicaoCaminho].replace('\n', '')
    return tx

def getCaminhos():
    arq = open('caminhos.txt', 'r')
    texto = arq.readlines()    
    arq.close()
    caminhos = []
    for cur in texto:
        caminhos.append(cur.replace('\n', ''))
    return caminhos

def getCaminhosNFe():
    arq = open('caminhosNFe.txt', 'r')
    texto = arq.readlines()    
    arq.close()
    caminhos = []
    for cur in texto:
        caminhos.append(cur.replace('\n', ''))
    return caminhos

def getCaminhosNFC():
    arq = open('caminhosNFC.txt', 'r')
    texto = arq.readlines()    
    arq.close()
    caminhos = []
    for cur in texto:
        caminhos.append(cur.replace('\n', ''))
    return caminhos

def getCaminhosPftrTomado():
    arq = open('caminhosPftrTomado.txt', 'r')
    texto = arq.readlines()    
    arq.close()
    caminhos = []
    for cur in texto:
        caminhos.append(cur.replace('\n', ''))
    return caminhos

def getCaminhosPftrPrestado():
    arq = open('caminhosPftrPrestado.txt', 'r')
    texto = arq.readlines()    
    arq.close()
    caminhos = []
    for cur in texto:
        caminhos.append(cur.replace('\n', ''))
    return caminhos

def addCaminhoPftrTomado(caminho):
    try:
        palavras = caminho.split("/")
        novoCaminho = ""
        for i in palavras:
            novoCaminho = novoCaminho + i + "\\"
        novoCaminho = novoCaminho[:-1]
        novoCaminho = novoCaminho +'\n'
        arquivo = open('caminhosPftrTomado.txt', 'r')
        conteudo = arquivo.readlines()

        print (novoCaminho)
        conteudo.append(novoCaminho)

        arquivo = open('caminhosPftrTomado.txt', 'w')
        arquivo.writelines(conteudo)
        arquivo.close()
    except:
        arquivo = open('caminhosPftrTomado.txt', 'r')
        conteudo = arquivo.readlines()

        conteudo.append(caminho + '\n')

        arquivo = open('caminhosPftrTomado.txt', 'w')
        arquivo.writelines(conteudo)
        arquivo.close()

def addCaminhoPftrPrestado(caminho):
    try:
        palavras = caminho.split("/")
        novoCaminho = ""
        for i in palavras:
            novoCaminho = novoCaminho + i + "\\"
        novoCaminho = novoCaminho[:-1]
        novoCaminho = novoCaminho +'\n'
        arquivo = open('caminhosPftrPrestado.txt', 'r')
        conteudo = arquivo.readlines()

        print (novoCaminho)
        conteudo.append(novoCaminho)

        arquivo = open('caminhosPftrPrestado.txt', 'w')
        arquivo.writelines(conteudo)
        arquivo.close()
    except:
        arquivo = open('caminhosPftrPrestado.txt', 'r')
        conteudo = arquivo.readlines()

        conteudo.append(caminho + '\n')

        arquivo = open('caminhosPftrPrestado.txt', 'w')
        arquivo.writelines(conteudo)
        arquivo.close()

def addCaminhoNFe(caminho):
    try:
        palavras = caminho.split("/")
        novoCaminho = ""
        for i in palavras:
            novoCaminho = novoCaminho + i + "\\"
        novoCaminho = novoCaminho[:-1]
        novoCaminho = novoCaminho +'\n'
        arquivo = open('caminhosNFe.txt', 'r')
        conteudo = arquivo.readlines()

        print (novoCaminho)
        conteudo.append(novoCaminho)

        arquivo = open('caminhosNFe.txt', 'w')
        arquivo.writelines(conteudo)
        arquivo.close()
    except:
        palavras = caminho.split("/")
        novoCaminho = ""
        for i in palavras:
            novoCaminho = novoCaminho + i + "\\"
        novoCaminho = novoCaminho[:-1]
        novoCaminho = novoCaminho +'\n'

        arquivo = open('caminhosNFe.txt', 'r')
        conteudo = arquivo.readlines()

        conteudo.append(caminho + '\n')

        arquivo = open('caminhosNFe.txt', 'w')
        arquivo.writelines(conteudo)
        arquivo.close()

def addCaminhoNFC(caminho):
    try:
        palavras = caminho.split("/")
        novoCaminho = ""
        for i in palavras:
            novoCaminho = novoCaminho + i + "\\"
        novoCaminho = novoCaminho[:-1]
        novoCaminho = novoCaminho +'\n'
        arquivo = open('caminhosNFC.txt', 'r')
        conteudo = arquivo.readlines()

        print (novoCaminho)
        conteudo.append(novoCaminho)

        arquivo = open('caminhosNFC.txt', 'w')
        arquivo.writelines(conteudo)
        arquivo.close()
    except:
        arquivo = open('caminhosNFC.txt', 'r')
        conteudo = arquivo.readlines()

        conteudo.append(caminho + '\n')

        arquivo = open('caminhosNFC.txt', 'w')
        arquivo.writelines(conteudo)
        arquivo.close()

def limparArquivos():
    arquivo = open('relatorioSER.txt', 'w')
    arquivo.close()
    arquivo = open('caminhosNFC.txt', 'w')
    arquivo.close()
    arquivo = open('caminhosNFe.txt', 'w')
    arquivo.close()
    arquivo = open('codigos.txt', 'w')
    arquivo.close()
    arquivo = open('numFilial.txt', 'w')
    arquivo.close()

def limparArquivosPftr():
    arquivo = open('relatorioPftr.txt', 'w')
    arquivo.close()
    arquivo = open('caminhosPftrTomado.txt', 'w')
    arquivo.close()
    arquivo = open('caminhosPftrPrestado.txt', 'w')
    arquivo.close()
    arquivo = open('codigos.txt', 'w')
    arquivo.close()
    arquivo = open('numFilial.txt', 'w')
    arquivo.close()

def pontoDePartida():
    arq = open('pontoDePartida.txt', 'r')
    texto = arq.readlines()    
    arq.close()
    try:
        return texto[0].replace('\n', '')
    except:
        return texto[0]

def usuarioSenha():
    arq = open('Acesso.txt', 'r')
    texto = arq.readlines()
    arq.close()
    acesso = []
    cont = 0
    
    for atual in texto:
        acesso.append(atual.replace('\n', ''))
        cont = cont + 1
    
    return acesso