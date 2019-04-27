# /lib/usr/python
# Handcrafted with Love
# Kirnath x ZeroByte.ID

import os
import requests
from bs4 import BeautifulSoup as kntl
from threading import Thread
from multiprocessing.pool import ThreadPool
from threading import Lock as LockPool
from threading import Thread
from json import loads as results
myThreads = 10
kecepatan = ThreadPool(myThreads)
myLock = LockPool()
print('MD5 Mass Decryptor')
print('lav13enrose')

class warna:
	HEADER = '\033[95m'
	OKBLUE = '\033[94m'
	GREEN = '\033[92m'
	WARNING = '\033[93m'
	FAIL = '\033[91m'
	ENDC = '\033[0m'
	BOLD = '\033[1m'
	UNDERLINE = '\033[4m'

def check(line):
	line = line.strip()
	email, password = line.split('|')
	url = 'http://www.sc0d3.net/check/Md5/check.php'
	datapost = {
		'ajax': '1',
		'do': 'check',
		'mailpass': email +'|'+ password,
		'delim': '|',
		'email': '0',
		'bank': '0',
		'card': '0',
		'info': '0'
		}
	request = requests.post(url, data=datapost)
	respon = results(request.text)
	msg = request.text
	start_pattern = "<font color=green>"
	stop_pattern = "<"
	start_index = msg.find(start_pattern) + len(start_pattern)
	stop_index = start_index + msg[start_index:].find(stop_pattern)
	md5nya = msg[start_index:stop_index]
	print 
	if respon['error'] == 0:
		print(warna.GREEN + '[MD5 FOUND] ' + warna.ENDC + email +'|'+ warna.GREEN + md5nya )
		open(saveas+'.txt', 'a').write(email +'|'+ md5nya + '\n')
	if respon['error'] == 2:
		print(warna.FAIL + '[DIE] ' + warna.ENDC + email +'|'+ password)
		
bacot = str(input('Masukkan Mailist :'))
saveas = str(input('Save As (only Put string, dont put .txt again): '))
mailist = open(bacot, 'r').readlines()
buka = [line.replace('\n', '') for line in mailist]
kecepatan.map(check, buka)
kecepatan.close()
kecepatan.join()