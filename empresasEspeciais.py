def updateEspecial(cnpj):
    dataFinal = getData.get_dataFinal(1).split('/')
    tamanhoMes = dataFinal[0]
    dataInicial = getData.get_dataInicial(1).split('/')
    
    diaIni = dataInicial[0]
    mesIni = dataInicial[1]
    anoIni = dataInicial[2]
    diaFin = dataFinal[0] 
    mesFin = dataFinal[1]
    anoFin = dataFinal[2]

    

    if tamanhoMes == 31:
        return 