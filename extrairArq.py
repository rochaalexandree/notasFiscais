import os
import zipfile
import shutil
import time
import glob
import caminhos

def extrair(caminho, destino):
    while (True):
        try:
            try:
                removeAll(destino)
            except:
                pass
            original = os.getcwd()
            filename = max([caminho + "/" + f for f in os.listdir(caminho)], key=os.path.getctime)
            if (filename.find('.zip') == -1):
                filename = None
            arqZip = zipfile.ZipFile(filename)
            arqZip.extractall(destino)
            arqZip.close()
            os.chdir(caminho)
            time.sleep(4)
            files = glob.glob('*.zip')
            for file in files:
                os.remove(file)
            os.chdir(original)
            break
        except:
            try:
                shutil.rmtree(destino)
            except:
                print('Tentando extrair outra vez')
            time.sleep(3)
    removeAll(caminho)

def removeAll(path):
    dir = os.listdir(path)
    original = os.getcwd()
    os.chdir(path)
    for file in dir:
        try:
            os.remove(file)
        except:
            pass
    os.chdir(original)

def mover(caminho, destino, tipo):
    pare = 0
    while(True):
        try:
            try:
                removeAll(destino)
            except:
                pass
            time.sleep(4)
            filename = max([caminho + f for f in os.listdir(caminho)], key=os.path.getctime)
            
            if not(filename.find('.zip') == -1):
                filename = None

            if os.path.isdir(destino): # vemos se este diretorio ja existe
                pass
                #print('Ja existe uma pasta com esse nome!')    
            else:
                os.makedirs(destino) # aqui criamos a pasta caso nao exista
                #print ('Pasta criada com sucesso!')
            time.sleep(2)
            shutil.move(filename,destino)

            path = getArqUnico(destino)
            if tipo == "Tomado":  
                caminhos.addCaminhoPftrTomado(path)
            elif tipo == "Prestado":
                caminhos.addCaminhoPftrPrestado(path)
            time.sleep(3)
            break
        except:
            if pare == 50:
                break
            print('Tentando mover outra vez')
            time.sleep(2)
        time.sleep(1)
        removeAll(caminho)

def getArqUnico(caminho):
    try:
        filename = max([caminho + "/" + f for f in os.listdir(caminho)], key=os.path.getctime)
        print(filename)
        return filename
    except:
        print("Não foi possível localizar o arquivo")