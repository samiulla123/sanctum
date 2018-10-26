'''
Progran Name: client_info.py 

This script can be used to find the system details like
CPU information, RAM information, Disc information and Network information.

To run the code, only Python 3 and the dependencies 
(cpuinfo) are needed.

You can install all the dependencies with pip:
pip install py-cpuinfo

'''

##################################################################
#Module importing section

import platform as pf 
import sys
import socket
import os
import uuid
import re
import cpuinf


####################################################################################################
#decleration section
system_details={}

#####################################################################################################

def client_system_info():
    mac=':'.join(re.findall('..', '%012x' % uuid.getnode()))  #find the MAC address of the machine in hexadecimal form using regular expression
    system_details.update({'c_mac':mac})
    #print(system_details)
    ####################################################################################################


    is_64bits = sys.maxsize > 2**32 #finds if the system is 64 bit or not
    if is_64bits:
        bit_size='64 bit'
    else:
        bit_size='32 bit'

    system_details.update({'c_arch':bit_size})

    ######################################################################################################
    #print(system_details)
    op_sys=pf.system()
    #print(pf.platform())
    if op_sys=='Linux':
        #print(pf.linux_distribution())
        op_sys+="-"+pf.linux_distribution()[0]+"-"+pf.linux_distribution()[1]
        #print(op_sys)
    elif op_sys=='Windows':
        op_sys=pf.platform()
    else:
        op_sys=pf.platform()

    system_details.update({'c_plateform':op_sys})
    ###########################################################################################################
    #print(system_details)
    #print(pf.processor())
    cpu_name=cpuinfo.get_cpu_info()['brand'].split('CPU')[0]

    ########################################################################################################

    cpu_freq=cpuinfo.get_cpu_info()['brand'].split('CPU')[1].split('@')[1].lstrip()
    #print(cpu_freq)

    ############################################################################################################
    system_details.update({'c_cpu':cpu_name,'c_cpu_freq':cpu_freq})
    #print(system_details)

    #############################################################################################################
    system_details.update({'c_cpu_cores':os.cpu_count()})
    #print(system_details)
    
    ###############################################################################################################

    

    p = os.popen("df -h /")
    i = 0
    while 1:
        i = i +1
        line = p.readline()
        if i==2:
            disk=line.split()[1:5][0]
            break

    disk=int(disk[0:len(disk)-1])*1024
    system_details.update({'c_rom':disk})
    #print(system_details)

    ###################################################################################################################

    p = os.popen('free')
    i = 0
    while 1:
        i = i + 1
        line = p.readline()
        if i==2:
            ram=int(int(line.split()[1:4][0])/1024)
            break

    system_details.update({'c_ram':ram})
    return system_details

    ########################################################################################################################


