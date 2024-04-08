import serial
from mpl_toolkits.basemap import Basemap
import matplotlib.pyplot as plt

# Conectar ao módulo GPS
serial_port = serial.Serial('/dev/ttyACM0', 115200, timeout=1)

# Inicializar o mapa
plt.figure(figsize=(10, 8))
m = Basemap(projection='mill',llcrnrlat=-90,urcrnrlat=90,\
            llcrnrlon=-180,urcrnrlon=180,resolution='c')

m.drawcoastlines()
m.drawcountries()
m.drawmapboundary(fill_color='aqua')
m.fillcontinents(color='coral',lake_color='aqua')

plt.title("Dashboard do Módulo GPS")

# Loop para receber e plotar os dados
while True:
    line = serial_port.readline().decode("iso-8859-1")#'utf-8') #.strip()
    if line.startswith('$GPRMC'): # exemplo de leitura de uma sentença NMEA específica
        parts = line.split(',')
        if len(parts) >= 4:
            print(f"A parte 3: {parts[3]} \n\n")
            lat = float(parts[3]) / 100
            print(f"Lat: {lat} \n \n")
            
            print(f"A parte 5: {parts[3]} \n \n")
            lon = float(parts[5]) / 100
            print(f"Lon: {lon}")
            if parts[4] == 'S':
                lat *= -1
            if parts[6] == 'W':
                lon *= -1
            x, y = m(lon, lat)
            m.plot(x, y, 'bo', markersize=5) # plotar ponto
            plt.draw()
            plt.pause(0.01)

plt.show()