import netifaces
import socket
import struct
import fcntl

def get_ip_address():
    ifname=netifaces.gateways()['default'][netifaces.AF_INET][1]
    ifname=ifname.encode()
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    return socket.inet_ntoa(fcntl.ioctl(
        s.fileno(),
        0x8915,  # SIOCGIFADDR
        struct.pack('256s', ifname[:15])
    )[20:24])


def get_logon_data():
    mac=netifaces.ifaddresses(netifaces.gateways()['default'][netifaces.AF_INET][1])[netifaces.AF_LINK][0]['addr']
    ip=get_ip_address()
    return {'c_inet':ip,'c_mac':mac}