#Importação das bibliotecas
import streamlit as st
import pandas as pd
from main import calcular_rota

#Definição do cabeçalho
st.title("Gerador de Rotas")

#Campo para inserir as informações do ponto de saída
cliente = st.text_input('Local da partida')
endereco = st.text_input('Endereço')
cep = st.text_input('CEP')

#Criar dicionário e armazenar informações
dados = {}
dados["Cliente"] = cliente
dados["Endereço"] = endereco
dados["CEP"] = cep

#Exibir informações do ponto de saída na tela
st.session_state[str(0)] = dados
st.write("Partida: " + str(cliente))
st.write("Endereço: " + str(endereco))

#Inserir planilha contendo os endereços de entrega
input = st.file_uploader("Selecione um arquivo",type=['xlsx'])

#Verificar se foi inserido uma planilha de endereços
if input != "":
    
    #Tentar ler a planilha inserida
    try:
        df = pd.read_excel(input)
        
        #Armazenar informações da planilha na dicionário dados
        for i in range(len(df)):
            dados = {}
            dados["Cliente"] = df.iloc[i,0]
            dados["Endereço"] = df.iloc[i,1]
            dados["CEP"] = df.iloc[i,2]
            st.session_state[str(i+1)] = dados
            
    except:
        st.write("Nenhum arquivo inserido")    
    
    
#Exibir endereços de entrega passados
st.write("Lista de destinos")
for i in st.session_state:
    if int(i) > 0:
        dados = st.session_state[i]
        nome_cliente = dados["Cliente"]
        nome_rua = dados["Endereço"]
        numero_cep = dados["CEP"]
        st.write(str(i) + " - " + str(nome_cliente) + " - " + str(nome_rua) + " - "+ str(numero_cep))
        
#Botão para executar a roteirização
executar = st.button("Gerar rota")


#Ao clicar no botão executar, realizar a roteirização
if executar:    
    st.write("Calculando Rota...")
    
    #Chamar classe para calcular rota
    roteiro = calcular_rota(st.session_state)
    
    #Executar o cálculo das rotas pelos métodos exato e heurístico
    resultado_exato, resultados_heuristicos, tempo = roteiro.gerar_rota()
    
    st.write("Concluído!!\n")
        
    #Exibir resultado do método exato
    st.subheader("Melhor Rota Exata")

    #Looping para exibir a sequência das entregas
    for i in range(len(resultado_exato["sequencia"])):
        st.write(str(resultado_exato["sequencia"][i]) + " - " + str(resultado_exato["sequencia_endereco"][i]))
        
    #Exibir distância percorrida da rota
    st.write("Distancia percorrida: " + str(resultado_exato["distancia"]) + " km") 
    
    #Exibir resultado do método heurístico
    st.subheader("Melhor Rota Heurística")
    
    for j in resultados_heuristicos:
        resultado = resultados_heuristicos[j]
                
        st.write(str(resultado["nome"]))
        
        #Looping para exibir a sequência das entregas
        for i in range(len(resultado["sequencia"])):
            st.write(str(resultado["sequencia"][i]) + " - " + str(resultado["sequencia_endereco"][i]))
        
        #Exibir distância percorrida da rota
        st.write("Distancia percorrida: " + str(resultado["distancia"]) + " km") 
    
    #Exibir tempo de execução
    st.write("Tempo de execução (s): " + str(tempo))

    



