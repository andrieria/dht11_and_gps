import serial
import csv
import matplotlib.pyplot as plt 
import pandas as pd
import json
from mpl_toolkits.basemap import Basemap
import matplotlib.gridspec as gridspec
import reverse_geocoder as rg
from geopy.geocoders import Nominatim


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

def dados_graficos():
    #tenho que criar um while

    
    plot1 = plt.subplot2grid((4, 4), (0, 0), rowspan=3, colspan=4) 
    plot2 = plt.subplot2grid((4, 4), (3, 0), colspan=2) 
    plot3 = plt.subplot2grid((4, 4), (3, 2), colspan=2)  
    
    plot1.set_title('Localização')
    mapa = Basemap(projection='mill', llcrnrlat=-90, urcrnrlat=90, llcrnrlon=-180, urcrnrlon=180, resolution='c', ax=plot1)
    #mapa.drawmapboundary(fill_color='aqua')
    #mapa.fillcontinents(color='coral',lake_color='aqua')
    mapa.bluemarble()
    mapa.drawcoastlines()
    mapa.drawcountries()
    x, y = mapa(longitude, latitude)
    mapa.plot(x, y, 'ro')
    
    
    
    plot2.plot(range(5), temperatura)
    plot2.set_xlabel('Tempo (s)')
    plot2.set_ylim(0, 100)  # Definindo o limite do eixo y
    plot2.set_ylabel('Temperatura em °C') # Adicionando rótulo ao eixo y
    
    
    plot3.plot(range(5), umidade)
    plot3.set_xlabel('Tempo em (s)')
    plot3.set_ylim(0, 100)  # Definindo o limite do eixo y
    plot3.set_ylabel('Umidade em %')  # Adicionando rótulo ao eixo y
    
    '''
    # Converter as coordenadas em uma tupla
    coordenadas = (latitude[0], longitude[0])
    # Usar a função search para obter os detalhes da localização
    result = rg.search(coordenadas)
    # Extrair os detalhes relevantes
    cidade = result[0]['name']
    estado = result[0]['admin1']
    pais = result[0]['cc']
    
    localizacao = ["Cidade: " + cidade + "\n Estado:" + estado + "\n País: " + pais]
    
    plot1.text(0.5, 0.5, 'Texto de exemplo', ha='center', va='center', fontsize=12)

    
    #return cidade, estado, país'''
    geolocator = Nominatim(user_agent="geoapiExercises")
    location = geolocator.reverse((latitude[0], longitude[0]), language='pt-BR')
    #location = geolocator.reverse((latitude[1], longitude[1]), exactly_one=True)
    
    address = location.raw['address']
    continente = address.get('continent', 'Failed')
    pais = address.get('country', 'Failed')
    estado = address.get('state', 'Failed')
    cidade = address.get('city', 'Failed')
    rua = address.get('road', 'Failed')
    bairro = address.get('neighbourhood', 'Failed')
    regiao = address.get('region', 'Failed')
    
    
    localizacao = "Continente: " + continente + "\n País: " + pais + "\n" + regiao + "\n Estado: " + estado + "\n Cidade: " + cidade + "\n Bairro: " + bairro + "\n Rua: " + rua
    #localizacao1 = "Continente: " + continente + "\n País: " + pais + "\n" + regiao + "\n Estado: " + estado 
    #localizacao2 = "\n Cidade: " + cidade + "\n Bairro: " + bairro + "\n Rua: " + rua
    #localizacao3 = localizacao1 + localizacao2
    #plot1.text(2, 2, localizacao, ha='right', va='center', fontsize=12)
    plot1.text(4, 0.5, localizacao, ha='right', va='center', fontsize=12)
    

    plt.tight_layout()  # Ajusta o layout para evitar sobreposição de subplots
    plt.show()


def main():
    recebendo_dados()
    dados_graficos()
    if len(temperatura) >= 10 and any(a > 0 for a in altitude) or any(a > 0 for a in latitude) or any(a > 0 for a in longitude):
        dados_graficos()
    else:
        print("Nenhum valor de altitude, longitude ou latitude é maior que zero")
    
if __name__ == "__main__":
    main()
    