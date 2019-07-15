from pywinauto.application import Application
import pyautogui
import time
import getData
import extrairArq
import tratarDados
import relatorio
from pywinauto import keyboard

def importar(tipo, codigoEmpresa, caminhoNFe, caminhoNFC, filiais, posicaoAtual):
    
    app = Application().start(cmd_line=u'C:/nQuestor/nfis.exe')
    
    tnfrmloginquestor = app.TnFrmLoginQuestor
            
    ## verifica se a página já está visível ##
    while(True):
        try:
            tnfrmloginquestor[u'4'].wait("visible")
            break
        except:
            time.sleep(2)

    ## faz o login ##
    time.sleep(2)
    tnfrmloginquestor[u'3'].type_keys('robcav')
    tnfrmloginquestor[u'4'].type_keys('masterkey')
    tnfrmloginquestor.TnButton2.click()

    estaduaisNFs(caminhoNFe, caminhoNFC, app, codigoEmpresa, filiais, posicaoAtual)
    

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
            print('Procurando a caixa de seleção de empresa')

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

def estaduaisNFs(caminhoNFe, caminhoNFC, app, codigoEmpresa, filiais, posicaoAtual):
    posiCami = posicaoAtual
    pare = posiCami + 10
    
    while(True):
        try:
            if caminhoNFe[posiCami] != "vazio" or caminhoNFC[posiCami] != "vazio":
                if(posiCami == pare):
                    break
                try:
                    escolherEmpresa(app, codigoEmpresa[posiCami], filiais[posiCami])
                except:
                    break

                while(True):
                    try:
                        app.TnFisSMenu.wait("visible")
                        break
                    except:
                        time.sleep(2)
                try:
                    if not(caminhoNFe[posiCami] == 'vazio'):
                        tnfissmenu = app.TnFisSMenu
                        tnfissmenu.menu_item(u'Ar&quivos->#1->#2').click()

                        while(True):
                            try:
                                tnfissmenu.TnComboBox4.wait("visible")
                                break
                            except:
                                time.sleep(2)
                        try:
                            tnfissmenu.TnComboBox4.select("Vários Arquivos")
                            #tnfissmenu.nToolBar.print_control_identifiers()
                            tnfissmenu.TnMaskEdit9.type_keys(caminhoNFe[posiCami])
                            tnfissmenu.nToolBar.type_keys('{F9}')
                            #time.sleep(10)
                            while(True):
                                try:
                                    tnfissmenu[u'22'].wait("visible")
                                    tnfissmenu.Static2.wait_not('visible')
                                    print('NF-e Importado')
                                    conteudo = "NF-e Importado\n"
                                    relatorio.relatorioSER(conteudo)
                                    break
                                except:
                                    time.sleep(2)
                        except:
                            print('Problema na importacao do NF-e')

                        
                except:
                    print('Não há mais arquivos NFs para importar')
                    break
                try:
                    #Verifica se o proximo caminho leva a um NFC-e para que ele não avance antes de importar  
                    if not(caminhoNFC[posiCami] == 'vazio'):  
                        estaduaisNFCs(caminhoNFC, app, posiCami)
                except:
                    print('Não há mais arquivos NFCs para importar')
                    break
                
            posiCami = posiCami + 1
        except:
            break

def estaduaisNFCs(caminho, app, posiCami):
    while(True):
            try:
                app.TnFisSMenu.wait("visible")
                break
            except:
                time.sleep(2)

    while(True):
        try:
            tnfissmenu = app.TnFisSMenu
            tnfissmenu[u'21'].wait("visible")
            #tnfissmenu.menu_item(u'#0->&Fechar\tCtrl+F4')
            time.sleep(3)
            tnfissmenu.menu_item(u'#0->&Fechar\tCtrl+F4').click()
            tnfissmenu.menu_item(u'Ar&quivos->#1->#2').click()
            break
        except:
            time.sleep(3)

    while(True):
        try:
            tnfissmenu.TnComboBox4.wait("visible")
            break
        except:
            time.sleep(2)
    while(True):
        try:
            tnfissmenu.TnComboBox4.select("Vários Arquivos")
            #tnfissmenu.nToolBar.print_control_identifiers()
            tnfissmenu.TnMaskEdit9.type_keys(caminho[posiCami])
            tnfissmenu.nToolBar.type_keys('{F9}')
            #time.sleep(10)
            while(True):
                try:
                    tnfissmenu[u'22'].wait("visible")
                    tnfissmenu.Static2.wait_not('visible')
                    print('NFC-e Importado')
                    conteudo = "NFC-e Importado\n"
                    relatorio.relatorioSER(conteudo)
                    break
                except:
                    time.sleep(2)
            
            break
        except:
            print('Problema na importacao do NFC-e')
            time.sleep(2)
    
    time.sleep(5)
