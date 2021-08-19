
class Metodo_das_economias(object):
    
    
    def __init__(self, lista_destinos, lista_distancias):
        self.lista_destinos = lista_destinos
        self.lista_distancias = lista_distancias    
        
    def decodificar(self,percurso, valor):
        
        print(percurso)
        sequencia_final = []
        for i in percurso:
            dados = self.lista_destinos[str(i)]
            sequencia_final.append(dados[valor])

        return sequencia_final
           
    def calcular(self):
        
        #Definir a quantidade e destinos
        n = len(self.lista_destinos)
                
        #Loop para preencher a distância das origens e destinos iguais
        for i in range(len(self.lista_distancias)):
            self.lista_distancias[i,i] = 100000
            
        #Calcular economias
        lista_economias = []
        
        for i in range(1,n):
            for j in range(1, n):
                if i!= j:
                    s = self.lista_distancias[i,0] + self.lista_distancias[0,j] - self.lista_distancias[i,j]
                    economia = [i,j,s]
                    lista_economias.append(economia)
                            
        # ordenar a lista de economias pelo maior valor da função objetivo
        lista_economias_ordenada = sorted(lista_economias, key=lambda tup: tup[2], reverse=True)
        
        #Criar variáveis para armazenar as rotas e distancias geradas
        lista_rotas = []
        distancias_roteiro = []
        par = lista_economias_ordenada[0]
        
        #Loop para percorrer toda a lista de economias
        for k in range(len(lista_economias_ordenada)):
            
            print("----Iteração: ", k)
            par = lista_economias_ordenada[k]
                        
            #Pegar roteiros
            i = ""
            j = ""
            
            for a in range(len(lista_rotas)):
                
                if par[0] in lista_rotas[a]:
                    i = a
                if par[1] in lista_rotas[a]:
                    j = a
            
            #Se i e j não estão em nenhum roteiro
            if (i == "") and (j == ""):
                
                #Adicionar rota dos pontos
                rota = [par[0], par[1]]
                lista_rotas.append(rota)
                distancia = self.lista_distancias[par[0], par[1]]
                distancias_roteiro.append(distancia)
                
                print ("Pontos", par[0], par[1])
                print ("Distancia dos pontos", distancia )
                print("Adicionar rota dos pontos")
                print("Roteiros", lista_rotas)
                print("Distancia percorrida das rotas", distancias_roteiro)

            #Senão (i, ou j, ou ambos estão em algum roteiro)
            else:
                
                #Se somente um nó, ou i, ou j,está em um roteiro
                if (i == "") or (j == ""):
                    
                    #Verificar se o nó i está no final de algum roteiro
                    if (i != ""):
                        
                        posicao = ""
                        for a in range(len(lista_rotas)):
                            if par[0] == lista_rotas[a][-1]:
                                posicao = a
                                
                        #Se tiver, adicionar o nó j ao final
                        if posicao != "":      
                            
                            lista_rotas[posicao].append(par[1])
                            distancia = self.lista_distancias[par[0], par[1]]
                            distancias_roteiro[posicao] = distancias_roteiro[posicao] + distancia
        
                            print ("Pontos", par[0], par[1])
                            print ("Distancia dos pontos", distancia )
                            print("Adicionado ao final do roteiro o nó j")
                            print("Roteiros", lista_rotas)
                            print("Distancia percorrida das rotas", distancias_roteiro)
                    
                        else:
                            pass
                            # print("O nó i não encontra-se no final do roteiro")
                                    
                    #Verificar se o nó j está no começo de algum roteiro
                    if (j != ""):
                        
                        posicao = ""
                        for a in range(len(lista_rotas)):
                            if par[1] == lista_rotas[a][0]:
                                posicao = a
                                
                         #Se tiver, adicionar o nó i ao começo      
                        if posicao != "":                    
                            lista_rotas[posicao].insert(0,par[0])
                            distancia = self.lista_distancias[par[0], par[1]]
                            distancias_roteiro[posicao] = distancias_roteiro[posicao] + distancia
                            
                            print ("Pontos", par[0], par[1])
                            print ("Distancia dos pontos", distancia )
                            print("Adicionado ao começo do roteiro o nó i")
                            print("Roteiros", lista_rotas)
                            print("Distancia percorrida das rotas", distancias_roteiro)
                            
                        else:
                            pass
                            # print("O nó j não encontra-se no começo do roteiro")
                    
                #Se i e j estão em roteiros diferentes
                elif i != j:
                    
                    #Se i e j são extremos de seus roteiros
                    if (par[0] == lista_rotas[i][-1]) and (par[1] == lista_rotas[j][0]):
                        
                        #Então: Une os dois roteiros
                        for m in lista_rotas[j]:
                            
                            lista_rotas[i].append(m)
                        distancias_roteiro[i] = distancias_roteiro[i] + distancias_roteiro[j]
                        
                        del lista_rotas[j]
                        del distancias_roteiro[j]
                        print ("Pontos", par[0], par[1])
                        print ("Distancia dos pontos", distancia )
                        print("Unir os roteiros dos i e j")
                        print("Roteiros", lista_rotas)
                        print("Distancia percorrida das rotas", distancias_roteiro)
                        
                    else:
                        pass
                         # print("Os nós i e j não estão nos extremos de seus roteiros")
                    
                else:
                    pass
                    # print ("Pontos pertencem ao mesmo roteiro")
          
        #Criar dicionário para armazenar roteiros gerados
        roteiros = {}
        
        #Loop para percorrer todos os roteiros gerados
        for i in range(len(lista_rotas)):
            
            #Pegar a distancia do ponto de saída até a primeira entrega
            distancia_inicio = self.lista_distancias[0, lista_rotas[i][0]]
            print ("Distancia dos pontos do início", distancia_inicio )
            
            #Pegar a distância da última entrega até o ponto de partida
            distancia_final = self.lista_distancias[lista_rotas[i][-1], 0]
            print ("Distancia dos pontos do final", distancia_final )
            
            #Inserir o ponto de partida no roteiro
            lista_rotas[i].insert(0,0)
            
            #Adicionar distâncias do ponto de partida na distância total da rota
            distancias_roteiro[i] = distancias_roteiro[i] + distancia_inicio + distancia_final
            
            #Gerar roteiros por nome do cliente e endereço
            sequencia_final_nome = self.decodificar(lista_rotas[i], "Cliente")
            sequencia_final_endereco = self.decodificar(lista_rotas[i], "Endereço")

            #Exibir sequencia e distância
            print("Rota gerada ", lista_rotas[i])
            print("Distancia percorrida ", distancias_roteiro[i])
            
            #Inserir informações no dicionário roteiro
            roteiro = {}
            roteiro["status"] = "Otimo"
            roteiro["distancia"] = distancias_roteiro[0]
            roteiro["sequencia"] = sequencia_final_nome
            roteiro["sequencia_endereco"] = sequencia_final_endereco
            nome = "Rota " + str(i + 1)
            roteiro["nome"] = nome
            
            #Adicionar roteiro no dicionário roteiros
            roteiros[nome] = roteiro
        
        #Retornar resultado
        return roteiros

