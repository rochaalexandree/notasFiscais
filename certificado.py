import pyautogui
import time
import tratarDados

def enterCertificado():
    x = 0
    y = 100
    codigos = None
    

    
    while (x < y):
        try:
            time.sleep(5)
            s = pyautogui.locateCenterOnScreen('ok.png')
            pyautogui.click(s[0], s[1])
            pyautogui.move(100, 100)
            x = x + 1
            codigos = tratarDados.codigosImportar()
            if len(codigos) % 10 == 0:
                y = int(len(codigos) / 10) * 2
            elif len(codigos) > 10:
                y = int(int(len(codigos) + 10) / 10) * 2
            elif(len(codigos) < 10):        
                y = int(((len(codigos) / 10) + 10) / 10) * 2
        except:
            pass
            

if __name__ == "__main__":
    enterCertificado()