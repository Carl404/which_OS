#!/bin/python3

import sys
import os
import subprocess
from so_array import os_array as os_array

def main():
    try:
        ip_objective = sys.argv[1]
        parse_data(ip_objective)
    except OSError:
        print("No ip objective") 


def parse_data(ip_objective):
    command_protocol = "ping -c 4 " + ip_objective + " | sed -n 2p | awk '{print $4 $5 $6 $7}'"

    ejecucion = subprocess.Popen(command_protocol, stdout=subprocess.PIPE, shell=True)
    (output, err) = ejecucion.communicate()
    ejecucion_status = ejecucion.wait()

    # Decode bytes to utf-8
    result = output.decode("utf-8")

    # Extract ttl and protocol values
    # 127.0.0.1:icmp_seq=1ttl=64time=0.023
    
    # Protocolo
    start = result.find(':') + 1
    end =  result.find('=')
    scrap_prot = result[start:end]

    if (scrap_prot == "icmp_seq") :
        scrap_prot = "ICMP"

    # TTL
    start = result.find('ttl=') + 4
    end =  result.find('time')
    scrap_ttl = result[start:end]

    query_dict (scrap_prot, scrap_ttl)



def query_dict( protocol, ttl):
    counter = 0
    result = []

    print ("Protocol: " + protocol)
    print ("Time to live: " + ttl)


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
            result.append(res_aux)

            print ("--------------------")
            print (" - SO: " + operative_system)
            print (" - TTL: " + ttl_array)
            print (" - PROTOCOL: " + protocol_array)
            print (" - VERSION: " + version_array)
            print ("--------------------")
            counter = counter + 1

if __name__ == '__main__':
    main() 