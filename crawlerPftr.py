from selenium import webdriver
import time
import pyautogui
import extrairArq
import getData
import relatorio
import caminhos
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC 
from selenium.webdriver.support.ui import WebDriverWait as wait


def prefeitura(browser, cnpjList, posicaoAtual, senha, cnpjFormatado):
    
    try:
        browser.get('https://sispmjp.joaopessoa.pb.gov.br:8080/sispmjp/login.jsf')
        browser.maximize_window()
    except:
        conteudo = "Sem acesso ao site da prefeitura ou a internet\n"
        relatorio.relatorioPftr(conteudo)
        #area.insert(END,conteudo)
        print('Sem acesso ao site ou a internet')
    
    ## Pega os usuarios ##

    try:
        #ler quantidade de usuarios#
        qtdUsuarios = len(cnpjList)
    except:
        pass
    
    
    ## Faz o login ##
    cont = 0
    
    while(cont < qtdUsuarios):
        try:
            boolean = entrarNoSistema(browser, cnpjFormatado[cont], senha[cont])
            if(boolean == True):
                #pare = posicaoAtual
                # while(posicaoAtual + 10 > pare):
                try:
                    representarContri(browser, cnpjList[cont], senha[cont], cnpjFormatado[cont])
                    cont = cont + 1
                    #pare = pare + 1
                    #clicar em sair
                except:
                    pass
                    #break
            #break
        except:
            print('exportação finalizada ou bloqueada')
            conteudo = "exportação finalizada ou bloqueada\n"
            relatorio.relatorioPftr(conteudo)
            break
            
    browser.close()
#Vai até o estado para representar o contibuinte
def representarContri(browser, cnpj, senha, cnpjFormatado):
    while(True):
        
        pare = 0
        
        while(True):
            try:
                try:
                    browser.get('https://sispmjp.joaopessoa.pb.gov.br:8080/sispmjp/paginas/ds/DS_ConsultarNFSePrestador.jsf')
                    time.sleep(1)
                    browser.find_element_by_xpath('//*[@id="form:dtComp_input"]').send_keys(getData.get_dataInicial(2))
                    time.sleep(1)
                    browser.find_element_by_xpath('//*[@id="form:compFim_input"]').send_keys(getData.get_dataFinal(2))
                    time.sleep(1)
                    browser.find_element_by_xpath('//*[@id="form:nrNfse"]').click()
                    time.sleep(1)
                    browser.find_element_by_xpath('//*[@id="form:j_idt60"]').click()
                    time.sleep(3)
                    
                    tempo = 0
                    while(True):
                        try:
                            elem = browser.find_element_by_xpath('//*[@id="dataTable_data"]/tr/td')
                            break
                        except:
                            if(tempo == 10):
                                break    
                            time.sleep(3)
                            tempo = tempo + 1
                            
                    elemento = elem.text

                    numeroNFS = 'string'
                    try:
                        numeroNFS = browser.find_element_by_xpath('//*[@id="dataTable_data"]/tr[1]/td[1]').text
                    except:
                        pass

                    if(elemento.isdigit() or numeroNFS.isdigit()):
                        try:
                            browser.find_element_by_xpath('//*[@id="commandButton_exportar"]').click()
                            time.sleep(3)
                            caminho = caminhos.getCaminho(1).replace('\n', '')
                            destino = caminho + getData.get_dataInicial(3) + '/' + cnpj + '/Prestado'
                            extrairArq.mover(caminho, destino, "Prestado")
                            conteudo = "Download realizado: " + cnpj + "\n"
                            relatorio.relatorioPftr(conteudo)
                            #area.insert(END,conteudo)
                        except:
                            print('Não foi possível mover o arquivo do Prestador para a pasta')
                    else:  
                        caminhos.addCaminhoPftrPrestado("vazio")
                except:
                    caminhos.addCaminhoPftrPrestado("vazio")

                try:
                    browser.get('https://sispmjp.joaopessoa.pb.gov.br:8080/sispmjp/paginas/ds/DS_ConsultarNFSeTomador.jsf')
                    time.sleep(1)
                    browser.find_element_by_xpath('//*[@id="form:dtComp_input"]').send_keys(getData.get_dataInicial(2))
                    time.sleep(1)
                    browser.find_element_by_xpath('//*[@id="form:compFim_input"]').send_keys(getData.get_dataFinal(2))
                    time.sleep(1)
                    browser.find_element_by_xpath('//*[@id="form:nrNfse"]').click()
                    time.sleep(1)
                    browser.find_element_by_xpath('//*[@id="form:j_idt60"]').click()
                    time.sleep(3)
                    
                    tempo = 0
                    while(True):
                        try:
                            elem = browser.find_element_by_xpath('//*[@id="dataTable_data"]/tr/td')
                            break
                        except:
                            if(tempo == 10):
                                break    
                            time.sleep(3)
                            tempo = tempo + 1

                    elemento = elem.text

                    try:
                        mensagem = browser.find_element_by_xpath('//*[@id="dataTable_data"]/tr[1]/td[2]/span').text 
                    except:
                        pass
                    # //*[@id="dataTable_data"]/tr[2]/td[2]/span

                    if(elemento.isdigit() or mensagem.isdigit()):
                        try:
                            browser.find_element_by_xpath('//*[@id="commandButton_exportar"]').click()
                            time.sleep(3)
                            caminho = caminhos.getCaminho(1).replace('\n', '')
                            destino = caminho + getData.get_dataInicial(3) + '/' + cnpj + '/Tomado'
                            extrairArq.mover(caminho, destino, "Tomado")
                            conteudo = "Download realizado: " + cnpj + "\n"
                            relatorio.relatorioPftr(conteudo)
                            #area.insert(END,conteudo)
                        except:
                            print('Não foi possível mover o arquivo do Tomador para a pasta')
                    else:
                        caminhos.addCaminhoPftrTomado("vazio")
                except:
                    caminhos.addCaminhoPftrTomado("vazio")
                ## Sair da representação ##
                try:
                    browser.find_element_by_xpath('//*[@id="menu_topo"]/ul/li[6]/a"]').click()
                    time.sleep(1)
                except:
                    print('Não quer sair da representação')
                time.sleep(2)
                break
                #M D COMERCIO DE VEICULOS PEÇAS E SERVICOS LTDA
                #Não possui inscrição municipal
            except:
                pare = pare + 1
                if pare == 2:
                    print('Download não realizado: ' + cnpj)
                    conteudo = "Download não realizado: " + cnpj + "\n"
                    relatorio.relatorioPftr(conteudo)
                    try:
                        browser.find_element_by_xpath('//*[@id="formAlterarSenha:continuar"]/span[2]').click()
                        time.sleep(2)
                        browser.find_element_by_xpath('//*[@id="menu_topo"]/ul/li[6]/a').click()
                        time.sleep(2)
                        entrarNoSistema(browser, cnpjFormatado, senha)
                    except:
                        print('Não estava pedindo pra trocar de senha')
                    break
                print('tentando de novo')
        break
                        
def entrarNoSistema(browser, cnpj, senha):
    pare = 0
    while (True):
        try:
            browser.find_element_by_xpath('//*[@id="j_username"]').clear()
            browser.find_element_by_xpath('//*[@id="j_password"]').clear()
            # acesso = caminhos.usuarioSenha()
            browser.find_element_by_xpath('//*[@id="j_username"]').send_keys(cnpj)
            browser.find_element_by_xpath('//*[@id="j_password"]').send_keys(senha)
            time.sleep(1)
            break
        except:
            if(pare == 4):
                break
            pare = pare + 1

    try:
        browser.find_element_by_xpath('//*[@id="commandButton_entrar"]').click()#Entra
        time.sleep(2)
        boolean = True
        while (boolean):
            try:
                browser.find_element_by_xpath('/html/body/div[1]/div[3]/div/form[2]/fieldset/table/tfoot/tr/td/button[2]/span[2]').click()
                # browser.find_element_by_xpath('//*[@id="formMensagens:commandButton_confirmar"]').click()#Passa dos avisos
                time.sleep(2)
            except:
                boolean = False
                time.sleep(1)
        
    except:
        time.sleep(2)
        print('Não foi possível fazer login')
        conteudo = "Não foi possível fazer o login no site da prefeitura\n"
        relatorio.relatorioPftr(conteudo)
        browser.get('https://sispmjp.joaopessoa.pb.gov.br:8080/sispmjp/login.jsf')
        time.sleep(2)
        entrarNoSistema(browser, cnpj, senha)
        return False
    return True