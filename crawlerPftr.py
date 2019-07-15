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


def prefeitura(browser, inscricaoMunic, cnpjList, posicaoAtual):
    
    try:
        browser.get('https://sispmjp.joaopessoa.pb.gov.br:8080/sispmjp/login.jsf')
        browser.maximize_window()
    except:
        conteudo = "Sem acesso ao site da prefeitura ou a internet\n"
        relatorio.relatorioPftr(conteudo)
        #area.insert(END,conteudo)
        print('Sem acesso ao site ou a internet')
        passar = False
    ## Faz o login ##
    
    while(True):
        try:
            boolean = entrarNoSistema(browser)
            if(boolean == True):
                pare = posicaoAtual
                while(posicaoAtual + 10 > pare):
                    try:
                        representarContri(browser, inscricaoMunic[pare], cnpjList[pare])
                        pare = pare + 1
                    except:
                        break
            break
        except:
            print('exportação finalizada ou bloqueada')
            conteudo = "exportação finalizada ou bloqueada\n"
            relatorio.relatorioPftr(conteudo)
            break
            
    browser.close()
#Vai até o estado para representar o contibuinte
def representarContri(browser, inscricaoMunic, cnpj):
    while(True):
        try:
            browser.get('https://sispmjp.joaopessoa.pb.gov.br:8080/sispmjp/paginas/ds/DS_GerenciarContribuinte.jsf')
            break
        except:
            time.sleep(2)
    
    while(True):
        try:
            browser.find_element_by_xpath('//*[@id="form:contribuintesVinculados:j_idt64:filter"]').clear()
            inscricaoMunic = inscricaoMunic.strip()
            inscricaoMunic = inscricaoMunic.lstrip('0 ')
            browser.find_element_by_xpath('//*[@id="form:contribuintesVinculados:j_idt64:filter"]').send_keys(inscricaoMunic)
            break
        except:
            time.sleep(2)

    time.sleep(3)
    while(True):
        try:
            browser.find_element_by_xpath('//*[@id="form:contribuintesVinculados:0:commandButton_representarContribuinte"]').click()
            time.sleep(3)
            while(True):
                try:
                    browser.find_element_by_xpath('//*[@id="form:confirmRepresentar"]').click()
                    time.sleep(3)
                    break
                except:
                    pass
        except:
            try:
                mensagem = browser.find_element_by_xpath('//*[@id="form:contribuintesVinculados_data"]/tr/td').text
                if(mensagem == 'Nenhum contribuinte encontrado'):
                    caminhos.addCaminhoPftrTomado("vazio")
                    caminhos.addCaminhoPftrPrestado("vazio")
                    break
            except:
                pass
            time.sleep(2)
    
        try:
            try:
                browser.find_element_by_xpath('//*[@id="j_idt47:msgPrincipal"]/div/ul/li/span[1]')
                caminhos.addCaminhoPftrTomado("vazio")
                caminhos.addCaminhoPftrPrestado("vazio")
                break
            except:
                browser.find_element_by_xpath('//*[@id="form:contribuintesVinculados_data"]/tr/td')
            time.sleep(3)
        except:
            boolean = True
            while(boolean):
                try:
                    browser.find_element_by_xpath('//*[@id="formMensagens:commandButton_confirmar"]').click()
                    time.sleep(2)
                except:
                    boolean = False
                    time.sleep(2)
            
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
                        while(True):
                            try:
                                elem = browser.find_element_by_xpath('//*[@id="dataTable_data"]/tr/td')
                                break
                            except:
                                pass
                        elemento = elem.text
                        if(elemento.isdigit()):
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
                        
                        while(True):
                            try:
                                elem = browser.find_element_by_xpath('//*[@id="dataTable_data"]/tr/td')
                                break
                            except:
                                pass
                        elemento = elem.text
                        
                        if(elemento.isdigit()):
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
                        browser.find_element_by_xpath('//*[@id="j_idt10:j_idt11"]').click()
                    except:
                        try:
                            browser.find_element_by_xpath('//*[@id="j_idt10"]').click()
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
                            entrarNoSistema(browser)
                        except:
                            print('Não estava pedindo pra trocar de senha')
                        break
                    print('tentando de novo')
            break
                        
def entrarNoSistema(browser):
    pare = 0
    while (True):
        try:
            browser.find_element_by_xpath('//*[@id="j_username"]').clear()
            browser.find_element_by_xpath('//*[@id="j_password"]').clear()
            browser.find_element_by_xpath('//*[@id="j_username"]').send_keys("01870094000112")
            browser.find_element_by_xpath('//*[@id="j_password"]').send_keys("RC002834")
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
                browser.find_element_by_xpath('//*[@id="formMensagens:commandButton_confirmar"]').click()#Passa dos avisos
                time.sleep(2)
            except:
                boolean = False
                time.sleep(1)
        
        browser.find_element_by_xpath('//*[@id="form_msg3:j_idt62"]/tbody/tr[2]/td[1]/div/div[2]').click()#Marca a caixa de contabilista
        time.sleep(2)
        browser.find_element_by_xpath('//*[@id="form_msg3:j_idt57"]/span[2]').click() #Avança
        time.sleep(2)
        #browser.find_element_by_xpath('//*[@id="formMenuPrincipal:menuPrincipal"]/ul/li[2]/ul/li/a').click() #Seleciona contribuintes e contabilistas
    except:
        time.sleep(2)
        print('Não foi possível fazer login')
        conteudo = "Não foi possível fazer o login no site da prefeitura\n"
        relatorio.relatorioPftr(conteudo)
        browser.get('https://sispmjp.joaopessoa.pb.gov.br:8080/sispmjp/login.jsf')
        time.sleep(2)
        entrarNoSistema(browser)
        return False
    return True