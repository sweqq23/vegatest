#!/usr/bin/python3
# -*- coding: utf-8 -*-
import time
import datetime
import websocket
import sys


n = int(sys.argv[1])
m = int(sys.argv[2])
from websocket import create_connection
ws = create_connection ("ws://127.0.0.1/echo")
print ("Старт")
ts = time.time()
st = datetime.datetime.fromtimestamp(ts).strftime('%Y-%m-%d %H:%M:%S')
print (st)
for i in range (n):
	for j in range (m):
		ws.send("dddddddddddddddddddddddddddddddddd")
ts = time.time()
st = datetime.datetime.fromtimestamp(ts).strftime('%Y-%m-%d %H:%M:%S')
print (st)

ws.close()
