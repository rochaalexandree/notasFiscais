import calendar
from datetime import date

def get_dataInicial(tipo):
    data_atual = date.today()
    month = '{}'.format(data_atual.month)
    year = '{}'.format(data_atual.year)
    month = int(month)
    year = int(year)
    
    if month == 1:
        month = 12
    else:
        month = month - 1
    if(tipo == 1):
        if month >=10:
            data = "01" + str(month) + str(year)
        else:
            data = "010" + str(month) + str(year)
    elif(tipo == 2):
        if month >=10:
            data = "01/" + str(month) + "/" + str(year)
        else:
            data = "01/0" + str(month)+ "/" + str(year)
    elif(tipo == 3):
        if month >=10:
            data = str(month) + "-" + str(year)
        else:
            data = str(month) + "-" + str(year)
    return data

def get_dataFinal(tipo):
    data_atual = date.today()
    month = '{}'.format(data_atual.month)
    year = '{}'.format(data_atual.year)
    month = int(month)
    year = int(year)
    if month == 1:
        month = 12
    else:
        month = month - 1

    monthRange = calendar.monthrange(year,month)
    if(tipo == 1):
        if month >=10:
            data = str(monthRange[1]) + str(month) + str(year)
        else:
            data = str(monthRange[1]) + "0" + str(month) + str(year)
    elif tipo == 2:
        if month >=10:
            data = str(monthRange[1]) + "/" + str(month) + "/" + str(year)
        else:
            data = str(monthRange[1]) + "/0" + str(month) + "/" + str(year)
    
    return data