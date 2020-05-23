#!/bin/python3

import sys
import os
import subprocess
from so_array import os_array as os_array

def main():
    ip_objetivo = sys.argv[1]
    parse_data(ip_objetivo)
    
    #print("No ha introducido la ip/red objetivo") 


def parse_data(ip_objetivo):
    command_protocol = "ping -c 4 " + ip_objetivo + " | sed -n 2p | awk '{print $4 $5 $6 $7}'"


    ejecucion = subprocess.Popen(command_protocol, stdout=subprocess.PIPE, shell=True)
    (output, err) = ejecucion.communicate()
    ejecucion_status = ejecucion.wait()

    # Ejecución nos devuelve el resultado en bytes, por lo que lo paseamos a str
    resultado = output.decode("utf-8")

    # Extraemos los valores de ttl y protocolo
    # 127.0.0.1:icmp_seq=1ttl=64time=0.023
    
    # Protocolo
    inicio = resultado.find(':') + 1
    fin =  resultado.find('=')
    scrap_prot = resultado[inicio:fin]

    if (scrap_prot == "icmp_seq") :
        scrap_prot = "ICMP"

    # TTL
    inicio = resultado.find('ttl=') + 4
    fin =  resultado.find('time')
    scrap_ttl = resultado[inicio:fin]

    query_dict (scrap_prot, scrap_ttl)



def query_dict( protocol, ttl):
    contador = 0
    resultado = []

    print ("El protocolo es: " + protocol)
    print ("El ttl es: " + ttl)


    print ("--------------------")
    print ("|-PROBABLE SYSTEMS-|")
    print ("--------------------")
    
    for x in range(len(os_array)):
        operative_system = str(os_array[x][0])
        ttl_array = str(os_array[x][1])
        protocol_array = str (os_array[x][2])
        version_array = str (os_array[x][3])
        
        if (ttl_array == ttl and protocol_array == protocol):
            res_aux = [operative_system, ttl_array, protocol_array, version_array]
            resultado.append(res_aux)

            print ("--------------------")
            print (" - SO: " + operative_system)
            print (" - TTL: " + ttl_array)
            print (" - PROTOCOL: " + protocol_array)
            print (" - VERSION: " + version_array)
            print ("--------------------")
            contador = contador + 1

if __name__ == '__main__':
    main() 