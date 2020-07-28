
import pycurl 
import json
import requests
import os

API = "http://ip-api.com/json/"
banner = """

  _____ _____     _____        __                           _   _             
 |_   _|  __ \   |_   _|      / _|                         | | (_)            
   | | | |__) |    | |  _ __ | |_ ___  _ __ _ __ ___   __ _| |_ _  ___  _ __  
   | | |  ___/     | | | '_ \|  _/ _ \| '__| '_ ` _ \ / _` | __| |/ _ \| '_ \ 
  _| |_| |        _| |_| | | | || (_) | |  | | | | | | (_| | |_| | (_) | | | |
 |_____|_|       |_____|_| |_|_| \___/|_|  |_| |_| |_|\__,_|\__|_|\___/|_| |_|
                                                                              
                                                                                                            
create by: Daniel Sarmiento Dev 
creation date: 28-July-2020
"""

def GetIP(IP):
    print(banner)
    API_IP = API + IP
    response = requests.get(API_IP)
    response_json = json.loads(response.text)
    print("----------------------------------------")
    print("Información de la IP")
    print("----------------------------------------")
    try:
            print("Dirección IP:",response_json['query'])
            print("País de Origen:",response_json['country'])
            print("Código del País:",response_json['countryCode'])
            print("Nombre de la Región:",response_json['regionName'])
            print("Ciudad:",response_json['city'])
            print("Código zip:",response_json['zip'])
            print("Latitud:",response_json['lat'])
            print("Longitud:",response_json['lon'])
            print("Tiempo de Zona:",response_json['timezone'])
            print("Compañia:",response_json['isp'])
            print("Organización:",response_json['org'])
            print("AS:",response_json['as'])
            print("----------------------------------------")
    except:
            print("No se obtuvo información acerca de la IP.")
            print("----------------------------------------")


if __name__ == "__main__":
    try:
        os.system ("clear") 
        print(banner)
        IP = input('Inserte IP: ')
        if len(IP) <= 6:
          os.system("clear")
          print("----------------------------------------")
          print("Numero De IP Incorrecto.")
          print("----------------------------------------")
          exit()
        else:
          pass
        os.system ("clear")
        GetIP(IP)
    except ValueError:
     print("la IP no se ha encontrado.")


