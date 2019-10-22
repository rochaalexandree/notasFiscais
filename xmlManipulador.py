import xml.etree.ElementTree as ET

def alteraXML(path):
    doc = ET.parse(path)

    root = doc.getroot()

    #print (root.tag, root.attrib['nfse:Competencia'])
    competencias = []
    
    for child in root.iter('{http://www.abrasf.org.br/nfse.xsd}Competencia'):
        competencias.append(child.text) 
        #print (child.text) 
    
    x = 0
    for child in root.iter('{http://www.abrasf.org.br/nfse.xsd}DataEmissao'):
        emissao = child.text
        print('texto Originial: ' + child.text)
        try:
            particiona = emissao.split('T')
            emissaoFinal = competencias[x] + 'T' + particiona[1]
            child.text = emissaoFinal
            print('texto alterado: ' + child.text + '\n'*2)
            x = x + 1
        except:
            pass
            
        
    for i in root.iter('{http://www.abrasf.org.br/nfse.xsd}DataEmissao'):
        print(i.text)    
    
        
        #print (child.text)
    
    doc.write(path)


if __name__ == "__main__":
    alteraXML('C:/Users/rocha/Downloads/NFSe.xml')