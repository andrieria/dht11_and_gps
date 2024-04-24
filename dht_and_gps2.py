import serial
import csv
import matplotlib.pyplot as plt 
import pandas as pd
import json
from mpl_toolkits.basemap import Basemap
import matplotlib.gridspec as gridspec
import streamlit as st


ser = serial.Serial('COM12', 9600) #abre porta serial

# Inicialize as listas para armazenar os dados
temperatura = []
umidade = []
latitude = []
longitude = []
altitude = []

def recebendo_dados():
    #while True:
    i = 0
    while i < 5:
    # Leia uma linha da porta serial
        linha = ser.readline().decode().strip()
        print(f"{linha}")

        # Verifique se a linha é um objeto JSON válido
        try:
            dados = json.loads(linha)
        except json.JSONDecodeError:
            continue
        
        if 'temperature' in dados and 'humidity' in dados: #and 'latitude' in dados and 'longitude' in dados and 'altitude' in dados
            print("Dentro do if")
            temperatura.append(dados['temperature'])
            umidade.append(dados['humidity'])
            latitude.append(-6.589452)
            longitude.append(-36.77206)
            altitude.append(252.6)
            '''latitude.append(dados['latitude'])
            
            
            longitude.append(dados['longitude'])
            altitude.append(dados['altitude'])'''
        i+=1

    # Verifique se o objeto JSON contém as chaves necessárias

    
    # Defina o nome do arquivo CSV
    nome_arquivo = 'dados_sensor.csv'
    # Abra o arquivo CSV em modo de escrita
    with open(nome_arquivo, mode='w', newline='') as arquivo_csv:
        # Crie o escritor CSV
        escritor_csv = csv.writer(arquivo_csv)

        # Escreva o cabeçalho do CSV
        escritor_csv.writerow(['Temperatura', 'Umidade', 'Latitude', 'Longitude', 'Altitude'])

        # Escreva os dados no CSV
        for temp, umid, lat, lon, alt in zip(temperatura, umidade, latitude, longitude, altitude):
            escritor_csv.writerow([temp, umid, lat, lon, alt])
    print("Dados salvos com sucesso no arquivo:", nome_arquivo)

def plot_world_map():
    #tenho que criar um while
    
    #fig = plt.figure(figsize=(12, 8))
    #gs = gridspec.GridSpec(2, 3, width_ratios=[2, 1, 1], height_ratios=[2, 1])
    
    plt.figure(figsize=(10, 5))
    
    # Plotar mapa mundi com os dados do GPS
    #ax1 = plt.subplot(gs[0, 0])
    #ax1.set_title('Localização')
    mapa = Basemap(projection='mill', llcrnrlat=-90, urcrnrlat=90, llcrnrlon=-180, urcrnrlon=180) #, ax=ax1)
    mapa.drawcoastlines()
    mapa.drawcountries()
    x, y = mapa(longitude, latitude)
    #mapa.plot(x, y, 'ro')
    plt.title('Localização')
    st.pyplot(x, y, 'ro')
    
    
    
    
    
    #plt.subplot(2, 1, 2)
    '''plt.subplot(3, 1, figsize=(8, 12)) 
    mapa = Basemap(projection='mill', llcrnrlat=-90, urcrnrlat=90, llcrnrlon=-180, urcrnrlon=180)
    mapa.drawcoastlines()
    mapa.drawcountries()
    x, y = mapa(longitude, latitude)
    mapa.plot(x, y, 'ro')'''

def plot_data():   
    plt.figure(figsize=(10, 5))
    plt.plot(temperatura, label='Temperatura')
    plt.title('Gráfico de Temperatura')
    plt.legend()
    st.pyplot()
    
    plt.figure(figsize=(10, 5))
    plt.plot(umidade, label='Umidade')
    plt.title('Gráfico de Umidade')
    plt.legend()
    st.pyplot()
    
    
    # Plotar gráfico de temperatura
    #ax2 = plt.subplot(gs[1, 0])
    #ax2.plot(range(10), range(10))
    #plt.subplot(2, 2, 1)
    '''plt.subplot(3, 2, figsize=(5, 10))
    plt.plot(temperatura)
    plt.title('Gráfico de Temperatura')
    plt.xlabel('Tempo (s)')
    plt.ylabel('Temperatura (°C)')
    plt.xlim(0, len(temperatura))
    plt.ylim(0,100)
    #plt.xticks(temperatura)
    #plt.yticks(temperatura, list(range(51)))'''

    # Plotar gráfico de umidade
    #ax3 = plt.subplot(gs[1 ,1])
    #ax3.plot(range(10), range(10))
    #plt.subplot(2, 2, 2)
    '''plt.subplot(3, 2, figsize=(5, 10))
    plt.plot(umidade)
    plt.title('Gráfico de Umidade')
    plt.xlabel('Amostras')
    plt.ylabel('Umidade (%)')
    plt.xlim(0, len(umidade))
    plt.ylim(0, 100)
    #plt.yticks(umidade, list(range(51)))'''


    #plt.tight_layout()  # Ajusta o layout para evitar sobreposição de subplots
    #plt.show()
st.title('Aplicativo de Visualização')
st.write('Aqui você pode visualizar o mapa-múndi juntamente com gráficos de temperatura e umidade.')

def main():
    # Botão para plotar o mapa-múndi
    if st.button('Plotar Mapa-Múndi'):
        plot_world_map()
    
    # Botão para plotar os gráficos de temperatura e umidade
    if st.button('Plotar Dados'):
        plot_data()
    '''recebendo_dados()
    dados_graficos()
    if len(temperatura) >= 10 and any(a > 0 for a in altitude) or any(a > 0 for a in latitude) or any(a > 0 for a in longitude):
        dados_graficos()
    else:
        print("Nenhum valor de altitude, longitude ou latitude é maior que zero")'''
    
if __name__ == "__main__":
    main()
    