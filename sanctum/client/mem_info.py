import socket
import math
import subprocess
import platform
def memory_size():
	with open("/proc/meminfo", "r") as f:
		lines = f.readlines()
	mem_dict={}
	for line in lines:
		data=line.split(':')
		if data[0]=="MemTotal":
			mem_dict[data[0].strip()]=data[1].strip()
		if data[0]=="MemFree":
                        mem_dict[data[0].strip()]=data[1].strip()
		if data[0]=="MemAvailable":
                        mem_dict[data[0].strip()]=data[1].strip()
		if data[0]=="Active":
			mem_dict[data[0].strip()]=data[1].strip()
	return parse(mem_dict)
def convert_size(size_bytes):
   if size_bytes == 0:
       return "0B"
   size_name = ("B", "KB", "MB", "GB", "TB", "PB", "EB", "ZB", "YB")
   i = int(math.floor(math.log(size_bytes, 1024)))
   p = math.pow(1024, i)
   s = round(size_bytes / p, 2)
   return "%s %s" % (s, size_name[i])

def parse(S):
	parsing={}
	for k,v in S.items():
		parsing[k]=convert_size(int(v[0:-2])*1024)
	return parsing		

def get_attr(attr):
	return memory_size()[attr]