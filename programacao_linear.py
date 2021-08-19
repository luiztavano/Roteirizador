#importação da biblioteca pulp
from pulp import LpProblem, LpStatus, lpSum, LpVariable, LpMinimize

class Metodo_exato(object):
    

    def __init__(self, lista_destinos, lista_distancias):
        self.lista_destinos = lista_destinos
        self.lista_distancias = lista_distancias
        
    #Função para retornar a sequencia de entregas pelo nome do cliente e endereço
    def decodificar(self,percurso, indice):
        #Definir variável para armazenar a sequencia de entregas
        lista = {}
        
        #Looping para transformar a saída do programa de rotas em um lista de
        #Sequencia de endereços
        for i in range(len(percurso)):
            valor = percurso[i].split("_")
            lista[valor[1]] = valor[2]
            
        n = 0
        i = "0"
        sequencia = []
        while n < len(self.lista_destinos):
            sequencia.append(i) 
            i = lista[i]
            n = n + 1
            
        #Criar uma lista de sequencia de entrega com o nome/endereço
        sequencia_final = []
        for i in sequencia:
            dados = self.lista_destinos[str(i)]
            sequencia_final.append(dados[indice])
           
        return sequencia_final
        
    def calcular(self):
        
        #Definir a quantidade e destinos
        n = len(self.lista_destinos)
        
        #Loop para preencher a distância das origens e destinos iguais
        for i in range(n):
            self.lista_distancias[i,i] = 100000
        
        #Chamar o modelo
        model = LpProblem(name="PCV", sense=LpMinimize)
        
        #Definição das variáveis
        x = LpVariable.dicts("x",(range(n), range(n)), cat="Binary")
        u = LpVariable.dicts("u",range(n),lowBound=0, upBound = n-1, cat="Integer")
        
        #Definição da Função objetivo
        obj_func = (lpSum(x[i][j] * self.lista_distancias[i,j] for i in range(n) for j in range(n)))
        model += obj_func
        
        #Restrição na horizontal
        for i in range(n):
            model += (lpSum(x[i][j] for j in range(n) if j!=i) == 1)
            
        #Restrição na vertical
        for j in range(n):
            model += (lpSum(x[i][j] for i in range(n) if i!=j) == 1)
        
        #Restrição para evitar sub-rotas
        for i in range(1,n):
            for j in range(1,n):
                if i!=j:
                    model += (u[i] - u[j] + x[i][j]*n <= n-1)
                    
                else:
                    model += (u[i] - u[i] == 0)
        
        # Executar modelo
        model.solve()
        
        #Ótimo da função
        otimo = model.objective.value()
        
        #Exibir apenas variavéis dos locais de entrega que são maiores que 0
        percurso = []
        for var in model.variables():
            
            if var.value() > 0:
                nome = var.name
                
                if nome[0] == "x":
                    percurso.append(var.name)
                    print(var.name)
                    

        #Chamar função para decodificar retornar a sequencia de entrege pelo
        #nome do cliente
        sequencia_final_nome = self.decodificar(percurso, "Cliente")
           
        #Chamar função para decodificar retornar a sequencia de entrege pelo
        #endereço do cliente
        sequencia_final_endereco = self.decodificar(percurso, "Endereço")
                    
        #Armazenar valores em um dicionário para o retorno          
        roteiro = {}
        roteiro["distancia"] = otimo 
        roteiro["sequencia"] = sequencia_final_nome
        roteiro["sequencia_endereco"] = sequencia_final_endereco
        
        #Retornar resultado
        return roteiro
    
