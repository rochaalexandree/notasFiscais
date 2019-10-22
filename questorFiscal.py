from pywinauto.application import Application
import pyautogui
import time
import getData
import extrairArq
import tratarDados
import relatorio
from pywinauto import keyboard
from pywinauto.keyboard import send_keys

def importar(tipo, codigoEmpresa, caminhoNFe, caminhoNFC, caminhoNFeEntrada, filiais, posicaoAtual, stop):
    
    app = Application().start(cmd_line=u'D:/nQuestor/nfis.exe')
    
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
    while(True):
        try:
            tnfrmloginquestor[u'3'].type_keys('administrador')
            time.sleep(1)
            tnfrmloginquestor[u'4'].type_keys('masterkey')
            tnfrmloginquestor.TnButton2.click()
            break
        except:
            time.sleep(2)
            pass

    estaduaisNFs(caminhoNFe, caminhoNFC, caminhoNFeEntrada, app, codigoEmpresa, filiais, posicaoAtual, stop)
    

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

def estaduaisNFs(caminhoNFe, caminhoNFC, caminhoNFeEntrada, app, codigoEmpresa, filiais, posicaoAtual, stop):
    posiCami = posicaoAtual
    pare = stop
    
    while(True):
        try:
            if caminhoNFe[posiCami] != "vazio" or caminhoNFC[posiCami] != "vazio" or caminhoNFeEntrada[posiCami] != "vazio":
                if(posiCami == pare):
                    break
                try:
                    if posiCami == posicaoAtual:
                        escolherEmpresa(app, codigoEmpresa[posiCami], filiais[posiCami])
                    else:
                        # Adicionar código e número de filial
                        app.TnFisSMenu.TnMaskEdit16.wait('visible')
                        send_keys(codigoEmpresa[posiCami])
                        time.sleep(2)
                        app.TnFisSMenu.TnMaskEdit16.type_keys(filiais[posiCami])
                        time.sleep(1)
                        pass
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
                        
                        # garante que só vai acessar o menu na primeira execução
                        if posiCami == posicaoAtual:
                            tnfissmenu.menu_item(u'Ar&quivos->#2->#2').click()
                            
                        while(True):
                            try:
                                tnfissmenu.TnComboBox4.wait("visible")
                                time.sleep(1)
                                break
                            except:
                                time.sleep(2)
                        try:
                            if posiCami == posicaoAtual:
                                app.TnFisSMenu.TnComboBox28.select('Ambos')
                                time.sleep(1)
                                app.TnFisSMenu.TnComboBox26.select('Não Permitir Erros')
                                time.sleep(1)
                                app.TnFisSMenu.TnComboBox24.select('Importar Somente não Importados')
                                time.sleep(1)
                                app.TnFisSMenu.TnComboBox22.select('Sim')
                                time.sleep(1)
                                app.TnFisSMenu.TnComboBox20.select('Não')
                                time.sleep(1)
                                app.TnFisSMenu.TnComboBox18.select('Não')
                                time.sleep(1)
                                app.TnFisSMenu.TnComboBox16.select('Não')
                                time.sleep(1)
                                app.TnFisSMenu.TnComboBox14.select('Não')
                                time.sleep(1)
                                app.TnFisSMenu.TnComboBox12.select('Sim')
                                time.sleep(1)
                                app.TnFisSMenu.TnComboBox10.select('Não Importar')
                                time.sleep(1)
                                app.TnFisSMenu.TnComboBox8.select('Outras')
                                time.sleep(1)
                                app.TnFisSMenu.TnComboBox6.select('Outras')
                                time.sleep(1)
                                tnfissmenu.TnComboBox4.select("Vários Arquivos")
                            #tnfissmenu.nToolBar.print_control_identifiers()
                            tnfissmenu.TnMaskEdit9.type_keys(caminhoNFe[posiCami])
                            tnfissmenu.nToolBar.type_keys('{F9}')
                            #time.sleep(10)
                            while(True):
                                try:
                                    # tnfissmenu[u'22'].wait("visible")
                                    tnfissmenu.Static2.wait('visible')
                                    tnfissmenu.Static.wait("visible")
                                    time.sleep(3)
                                    tnfissmenu.Static.wait("visible")

                                    # relatório fica aqui
                                    # print(tnfissmenu.TnTreeView.texts())
                                    # tnfissmenu.TnTreeView.set_focus().click_input(button='right')
                                    
                                    # time.sleep(2)
                                    # print ([item['text'] for item in app.PopupMenu.menu_items()])
                                    # app.PopupMenu.menu_item(u'&Gravar em Arquivo...').click_input()
                                    
                                    

                                    tnfissmenu.Static.click()

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
                    
                    if not(caminhoNFeEntrada[posiCami] == 'vazio'):
                        estaduaisNFsEntrada(caminhoNFeEntrada, app, posiCami)
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
                    # tnfissmenu[u'22'].wait("visible")
                    
                    tnfissmenu.Static2.wait('visible')
                    tnfissmenu.Static.wait("visible")
                    time.sleep(3)
                    tnfissmenu.Static.wait("visible")



                    tnfissmenu.Static.click()

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


def estaduaisNFsEntrada(caminhoNFeEntrada, app, posiCami):
    while(True):
            try:
                app.TnFisSMenu.wait("visible")
                break
            except:
                time.sleep(2)

    while(True):
        try:
            tnfissmenu = app.TnFisSMenu
            tnfissmenu.TnComboBox4.wait("visible")
            break
        except:
            time.sleep(2)
    while(True):
        try:
            tnfissmenu.TnComboBox4.select("Vários Arquivos")
            #tnfissmenu.nToolBar.print_control_identifiers()
            tnfissmenu.TnMaskEdit9.type_keys(caminhoNFeEntrada[posiCami])
            tnfissmenu.nToolBar.type_keys('{F9}')
            #time.sleep(10)
            while(True):
                try:
                    # tnfissmenu[u'22'].wait("visible")
                    
                    tnfissmenu.Static2.wait('visible')
                    tnfissmenu.Static.wait("visible")
                    time.sleep(3)
                    tnfissmenu.Static.wait("visible")



                    tnfissmenu.Static.click()

                    print('NFe de Entrada Importado')
                    conteudo = "NFe de Entrada Importado\n"
                    relatorio.relatorioSER(conteudo)
                    break
                except:
                    time.sleep(2)
            
            break
        except:
            print('Problema na importacao do NFe de Entrada')
            time.sleep(2)
    
    time.sleep(5)