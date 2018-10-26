import time
import datetime
import socket
def get_ip():
	net_dict={}
	hn=socket.gethostname()
	hip=socket.gethostbyname(hn)
	net_dict['Hostname']=hn
	net_dict['HostIpAddress']=hip
	ts=time.time()
	ts=datetime.datetime.fromtimestamp(ts).strftime('%Y-%m-%d %H:%M:%S')
	net_dict['time_stamp']=ts
	return net_dict

