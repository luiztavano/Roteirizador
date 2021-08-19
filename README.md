# Roteirizador
Esses scripts tem como objetivo realizar a roteirização dos endereços de entrega passados pelo usuário através de uma planilha (.xlsx).

### Funcionamento 
Seu funcionamento consiste inicialmente na extração das distâncias entre todas as cidades que são passadas pelo usuário utilizando-se para isso da biblioteca Selenium para realizar um "Web Scraping" no site google.com.br/maps/dir/. Em seguida, as informações são enviadas aos geradores de rota. 
Nesse sistema são utilizadas duas técnicas para obtenção das rotas de entrega, a primeira técnica se dá através de Programação Linear com a implementação do PCV (Problema do caixeiro viajante) para obtenção do Método Exato que consiste na melhor rota matematicamente possível, porém com um tempo de processamento grande. Já a segunda técnica se dá através da implementação do "Método das Economias" criada por Clarke e Wright em 1964 para obtenção do método heurístico que consiste na obtenção de um resultado bom, porém com um menor tempo de processamento.


### Requisitos
É necessário ter os seguintes requisitos instalados na máquina
1. Python 3.6 
2. Biblioteca pandas - pip install pandas
3. Biblioteca streamlit - pip install streamlit
4. Biblioteca pulp - pip install pulp
5. Biblioteca selenium - pip install selenium
6. Além disso, é necessário o download do ChromeDriver que pode ser encontrado [aqui](https://chromedriver.chromium.org/downloads)

### Modo de executação
1. Faça uma cópia dos arquivos em sua máquina e salve-os em uma pasta de sua preferencia;
2. Abra o prompt de comando na pasta aonde está salvo o arquivo
3. Instale as bibliotecas necessárias
4. Digite o seguinte comando e aparte enter - 'streamlit run roteirizador.py'
5. Será aberta uma nova guia no Chrome contendo a interface de interação com o usuário
6. Preencher as informações sobre o ponto de partida, apertando 'Enter' para validar os mesmos
7. Abra a planilha Endereços.xlsx, insira as informações sobre as entregas conforme abaixo, salve e feche
    - Nome do cliente
    - Endereço
    - CEP
9. Na interface do programa clique em "Gerar rota".
10. O programa irá retornar uma lista com a sequência de entrega dos Métodos Exato e Heurístico.


### Obs:
Para uma quantidade maior de 15 entregas não é interessante a utilização no Método Exato para obtenção da rota, devido o aumento fatorial do tempo de processamento.
