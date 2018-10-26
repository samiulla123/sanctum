from net_info import get_ip
import requests

data=get_ip()
requests.post(url='http://127.0.0.1:8000/display/',data=data)
