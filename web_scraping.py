#importação das bibliotecas
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
from time import sleep

class web_scraping(object):

    
    def __init__(self, lista_destinos):
        self.lista_destinos = lista_destinos
    
    def preencher_campos(self, destino_1, destino_2):
    
        #Tentar encontrar o campo endereço de partida
        partida = driver.find_elements_by_id('directions-searchbox-0')
        
        #Verificar se o campo end. partida já foi carregado
        while partida == []:
            sleep(0.05)
            partida = driver.find_elements_by_id('directions-searchbox-0')
            
        partida = partida[0].find_element_by_css_selector('div div input')
        partida.click()
        partida.send_keys(Keys.DELETE)
        partida.send_keys(destino_1)
        partida.send_keys(Keys.ENTER)
        
        #Encontrar e preencher campo do end. de chegada
        destino = driver.find_elements_by_id('directions-searchbox-1')
        destino = destino[0].find_element_by_css_selector('div div input')
        destino.click()
        destino.send_keys(Keys.DELETE)   
        destino.send_keys(destino_2)
        destino.send_keys(Keys.ENTER)
        
        
    def pegar_distancia(self, destino_1, destino_2):
        
        endereco_1 = destino_1["Endereço"]
        endereco_2 = destino_2["Endereço"]
        
        #Preencher os campos de origem e destino
        self.preencher_campos(endereco_1, endereco_2)
        
        #Tentar encontar a rota
        box_resultado = driver.find_elements_by_id("section-directions-trip-0")
        
        contator = 0
        tentativa = 0
        
        #Verificar se a rota já foi carregada
        while box_resultado == []:
                        
            #Esperar até 10 segundos para carregar
            if contator < 100:
                sleep(0.05)
                contator = contator + 1
                
            #Se não carregar, fechar a conexão e abrir outra janela
            else:
                
                if tentativa == 2:
                    distancia = 100000
                    return distancia
                
                elif tentativa == 1:
                    
                    cep_1 = destino_1["CEP"]
                    cep_2 = destino_2["CEP"]
                    
                    self.preencher_campos(cep_1, cep_2)
                    tentativa = tentativa + 1 
                    contator = 0
                    
                else:    
                    driver.quit()
                    self.criar_conexao()
                    self.preencher_campos(endereco_1, endereco_2)
                    tentativa = tentativa + 1 
                    contator = 0
             
             #Tentar encontar a rota
            box_resultado = driver.find_elements_by_id("section-directions-trip-0")
    
        #Clicar na rota
        box_resultado[0].click()
        
        #Encontar o valor da distância
        box_distancia = driver.find_elements_by_class_name('section-trip-summary-subtitle')
        
        #Verificar se o campo distância já foi carregado
        while box_distancia == []:
            sleep(0.05)
            box_distancia = driver.find_elements_by_class_name('section-trip-summary-subtitle')
        
        distancia = box_distancia[0].find_element_by_css_selector('span').text
        distancia = distancia.split()
        distancia = distancia[0]
        distancia = distancia.replace(",", ".")
        distancia = float(distancia)
        
        #Encontar e clicar no botão de voltar
        box_voltar = driver.find_elements_by_id("pane")
        botao_voltar = box_voltar[0].find_element_by_css_selector('div div div div div button')
        botao_voltar.click()
        
        #Retornar distância
        return distancia
    
    def criar_conexao(self):
        
        #caminho aonde está salvo o chromedriver
        DRIVER_PATH = 'C:/Users/DBI5/Documents/TCC/chromedriver.exe'
        
        #passar opções
        options = Options()
        options.headless = False
        
        #Criar a conexão com o página
        global driver
        driver = webdriver.Chrome(options=options, executable_path=DRIVER_PATH)
        
        #Abrir página do Google Maps
        driver.get("https://www.google.com.br/maps/dir/")
    
    
    def distancia_entre_destinos(self):

        self.criar_conexao()
            
        #Loop para combinar todos os destinos
        lista_distancias = {}
        
        for i in range(len(self.lista_destinos)):
            for j in range(len(self.lista_destinos)):
                
                if i!=j:
                    destino_1 = self.lista_destinos[str(i)]
                    destino_2 = self.lista_destinos[str(j)]
                    distancia = self.pegar_distancia(destino_1, destino_2)
                    
                else:
                    distancia = 0
    
                lista_distancias[i,j] = distancia
             
        #Fechar conexão com a página
        driver.quit() 
        for valor in lista_distancias:
            print(valor, lista_distancias[valor])
            
        #Retornar lista de distâncias
        return lista_distancias
    


