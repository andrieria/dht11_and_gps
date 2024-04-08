import serial
import csv
import matplotlib.pyplot as plt 
import pandas as pd
from mpl_toolkits.basemap import Basemap

ser = serial.Serial('/dev/ttyACM0', 9600) #abre porta serial COM6 



def dados_grafico_dht():
#tenho que criar um while
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
        
        '''if type(sep[i]) == 'int':
            dado = sep[i]
            print(f"Testando aqui: {dado}")
            #temperatura = float(sep[1])
            #humidade = float(sep[2])
        '''
        '''i = 0
        while i < 2000:    
            dados = str(ser.readline().decode("utf-8"))
            print(f"Dado: {dados}")
            sep = dados.split("|")
            print(f"Sep: {sep[i]}")'''
        
        '''if type(sep[i]) == 'str':
                continue
            else:'''
        #temperatura = float(sep[1])
        #humidade = float(sep[2])
        i+=1   
            
        #return (f"Temperatura: {temperatura} and Humidade: {humidade}")


def dados_grafico_gps():
    pass


def main():
    dados_grafico_dht()
    
if __name__ == "__main__":
    main()
    