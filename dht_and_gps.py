import serial
import csv
import matplotlib.pyplot as plt 
import pandas as pd
from mpl_toolkits.basemap import Basemap

ser = serial.Serial('COM12', 9600) #abre porta serial

# Inicialize as listas para armazenar os dados
temperatura = []
umidade = []
latitude = []
longitude = []
altitude = []

def recebendo_dados():
    while True:
    # Leia uma linha da porta serial
        linha = porta_serial.readline().decode().strip()

        # Verifique se a linha é um objeto JSON válido
        try:
            dados = json.loads(linha)
        except json.JSONDecodeError:
            continue

    # Verifique se o objeto JSON contém as chaves necessárias
    if 'temperature' in dados and 'humidity' in dados and 'latitude' in dados and 'longitude' in dados and 'altitude' in dados:
        temperatura.append(dados['temperature'])
        umidade.append(dados['humidity'])
        latitude.append(dados['latitude'])
        longitude.append(dados['longitude'])
        altitude.append(dados['altitude'])

def dados_graficos():
#tenho que criar um while


    '''
    i = 0
    while True:
        try:
            dados = str(ser.readline().decode("utf-8"))
            print(f"Dados do primeiro try {dados}")
        
        except UnicodeDecodeError:
            try:
                dados = ser.readline().decode("iso-8859-1")
                print(f"Dados do segundo try {dados}")
            except UnicodeDecodeError:
                print("Não foi possível decodificar o texto")
        print(f"{dados}")
        sep = dados.split("|")
        
        if type(sep[i]) == 'int':
            dado = sep[i]
            print(f"Testando aqui: {dado}")
            #temperatura = float(sep[1])
            #humidade = float(sep[2])
        
        i = 0
        while i < 2000:    
            dados = str(ser.readline().decode("utf-8"))
            print(f"Dado: {dados}")
            sep = dados.split("|")
            print(f"Sep: {sep[i]}")
        
        if type(sep[i]) == 'str':
                continue
            else:
        #temperatura = float(sep[1])
        #humidade = float(sep[2])
        i+=1   
            
        #return (f"Temperatura: {temperatura} and Humidade: {humidade}")
'''


'''def dados_grafico_gps():
    pass'''


def main():
    if len(temperatura) >= 10 and any(a > 0 for a in altitude) or any(a > 0 for a in latitude) or any(a > 0 for a in longitude):
        dados_grafico_dht()
    else:
        print("Nenhum valor de altitude, longitude ou latitude é maior que zero")
    
if __name__ == "__main__":
    main()
    