import requests
import netifaces
import socket
import fcntl
import struct
import client_info

REGISTRATION_URL='http://127.0.0.1:8000/display/clients/'
CLIENTINFO_URL='http://127.0.0.1:8000/display/clientinfo/'

def get_ip_address():
    ifname=netifaces.gateways()['default'][netifaces.AF_INET][1]
    ifname=ifname.encode()
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    return socket.inet_ntoa(fcntl.ioctl(
        s.fileno(),
        0x8915,  # SIOCGIFADDR
        struct.pack('256s', ifname[:15])
    )[20:24])



def get_login_data():
    ip=get_ip_address()
    mac=netifaces.ifaddresses(netifaces.gateways()['default'][netifaces.AF_INET][1])[netifaces.AF_LINK][0]['addr']
    name=socket.gethostname()
    return {'c_inet':ip,'c_mac':mac,'c_name':name}

def create_account():
    import ast
    data=get_login_data()
    result=requests.post(url=REGISTRATION_URL,data=data)
    if result.ok:
        print('result:',result.content)
        cid=ast.literal_eval(result.content.decode())['id']
        with open('key.cli','w+')as handle:
            handle.write(str(cid))

        print('registration successfull')
        print('sending basic info')
        dat=client_info.client_system_info()
        dat.update({'c_id':cid})
        result=requests.post(url=CLIENTINFO_URL,data=dat)
        print('data sent successfully',dat,result)
    else:
        print('registration failed')
