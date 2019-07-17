from selenium import webdriver
import time
import pyautogui
import extrairArq
import getData
import relatorio
import caminhos
import tratarDados
import certificado
import questorFiscal
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC 
from selenium.webdriver.support.ui import WebDriverWait as wait 

def servirtual(browser, lista, tipoDeNota, posicaoAtual):
    execute = posicaoAtual #Controla as execuções
    login = posicaoAtual #Garante que o login só será feito uma vez a cada 15 minutos 
    parada = len(lista) #limite temporário de execução
    cnpj = posicaoAtual
    start = True
    
    while(execute < parada):
        if execute == parada:
            break
        #try:
            ## Vai para pagina e o iframe desejado da página ##
        if login == posicaoAtual:
            try:
                browser.get('https://www.receita.pb.gov.br/ser/servirtual')
                browser.maximize_window()
            except:
                print("Sem acesso a página principal ou a internet")
                conteudo = "Sem acesso a página principal ou a internet\n"
                relatorio.relatorioSER(conteudo)
                start = False
            inicio = 0
            while(start):
                try:
                    wait(browser, 2).until(EC.frame_to_be_available_and_switch_to_it("acessoATF"))
                    time.sleep(2)
                    #browser.find_element_by_css_selector('#SERlogin > form > div:nth-child(12) > div > a').click() #Acessa o certificado Digital
                    browser.find_element_by_xpath('//*[@id="form-cblogin-username"]/div/input').send_keys('jos00004')
                    browser.find_element_by_xpath('//*[@id="form-cblogin-password"]/div[1]/input').send_keys('RC072019')
                    browser.implicitly_wait(2)
                    login = login + 1
                    start = False
                except:
                    time.sleep(1)
                    if(inicio == 29):
                        print("Sem acesso a página principal ou a internet")
                        conteudo = "Sem acesso a página principal ou a internet\n"
                        relatorio.relatorioSER(conteudo)
                        break
                    inicio = inicio + 1
            
            if(inicio == 29):
                break
            
            browser.switch_to.default_content()
            time.sleep(3)
            

        time.sleep(3)
        try:
            if cnpj > 0:
                browser.get('https://www.receita.pb.gov.br/ser/servirtual')
        except:
            print("Sem acesso a página principal ou a internet")
            conteudo = "Sem acesso a página principal ou a internet\n"
            relatorio.relatorioSER(conteudo)
        if(tipoDeNota == 'NFe'):
            cnpj = preencheDadosSER1(browser, cnpj, lista)
            preencheDadosSERentrada(browser, cnpj, lista)
        elif(tipoDeNota == 'NFC'):
            cnpj = preencheDadosSER2(browser, cnpj, lista) 
        
        cnpj = cnpj + 1
        browser.switch_to.default_content()
        execute = execute + 1
        time.sleep(3)
        if((execute > 9) and ((execute % 10) == 0)):
            break
        if cnpj == parada:
            break
    
    browser.close()
    return lista

def preencheDadosSER1(browser, cnpj, lista):
    
    try:
        browser.get('https://www.receita.pb.gov.br/ser/servirtual/documentos-fiscais/nf-e/nfe-xml') 
        try:
            wait(browser, 2).until(EC.frame_to_be_available_and_switch_to_it("iframe"))
            element = browser.find_element_by_xpath('/html/body/table/tbody/tr[2]/td/form/table/tbody/tr[2]/td[2]/input[1]')         
            element.clear()
            element.send_keys(getData.get_dataInicial(1))
            time.sleep(3)

            element = browser.find_element_by_xpath('/html/body/table/tbody/tr[2]/td/form/table/tbody/tr[2]/td[2]/input[2]')
            element.clear()
            element.send_keys(getData.get_dataFinal(1))
            time.sleep(3)

            browser.find_element_by_xpath('/html/body/table/tbody/tr[2]/td/form/table/tbody/tr[7]/td/table/tbody/tr[1]/td[2]/select/option[2]').click()#seleciona CNPJ
            time.sleep(2)
            wait(browser, 2).until(EC.frame_to_be_available_and_switch_to_it("cmpDest"))
            browser.find_element_by_xpath('//*[@id="Layer1"]/table/tbody/tr/td/form/table/tbody/tr[1]/td[2]/input').clear()
            browser.find_element_by_xpath('//*[@id="Layer1"]/table/tbody/tr/td/form/table/tbody/tr[2]/td[2]/input[1]').clear()
            
            browser.switch_to.default_content()
            wait(browser, 2).until(EC.frame_to_be_available_and_switch_to_it("iframe"))

            wait(browser, 2).until(EC.frame_to_be_available_and_switch_to_it("cmpEmit"))    
            browser.find_element_by_xpath('//*[@id="Layer1"]/table/tbody/tr/td/form/table/tbody/tr[1]/td[2]/input').send_keys(lista[cnpj]) #Digita CNPJ
            time.sleep(5)
            browser.find_element_by_xpath('//*[@id="Layer1"]/table/tbody/tr/td/form/table/tbody/tr[1]/td[3]/input').click() #Pesquisa
            time.sleep(2)
            browser.switch_to.default_content()
            wait(browser, 2).until(EC.frame_to_be_available_and_switch_to_it("iframe"))
            #browser.find_element_by_xpath('/html/body/table/tbody/tr[2]/td/form/table/tbody/tr[8]/td[2]/select/option[16]').click()#Seleciona PB
            browser.find_element_by_xpath('/html/body/table/tbody/tr[2]/td/form/table/tbody/tr[13]/td/select/option[2]').click()#Seleciona XML
            time.sleep(2)
            browser.find_element_by_xpath('/html/body/table/tbody/tr[2]/td/form/table/tbody/tr[13]/td/input[4]').click() #Consultar
            time.sleep(3)
            try:
                try:
                    browser.find_element_by_xpath('/html/body/table/tbody/tr[2]/td/form/table/tbody/tr[14]/td/b/i/a')
                    browser.switch_to.default_content()
                    getSERXML(browser, cnpj, lista)
                except:
                    browser.switch_to_alert().accept()
                    caminhos.addCaminhoNFe('vazio') 
                    print("Sem acesso a essa área")
            except:
                caminhos.addCaminhoNFe('vazio')
                print("Não era um alerta")
        except:
            caminhos.addCaminhoNFe('vazio')
            print('Erro no preenchimento dos dados')
    except:
        caminhos.addCaminhoNFe('vazio')
        print('Erro no acesso a página')
        conteudo = "Sem acesso a página dos Documentos fiscais de " + lista[cnpj] + " ou a internet\n"
        relatorio.relatorioSER(conteudo)
    return cnpj    

def preencheDadosSERentrada(browser, cnpj, lista):

    try:
        browser.get('https://www.receita.pb.gov.br/ser/servirtual/documentos-fiscais/nf-e/nfe-xml') 
        try:
            wait(browser, 2).until(EC.frame_to_be_available_and_switch_to_it("iframe"))
            element = browser.find_element_by_xpath('/html/body/table/tbody/tr[2]/td/form/table/tbody/tr[2]/td[2]/input[1]')         
            element.clear()
            element.send_keys(getData.get_dataInicial(1))

            element = browser.find_element_by_xpath('/html/body/table/tbody/tr[2]/td/form/table/tbody/tr[2]/td[2]/input[2]')
            element.clear()
            element.send_keys(getData.get_dataFinal(1))

            browser.find_element_by_xpath('/html/body/table/tbody/tr[2]/td/form/table/tbody/tr[10]/td/table/tbody/tr[1]/td[2]/select/option[2]').click()#seleciona CNPJ

            wait(browser, 2).until(EC.frame_to_be_available_and_switch_to_it("cmpEmit"))
            browser.find_element_by_xpath('//*[@id="Layer1"]/table/tbody/tr/td/form/table/tbody/tr[1]/td[2]/input').clear()    
            browser.find_element_by_xpath('//*[@id="Layer1"]/table/tbody/tr/td/form/table/tbody/tr[2]/td[2]/input[1]').clear()
            
            browser.switch_to.default_content()
            wait(browser, 2).until(EC.frame_to_be_available_and_switch_to_it("iframe"))
            
            wait(browser, 2).until(EC.frame_to_be_available_and_switch_to_it("cmpDest"))
            
            browser.find_element_by_xpath('//*[@id="Layer1"]/table/tbody/tr/td/form/table/tbody/tr[1]/td[2]/input').send_keys(lista[cnpj]) #Digita CNPJ
            browser.find_element_by_xpath('//*[@id="Layer1"]/table/tbody/tr/td/form/table/tbody/tr[1]/td[3]/input').click() #Pesquisa
            browser.switch_to.default_content()
            wait(browser, 2).until(EC.frame_to_be_available_and_switch_to_it("iframe"))
            #browser.find_element_by_xpath('/html/body/table/tbody/tr[2]/td/form/table/tbody/tr[11]/td[2]/select[1]/option[16]').click()#Seleciona PB
            browser.find_element_by_xpath('/html/body/table/tbody/tr[2]/td/form/table/tbody/tr[13]/td/select/option[2]').click()#Seleciona XML

            browser.find_element_by_xpath('/html/body/table/tbody/tr[2]/td/form/table/tbody/tr[13]/td/input[4]').click() #Consultar
            time.sleep(3)
            try:
                try:
                    browser.find_element_by_xpath('/html/body/table/tbody/tr[2]/td/form/table/tbody/tr[14]/td/b/i/a')
                    browser.switch_to.default_content()
                    getSERXMLentrada(browser, cnpj, lista)
                    
                except:
                    browser.switch_to_alert().accept()
                    print("Sem acesso a essa área")
                    
            except:
                print("Não era um alerta")
            
        except:
            print('Erro no preenchimento dos dados')
            #controlExec = controlExec - 1
    except:
        print('Erro no acesso a página')
        conteudo = "Sem acesso a página dos Documentos fiscais de " + lista[cnpj] + " ou a internet\n"
        relatorio.relatorioSER(conteudo)
        #break
    return cnpj

def getSERXMLentrada(browser, cnpj, lista):
    start = True
    x = True
    cont = 0

    while(True):
        try:
            browser.get('https://www4.receita.pb.gov.br/atf/seg/SEGf_MinhasMensagens.do')
            time.sleep(3)
            break
        except:
            cont = cont + 1
            if cont == 3:
                start = False
                x = False
                break
            print('Sem acesso a https://www4.receita.pb.gov.br/atf/seg/SEGf_MinhasMensagens.do')
                
    ## Clica na primeira mensagem ##
    while(start):
        try:
            browser.find_element_by_css_selector("body > form > div > table > tbody > tr:nth-child(3) > td:nth-child(4) > a").click()
            time.sleep(5)
            break
        except:
            pass
    
    ## Clica na mensagem do meio ##
    pare = 0

    try:
        browser.find_element_by_xpath('/html/body/form/div/table/tbody/tr[5]/td[3]/a/img')
    except:
        try:
            browser.find_element_by_xpath('/html/body/form/div/table/tbody/tr[3]/td[3]')
            browser.find_element_by_xpath('/html/body/form/div/table/tbody/tr[5]/td[3]')
            browser.find_element_by_xpath('/html/body/form/div/table/tbody/tr[7]/td[3]')
            pare = 14
        except:
            pass
            
    while (x):
        try:
            try:
                browser.find_element_by_xpath('/html/body/form/div/table/tbody/tr[5]/td[3]/a/img')
                browser.find_element_by_css_selector("body > form > div > table > tbody > tr.tdAlternada > td:nth-child(4) > a").click()
                time.sleep(5)
                x = False
            except:
                pare = pare + 1
                if pare == 18:
                    break
                #time.sleep(2)
                browser.find_element_by_name("btnNovas").click()
                #browser.find_element_by_xpath('/html/body/form/div/table/tbody/tr[10]/td/input[2]').click()
                time.sleep(10)
                #print("mais uma")
        except:
            print("Não foi possível atualizar")
            time.sleep(1)
            break
            
    ## Faz o Download do XML##
    
    try:
        browser.find_element_by_css_selector("body > table > tbody > tr:nth-child(2) > td > form > table > tbody > tr:nth-child(8) > td > a").click()
        caminho = caminhos.getCaminho(0)
        destino = caminho + getData.get_dataInicial(3) + '/' + lista[cnpj] + '/NFe-Entrada'
        time.sleep(3)
        extrairArq.extrair(caminho, destino)
        print("Download e extração dos arquivos de " + lista[cnpj] +" realizada\n")
        conteudo = "Download e extração dos arquivos de " + lista[cnpj] +" realizada\n"
        try:
            relatorio.relatorioSER(conteudo)
        except:
            print('Erro ao adicionar ao relatorio')
    except:
        print('impossibilitado de fazer o download de ' + lista[cnpj])
        conteudo = "impossibilitado de fazer o download de " + lista[cnpj] + "\n"
        relatorio.relatorioSER(conteudo)

def getSERXML(browser, cnpj, lista):
    start = True
    x = True
    cont = 0

    while(True):
        try:
            browser.get('https://www4.receita.pb.gov.br/atf/seg/SEGf_MinhasMensagens.do')
            time.sleep(3)
            break
        except:
            cont = cont + 1
            if cont == 3:
                start = False
                x = False
                break
            print('Sem acesso a https://www4.receita.pb.gov.br/atf/seg/SEGf_MinhasMensagens.do')
                
    ## Clica na primeira mensagem ##
    while(start):
        try:
            browser.find_element_by_css_selector("body > form > div > table > tbody > tr:nth-child(3) > td:nth-child(4) > a").click()
            time.sleep(2)
            break
        except:
            pass
    
    ## Clica na mensagem do meio ##
    pare = 0

    try:
        browser.find_element_by_xpath('/html/body/form/div/table/tbody/tr[5]/td[3]/a/img')
    except:
        try:
            browser.find_element_by_xpath('/html/body/form/div/table/tbody/tr[3]/td[3]')
            browser.find_element_by_xpath('/html/body/form/div/table/tbody/tr[5]/td[3]')
            browser.find_element_by_xpath('/html/body/form/div/table/tbody/tr[7]/td[3]')
            pare = 14
        except:
            pass

    while (x):
        try:
            try:
                browser.find_element_by_xpath('/html/body/form/div/table/tbody/tr[5]/td[3]/a/img')
                browser.find_element_by_css_selector("body > form > div > table > tbody > tr.tdAlternada > td:nth-child(4) > a").click()
                time.sleep(2)
                x = False
            except:
                pare = pare + 1
                if pare == 18:
                    break
                browser.find_element_by_name("btnNovas").click()
                time.sleep(10)
                #print("mais uma")
        except:
            print("Não foi possível atualizar")
            time.sleep(1)
            break
            
    ## Faz o Download do XML##
    
    try:
        download = browser.find_element_by_css_selector("body > table > tbody > tr:nth-child(2) > td > form > table > tbody > tr:nth-child(8) > td > a")
        time.sleep(2)
        download.click()

        time.sleep(2)
        
        caminho = caminhos.getCaminho(0)
        destino = caminho + getData.get_dataInicial(3) + '/' + lista[cnpj] + '/NFE'
        time.sleep(3)
        extrairArq.extrair(caminho, destino)
        time.sleep(3)
        caminhos.addCaminhoNFe(destino)
        try:
            
            conteudo = "Download e extração dos arquivos de " + lista[cnpj] +" realizada\n"
            try:
                relatorio.relatorioSER(conteudo)
            except:
                print('Erro ao adicionar ao relatorio')
        except:
            print('Erro ao adicionar o código na lista de importação')
    except:
        caminhos.addCaminhoNFe('vazio')
        print('impossibilitado de fazer o download de ' + lista[cnpj])
        conteudo = "impossibilitado de fazer o download de " + lista[cnpj] + "\n"
        relatorio.relatorioSER(conteudo)

def preencheDadosSER2(browser, cnpj, lista):
    
    try:
        browser.get('https://www.receita.pb.gov.br/ser/servirtual/documentos-fiscais/nfc-e/consulta-por-emitente')
        try:    
            wait(browser, 2).until(EC.frame_to_be_available_and_switch_to_it("iframe"))
            element = browser.find_element_by_xpath('/html/body/table/tbody/tr[2]/td/form/table/tbody/tr[2]/td[2]/input[1]')
            element.clear()
            element.send_keys(getData.get_dataInicial(1))

            element = browser.find_element_by_xpath('/html/body/table/tbody/tr[2]/td/form/table/tbody/tr[2]/td[2]/input[2]')
            element.clear()
            element.send_keys(getData.get_dataFinal(1))
            browser.find_element_by_xpath('/html/body/table/tbody/tr[2]/td/form/table/tbody/tr[8]/td/table/tbody/tr[1]/td[2]/select/option[2]').click()
            wait(browser, 2).until(EC.frame_to_be_available_and_switch_to_it("cmpEmit"))
            browser.find_element_by_xpath('//*[@id="Layer1"]/table/tbody/tr/td/form/table/tbody/tr[1]/td[2]/input').clear()
            browser.find_element_by_xpath('//*[@id="Layer1"]/table/tbody/tr/td/form/table/tbody/tr[2]/td[2]/input[1]').clear()

            browser.find_element_by_xpath('//*[@id="Layer1"]/table/tbody/tr/td/form/table/tbody/tr[1]/td[2]/input').send_keys(lista[cnpj])
            browser.find_element_by_xpath('//*[@id="Layer1"]/table/tbody/tr/td/form/table/tbody/tr[1]/td[3]/input').click()
            browser.switch_to.default_content()
            
            wait(browser, 2).until(EC.frame_to_be_available_and_switch_to_it("iframe"))
            
            browser.find_element_by_xpath('/html/body/table/tbody/tr[2]/td/form/table/tbody/tr[12]/td/select/option[3]').click()
            browser.find_element_by_xpath('/html/body/table/tbody/tr[2]/td/form/table/tbody/tr[12]/td/input[3]').click()
            
            time.sleep(3)
            
            try:
                try:
                    browser.find_element_by_xpath('/html/body/table/tbody/tr[2]/td/form/table/tbody/tr[13]/td/b/i/a')
                    browser.switch_to.default_content()
                    getSERXML2(browser, cnpj, lista)
                except:
                    browser.switch_to_alert().accept()
                    caminhos.addCaminhoNFC('vazio')    
                    print("Sem acesso a essa área")
            except:
                caminhos.addCaminhoNFC('vazio')
                print("Não era um alert")
        except:
            caminhos.addCaminhoNFC('vazio')
            print('Erro no preenchimento dos dados')
    except:
        caminhos.addCaminhoNFC('vazio')
        print('Erro no acesso a página')
        conteudo = "Sem acesso a página dos Documentos fiscais de " + lista[cnpj] + " ou a internet\n"
        relatorio.relatorioSER(conteudo)

    return cnpj

def getSERXML2(browser, cnpj, lista):
    start = True #Controla o acesso ao segundo while
    x = True #Controla o acesso ao terceiro while
    cont = 0

    while(True):
        try:
            browser.get('https://www4.receita.pb.gov.br/atf/seg/SEGf_MinhasMensagens.do')
            time.sleep(4)
            break
        except:
            cont = cont + 1
            if cont == 3:
                start = False
                x = False
                break
            print('Sem acesso a https://www4.receita.pb.gov.br/atf/seg/SEGf_MinhasMensagens.do')

    ## Clica na priemira mensagem ##
    while(start):
        try:
            browser.find_element_by_css_selector("body > form > div > table > tbody > tr:nth-child(3) > td:nth-child(4) > a").click()
            time.sleep(2)
            break
        except:
            pass
        
    
    ## Clica na mensagem do meio ##
    pare = 0
    try:
        browser.find_element_by_xpath('/html/body/form/div/table/tbody/tr[5]/td[3]/a/img')
    except:
        try:
            browser.find_element_by_xpath('/html/body/form/div/table/tbody/tr[3]/td[3]')
            browser.find_element_by_xpath('/html/body/form/div/table/tbody/tr[5]/td[3]')
            browser.find_element_by_xpath('/html/body/form/div/table/tbody/tr[7]/td[3]')
            browser.find_element_by_xpath('/html/body/form/div/table/tbody/tr[9]/td[3]')
            pare = 14
        except:
            pass
    
    while (x):
        try:
            try:
                browser.find_element_by_xpath('/html/body/form/div/table/tbody/tr[5]/td[3]/a/img') #garante que o clipe está lá
                browser.find_element_by_css_selector("body > form > div > table > tbody > tr:nth-child(5) > td:nth-child(4) > a").click()
                time.sleep(2)
                x = False
            except:
                pare = pare + 1
                if pare == 18:
                    break
                time.sleep(2)
                browser.find_element_by_name("btnNovas").click()
                #browser.find_element_by_xpath('/html/body/form/div/table/tbody/tr[12]/td/input[2]').click()
                time.sleep(10)
                print("mais uma")
        except:
            print("Não foi possível atualizar")
            time.sleep(1)
            break
    
    ## Faz o Download do XML ##
    
    try:
        download = browser.find_element_by_css_selector("body > table > tbody > tr:nth-child(2) > td > form > table > tbody > tr:nth-child(8) > td > a")
        download.click()
        time.sleep(2)
        caminho = caminhos.getCaminho(0)
        destino = caminho + getData.get_dataInicial(3) + '/' + lista[cnpj] + '/NFCe'
        time.sleep(3)
        extrairArq.extrair(caminho, destino)
        caminhos.addCaminhoNFC(destino)
        print("Download e extração dos arquivos de " + lista[cnpj] +" realizada")
        conteudo = "Download e extração dos arquivos de " + lista[cnpj] +" realizada\n"
        relatorio.relatorioSER(conteudo)
    except:
        caminhos.addCaminhoNFC('vazio')
        print('impossibilitado de fazer o download')
        conteudo = "impossibilitado de fazer o download de " + lista[cnpj] + "\n"
        relatorio.relatorioSER(conteudo)
