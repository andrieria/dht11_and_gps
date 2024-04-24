import matplotlib.pyplot as plt
import matplotlib.gridspec as gridspec


#fig, (ax1, ax2) = plt.subplots(2)
#import matplotlib.pyplot as plt

# Criando a figura e os subplots com layout personalizado
#fig, (ax1, ax2, ax3) = plt.subplots(3, gridspec_kw={'height_ratios': [2, 1, 1]})

# Criando a figura e subplots com layout personalizado usando GridSpec
fig = plt.figure(figsize=(8, 6))  # Definindo o tamanho da figura
gs = gridspec.GridSpec(2, 2, width_ratios=[4, 1], height_ratios=[3, 1])  # Proporções de largura e altura


# Adicionando os subplots
ax1 = fig.add_subplot(gs[0, 0])  # Subplot maior
ax2 = fig.add_subplot(gs[0, 1])  # Subplot menor direito
ax3 = fig.add_subplot(gs[1, 0])  # Subplot menor inferior


'''# Plotagem nos subplots
ax1.plot(x1, y1)  # Plotagem no ax1
ax2.plot(x2, y2)  # Plotagem no ax2
ax3.plot(x3, y3)  # Plotagem no ax3'''

# Ajustando rótulos e títulos
ax1.set_title('Gráfico 1')  # Título do ax1
ax1.set_xlabel('Eixo X')    # Rótulo do eixo x para o ax1
ax1.set_ylabel('Eixo Y')    # Rótulo do eixo y para o ax1

ax2.set_title('Gráfico 2')  # Título do ax2
ax2.set_xlabel('Eixo X')    # Rótulo do eixo x para o ax2
ax2.set_ylabel('Eixo Y')    # Rótulo do eixo y para o ax2

ax3.set_title('Gráfico 3')  # Título do ax3
ax3.set_xlabel('Eixo X')    # Rótulo do eixo x para o ax3
ax3.set_ylabel('Eixo Y')    # Rótulo do eixo y para o ax3


ax1.set_xlim([0,35])   #faixa do eixo horizontal

ax1.set_ylim([0,35]) # faixa do eixo vertical  
    
    

ax2.set_xlim([0,35])  

ax2.set_ylim([0,100])

ax3.set_xlim([0,35])  

ax3.set_ylim([0,100])
    
#leitura.append(random.randint(0,1023))  #teste com numeros aleatorios
leitura_temperatura = [0, 5, 10, 15]
leitura_humidade = [8, 16, 24, 32]

   
ax1.plot(leitura_temperatura)
ax2.plot(leitura_humidade)
ax3.plot(leitura_temperatura)

plt.tight_layout()  # Ajusta automaticamente o espaçamento entre subplots
plt.show()


'''import streamlit as st
import matplotlib.pyplot as plt
from mpl_toolkits.basemap import Basemap

# Função para plotar o mapa-múndi
def plot_world_map():
    plt.figure(figsize=(10, 5))
    mapa = Basemap(projection='mill', llcrnrlat=-90, urcrnrlat=90, llcrnrlon=-180, urcrnrlon=180)
    mapa.drawcoastlines()
    mapa.drawcountries()
    plt.title('Mapa-Múndi')
    st.pyplot()

# Função para plotar gráficos de temperatura e umidade
def plot_data():
    # Aqui você deve colocar a lógica para plotar os gráficos de temperatura e umidade
    # Substitua as linhas abaixo pelo código real
    plt.figure(figsize=(10, 5))
    plt.plot(range(10), range(10), label='Temperatura')
    plt.title('Gráfico de Temperatura')
    plt.legend()
    st.pyplot()

    plt.figure(figsize=(10, 5))
    plt.plot(range(10), range(10), label='Umidade')
    plt.title('Gráfico de Umidade')
    plt.legend()
    st.pyplot()

# Interface do Streamlit
st.title('Aplicativo de Visualização')
st.write('Aqui você pode visualizar o mapa-múndi juntamente com gráficos de temperatura e umidade.')

# Botão para plotar o mapa-múndi
if st.button('Plotar Mapa-Múndi'):
    plot_world_map()

# Botão para plotar os gráficos de temperatura e umidade
if st.button('Plotar Dados'):
    plot_data()
'''




'''import matplotlib.pyplot as plt

# Dados de exemplo
x = [1, 2, 3, 4, 5]
y = [2, 4, 6, 8, 10]

# Plot dos dados
plt.plot(x, y)
plt.xlabel('Eixo X')
plt.ylabel('Eixo Y')

# Definindo os marcadores dos eixos X e Y
novo_valores_x = ['A', 'B', 'C', 'D', 'E']
novo_valores_y = ['um', 'dois', 'três', 'quatro', 'cinco']
plt.xticks(x, novo_valores_x)
plt.yticks(y, novo_valores_y)

plt.show()'''



'''import matplotlib.pyplot as plt
from mpl_toolkits.basemap import Basemap
import matplotlib.gridspec as gridspec

# Dados de exemplo
longitude = [0, 45, -30, 60]
latitude = [30, 60, -20, -10]

# Criando a figura e o layout dos subplots com gridspec
fig = plt.figure(figsize=(16, 8))
gs = gridspec.GridSpec(2, 3, width_ratios=[2, 1, 1], height_ratios=[2, 1])

# Adicionando o primeiro subplot (maior)
ax1 = plt.subplot(gs[0, 0])
ax1.set_title('Localização')
mapa = Basemap(projection='mill', llcrnrlat=-90, urcrnrlat=90, llcrnrlon=-180, urcrnrlon=180, ax=ax1)
mapa.drawcoastlines()
mapa.drawcountries()
x, y = mapa(longitude, latitude)
mapa.plot(x, y, 'ro')

# Adicionando os subplots menores
ax2 = plt.subplot(gs[1, 0])
ax2.plot(range(10), range(10))
ax3 = plt.subplot(gs[1, 1])
ax3.plot(range(10), range(10))

plt.tight_layout()
plt.show()'''
