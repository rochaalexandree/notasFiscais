from pywinauto.application import Application
import pyautogui
import time
import getData
import extrairArq
import tratarDados
import relatorio
from pywinauto import keyboard

def importar(tipo, codigoEmpresa, caminhoTomado, caminhoPrestado, filiais, posicaoAtual):
    
    app = Application().start(cmd_line=u'D:/nQuestor/nfis.exe')
    
    tnfrmloginquestor = app.TnFrmLoginQuestor
            
    ## verifica se a página já está visível ##
    while(True):
        try:
            tnfrmloginquestor[u'4'].wait("visible")
            tnfrmloginquestor[u'3'].type_keys('administrador')
            tnfrmloginquestor[u'4'].type_keys('masterkey')
            break
        except:
            time.sleep(2)

    ## faz o login ##
    time.sleep(2)
    tnfrmloginquestor.TnButton2.click()

    municipal(caminhoTomado, caminhoPrestado, app, codigoEmpresa, filiais, posicaoAtual)

    app.kill()

def escolherEmpresa(app, codigoEmpresa, filial):
    ## combo box inicial de seleção ##

    #adicionar aqui o clique para troca de empresa
    try:
        app.TnFisSMenu.nToolBarPrinc.type_keys('{F7}')
    except:
        pass
    while(True):
        try:
            app[u'Sele\xe7\xe3o'].wait('visible')
            tnfrmdlgscrollbox = app[u'Sele\xe7\xe3o']
            break
        except:
            print('Não encontrou a caixa de seleção de empresa')

    while(True):
        try:
            tnfrmdlgscrollbox.wait("visible")
            time.sleep(3)
            break
        except:
            time.sleep(2)
    try:
        tnfrmdlgscrollbox[u'11'].type_keys(codigoEmpresa)
        time.sleep(2)
    except:
        print('Nao ha mais codigos para importar')
        app.kill()
    
    #Mensagem de erro por causa do tempo de busca no banco de dados
    try:
        app.TnMessageForm.OK.click()
        time.sleep(3)
        app.TnMessageForm.OK.click()
    except:
        pass

    try:
        tnfrmdlgscrollbox[u'8'].type_keys(filial)
        time.sleep(2)
    except:
        print('Sem numero de filial')
    
    try:
        app.TnMessageForm.OK.click()
        time.sleep(3)
        app.TnMessageForm.OK.click()
    except:
        pass

    tnfrmdlgscrollbox.TnMaskEdit4.type_keys(getData.get_dataInicial(1))
    time.sleep(2)
    tnfrmdlgscrollbox.TnMaskEdit2.type_keys(getData.get_dataFinal(1))
    time.sleep(3)
    tnfrmdlgscrollbox.OK.click()
    time.sleep(5)
    try:
        tnfrmdlgscrollbox.OK.click()
    except:
        pass

    try:
        app.TnMessageForm[u'&N\xe3o'].click()
        time.sleep(3)
        app.TnMessageForm.OK.click()
        time.sleep(3)
        app.TnMessageForm.OK.click()
        time.sleep(3)
    except:
        try:
            app.TnMessageForm.NO.click()
            time.sleep(3)
            app.TnMessageForm.OK.click()
            time.sleep(3)
            app.TnMessageForm.OK.click()
            time.sleep(3)        
        except:
            pass

def municipal(caminhoTomado, caminhoPrestado, app, codigoEmpresa, filiais, posicaoAtual):
    posiCami = posicaoAtual
    while(True):
        try:
            if caminhoPrestado[posiCami] != "vazio" or caminhoTomado[posiCami] != "vazio":
                try:
                    escolherEmpresa(app, codigoEmpresa[posiCami], filiais[posiCami])
                except:
                    break
            
                while(True):
                    try:
                        app.TnFisSMenu.wait("visible")
                        break
                    except:
                        pass
                try:
                    if caminhoPrestado[posiCami] != "vazio":
                        municipalPrestado(caminhoPrestado[posiCami], app)
                    elif caminhoTomado[posiCami] != "vazio":
                        municipalTomado(caminhoTomado[posiCami], app)
                except:
                    break

            posiCami = posiCami + 1
        except:
            break
    
    
def municipalPrestado(caminhoPrestado, app):
    tnfissmenu = app.TnFisSMenu
    tnfissmenu.menu_item(u'Ar&quivos->#3->#4').click()
    
    try:
        while(True):
            try:
                tnfissmenu[u'73'].wait("visible")
                try:
                    tnfissmenu[u'72'].type_keys(getData.get_dataFinal(1)) #data final
                except:
                    try:
                        tnfissmenu[u'71'].type_keys(getData.get_dataFinal(1)) #data final
                    except:
                        tnfissmenu[u'74'].type_keys(getData.get_dataFinal(1)) #data final
                break
            except:
                pass
        ## Seta todos os combobox ##
        tnfissmenu.TnComboBox18.select("Emitidas (Saídas)") # Movimento
        tnfissmenu.TnComboBox16.select("Tributado") #Integrar    
        tnfissmenu.TnComboBox14.select("Sim") #importar Produto 
        tnfissmenu.TnComboBox12.select("Não") # Importar Pis/cofins/Outros
        tnfissmenu.TnComboBox10.select("Sim") #Impotar produto padrão
        tnfissmenu.TnComboBox8.select("Não Permitir Erros") #Tratamento de Erro
        tnfissmenu.TnComboBox6.select("Importar Somente NFe não Importadas") #Tipo de Processamento
        tnfissmenu.TnComboBox4.select("Não") #validar emitente   
        tnfissmenu.TnComboBox2.select("Um Único Arquivo") #Tipo do Local
        
        ## Seta todas as caixas de texto ##
        
        tnfissmenu.TnMaskEdit36.type_keys("0")#Produto Padrão
        try:
            app.TnMessageForm.OK.click()
            time.sleep(3)
            app.TnMessageForm.OK.click()
        except:
            pass    
        
        tnfissmenu.TnMaskEdit28.type_keys("5933002")# Natureza
        tnfissmenu.TnMaskEdit25.type_keys("5933002")# Natureza Retidos

        ## IRRF ##
        tnfissmenu.TnMaskEdit22.type_keys("1708")
        tnfissmenu.TnMaskEdit21.type_keys("1")

        ## PIS ##
        tnfissmenu.TnMaskEdit18.type_keys("5952")
        tnfissmenu.TnMaskEdit17.type_keys("2")

        ## COFINS ##
        tnfissmenu.TnMaskEdit14.type_keys("5952")
        tnfissmenu.TnMaskEdit13.type_keys("2")

        ## CSLL ##
        tnfissmenu.TnMaskEdit10.type_keys("5952")
        tnfissmenu.TnMaskEdit9.type_keys("2")
        
        tnfissmenu.TnMaskEdit6.type_keys(caminhoPrestado) # caminho 
        tnfissmenu.Static.click()
        # tnfissmenu.nToolBar.type_keys('{F9}')
            #time.sleep(10)
        while(True):
            try:
                tnfissmenu.Static2.wait('visible')
                tnfissmenu.Static.wait('visible')
                time.sleep(3)
                tnfissmenu.Static.click()
                print('NFC-e Importado')
                conteudo = "NFe Saídas foi Importado\n"
                relatorio.relatorioPftr(conteudo)
                break
            except:
                time.sleep(2)

    except:
        print("Nao foi possivel concluir a importacao")

def municipalTomado(caminhoTomado, app):
    tnfissmenu = app.TnFisSMenu
    # tnfissmenu.menu_item(u'Ar&quivos->#3->#4').click()
    
    try:
        while(True):
            try:
                tnfissmenu[u'73'].wait("visible")
                tnfissmenu[u'73'].type_keys(getData.get_dataFinal(1)) #data final
                break
            except:
                pass
        
        ## Seta todos os combobox ##
        tnfissmenu.TnComboBox18.select("Recebidas (Entradas)") # Movimento
        tnfissmenu.TnComboBox16.select("Outras") #Integrar    
        tnfissmenu.TnComboBox14.select("Não") #importar Produto 
        tnfissmenu.TnComboBox8.select("Permitir Erros") #Tratamento de Erro
        tnfissmenu.TnComboBox6.select("Importar Somente NFe não Importadas") #Tipo de Processamento
        tnfissmenu.TnComboBox4.select("Não") #validar emitente   
        tnfissmenu.TnComboBox2.select("Um Único Arquivo") #Tipo do Local
        
        ## Seta todas as caixas de texto ##
        
        tnfissmenu.TnMaskEdit28.type_keys("8000012")# Natureza
        tnfissmenu.TnMaskEdit25.type_keys("8000002")# Natureza Retidos

        ## IRRF ##
        tnfissmenu.TnMaskEdit22.type_keys("1708")
        tnfissmenu.TnMaskEdit21.type_keys("6")

        ## PIS ##
        tnfissmenu.TnMaskEdit18.type_keys("5952")
        tnfissmenu.TnMaskEdit17.type_keys("7")

        ## COFINS ##
        tnfissmenu.TnMaskEdit14.type_keys("5952")
        tnfissmenu.TnMaskEdit13.type_keys("7")

        ## CSLL ##
        tnfissmenu.TnMaskEdit10.type_keys("5952")
        tnfissmenu.TnMaskEdit9.type_keys("7")
        
        tnfissmenu.TnMaskEdit6.type_keys(caminhoTomado) # caminho 

        tnfissmenu.Static.click()
        # tnfissmenu.nToolBar.type_keys('{F9}')
            #time.sleep(10)
        while(True):
            try:
                tnfissmenu.Static2.wait('visible')
                tnfissmenu.Static.wait('visible')
                time.sleep(3)
                tnfissmenu.Static.click()
                print('NFC-e Importado')
                conteudo = "NFe Entradas foi Importado\n"
                relatorio.relatorioPftr(conteudo)
                break
            except:
                time.sleep(2)

    except:
        print("Nao foi possivel concluir a importacao")
    