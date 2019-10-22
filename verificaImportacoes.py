def confirmaImportacao(mensagemConfirmacao):
    arq = open("importacoesConfirmadas.txt", 'r')
    conteudo = arq.readlines()
    arq.close()
    
    conteudo.append(mensagemConfirmacao + '\n')
    
    arq = open("importacoesConfirmadas.txt", 'w')
    arq.writelines(conteudo)
    arq.close()

def verificaImportacao(codigos):
    try:
        codigosUpdate = codigos
        arq = open("importacoesConfirmadas.txt", 'r')
        conteudo = arq.readlines()
        arq.close()

        lista = []
        for cur in conteudo:
            number = cur.split(' ')
            number[0].replace('\n')
            lista.append(number[0])
        
        cont = 0
        
        for run in codigos:
            for cur in lista: 
                if(run == cur):
                    codigosUpdate.pop(cont)
                    break
            cont = cont + 1
    except:
        pass
    return codigosUpdate