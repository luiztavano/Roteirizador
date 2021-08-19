from programacao_linear import Metodo_exato
from web_scraping import web_scraping
from heuristica import Metodo_das_economias
from time import time

class calcular_rota(object):
    
    
    def __init__(self, lista_destinos):
        self.lista_destinos = lista_destinos

    def gerar_rota(self):
        #Início da cronometragem
        inicio = time()
        
        print("Obtendo distâncias...")
        
        #Pegar distancias
        ws = web_scraping(self.lista_destinos)
        lista_distancias = ws.distancia_entre_destinos()
        
        print("Calculando a melhor rota...")
        
        #Roteirizar pelo método exato
        rota = Metodo_exato(self.lista_destinos, lista_distancias)
        resultado_exato =  rota.calcular()
        
        #Roteirizar pelo método heurístico
        rota = Metodo_das_economias(self.lista_destinos, lista_distancias)
        resultado_heuristico =  rota.calcular()
        
        #Para cronometro
        fim = time()
        
        #Armazenar tempo de processamento
        tempo = fim - inicio
        
        print("Concluído!!\n")
        
        #Exibir resultado
        print("---Melhor Rota---\n")
    
        #retornar rotas e tempo
        return resultado_exato, resultado_heuristico, tempo
