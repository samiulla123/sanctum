
'''
Progran Name: client_system_statistics.py 

This script can be used to find the current system status like
CPU status, RAM status, Disc Status and Network status.

The Script is dived into four function(methods) each returns data in the form of dictionary 

To run the code, only Python 3 and the dependencies 
(psutil and speedtest) are needed.

You can install all the dependencies with pip:
#1: pip install psutil
#2: pip install speedtest-cli




'''



####################################################################
#package import block


import os 
import speedtest
import psutil

#####################################################################
#defination of 4 dict 
cpu_stat={}
memory_stat={}
disc_stat={}
network_stat={}

nc=lambda x:x if x is not None else 0
######################################################################
#this method returns the CPU status in the form of dict
def system_cpu_stat():
    fq=psutil.cpu_freq()
    #print(fq)
    cpu_use=str(os.popen("top -n1 | awk '/Cpu\(s\):/ {print $2}'").readline().strip(\
        ))
    
    if not hasattr(psutil, "sensors_temperatures"):
        pass#cpu_use=0#sys.exit("platform not supported")
    temps = psutil.sensors_temperatures()
    if not temps:
        pass #cpu_use=0#sys.exit("can't read any temperature")
    for name, entries in temps.items():
        #print(type(cpu_stat),type(fq.current),type(fq.min),type(fq.max),type(entries[0].current),type(entries[0].high),type(entries[0].critical))
        cpu_stat.update({'cpu_usage':float(nc(cpu_use)),'cpu_curr_freq':int(nc(fq.current)),'cpu_min_freq':int(nc(fq.min)),'cpu_max_freq':int(nc(fq.max)),'cpu_curr_temp':float(nc(entries[0].current)),'cpu_high_temp':float(nc(entries[0].high)),'cpu_crit_temp':float(nc(entries[0].critical))})
        break
    return validate_cpu(cpu_stat)

############################################################################################
#this method finds and retuns the network stats in the form of dict
    
def system_network_stat():
    s = speedtest.Speedtest()
    s.get_servers()
    s.get_best_server()
    s.download()
    s.upload()
    res = s.results.dict()
    d,u,p= res["download"], res["upload"], res["ping"]
    network_stat.update({'n_up':int(nc(u/1024)),'n_down':int(nc(d/1024))})
    #print(network_stat)
    return validate_net(network_stat)

############################################################################################
#This method finds and returns RAM staus in the form of dict 
                                                                 
def system_ram_stat():
    p = os.popen('free')
    i = 0
    while 1:
        i = i + 1
        line = p.readline()
        if i==2:
            RAM_stats=line.split()[1:4]
            break
    memory_stat.update({'m_total':int(round(int(nc(RAM_stats[0])) / 1000,1)),'m_used':int(round(int(nc(RAM_stats[1])) / 1000,1)),'m_free':int(round(int(nc(RAM_stats[2])) / 1000,1))})
    return validate_mem(memory_stat)

##############################################################################################################################################
#this method finds and returns dick staus in the form of dict
                                      
def system_disk_stat():
    p = os.popen("df -h /")
    i = 0
    while 1:
        i = i +1
        line = p.readline()
        if i==2:
            DISK_stats = line.split()[1:5]
            break
               
    DISK_total = DISK_stats[0]
    DISK_free = DISK_stats[2]
        #print(DISK_free)
    DISK_perc = DISK_stats[3]
    DISK_total=int(DISK_total[0:len(DISK_total)-1])*1024
    DISK_free=int(DISK_free[0:len(DISK_free)-1])*1024
    DISK_used=(DISK_total-DISK_free)
    DISK_perc = int(DISK_perc[0:len(DISK_perc)-1])
        #print(DISK_perc)
    disc_stat.update({'d_total':int(nc(DISK_total)),'d_free':int(nc(DISK_free)),'d_used':int(nc(DISK_used)),'d_used_perc':int(nc(DISK_perc))})
    return validate_disk(disc_stat)


def validate_cpu(d):
    data=d
    ints=['cpu_curr_freq','cpu_min_freq','cpu_max_freq']
    dec=['cpu_usage','cpu_curr_temp','cpu_high_temp','cpu_crit_temp']
    for k,v in data.items():
        if k in ints:
            if type(v) is int:
               continue
            else:
                data[k]=0
    for k,v in data.items():
        if k in dec:
            if type(v) is float:
               continue
            else:
                data[k]=0.0
    return data      
                
def validate_mem(d):
    data=d
    ints=['m_total','m_used','m_free','m_active','m_inactive','m_shared','m_cached','m_buffers']
    for k,v in data.items():
        if k in ints:
            if type(v) is int:
               continue
            else:
                data[k]=0
    return data

def validate_disk(d):
    data=d
    ints=['d_total','d_used','d_free','d_used_perc']
    for k,v in data.items():
        if k in ints:
            if type(v) is int:
               continue
            else:
                data[k]=0
    return data

def validate_net(d):
    data=d
    ints=['n_up','n_down']
    for k,v in data.items():
        if k in ints:
            if type(v) is int:
               continue
            else:
                data[k]=0
    return data

