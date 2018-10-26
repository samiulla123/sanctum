#! /usr/bin/python3.5

import time
import datetime
print('running every minute....i guess')
ts=time.time()
ts=datetime.datetime.fromtimestamp(ts).strftime('%Y-%m-%d %H:%M:%S')
print('stored on : ',ts)
