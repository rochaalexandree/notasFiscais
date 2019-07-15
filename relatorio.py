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