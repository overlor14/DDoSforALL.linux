#!/usr/bin/env python3
import subprocess
import time
import os

def install():
	if not 'socks5.txt' in os.listdir(path=os.getcwd()):
		print('\n[-] socks5.txt not found.')
		exit()
	subprocess.call('sudo apt-get install proxychains', shell=True)
	with open('socks5.txt', 'r') as f:
		arr = [f'socks5  {a.replace(":"," ")}' for a in f.readlines()]

	print('\n[+] Read proxies from socks5.txt')
	time.sleep(1)
	with open('socks5_.txt', 'a') as f:
		f1 = open(r'/etc/proxychains4.conf', 'a')
		for i in arr:
			f.write(i)
			f1.write(i)

	print('\n[+] TOR Service download start...')
	time.sleep(1)
	subprocess.call('sudo apt-get install tor', shell=True)

	print('\n[+] Launch TOR.')
	time.sleep(1)
	subprocess.call('sudo service tor start', shell=True)
	s = subprocess.check_output('sudo service tor status')
	time.sleep(1)
	s = bytes.decode(s,encoding='utf-8')
	if 'exited' in s:
		print('\n[+] TOR launch sucsessful!')
		time.sleep(1)
	else:
		print('\n[-] Something went wrong.')
		time.sleep(1)

def add_proxy(*proxies):
	with open('/etc/proxychains4.conf', 'a') as f:
		for i in proxies:
			f.write(i+'\n')
	print(f'\n[+] {len(proxies)} proxies added sucsessful!')
	time.sleep(1)

def main():
	while 1:
		print("""\nSelect tool:
1. Install proxychains(+add proxies from socks5.txt) and TOR service.
2. Add proxy to proxychains.
q. Quit""")
		sel = input('>>> ')
		if sel == '1':
			install()
		elif sel == '2':
			print('\nEnter proxies through a comma, like: [PROXY TYPE]  [IP] [PORT],[PROXY TYPE]  [IP] [PORT],...')
			n = input('>>> ').split(',')
			add_proxy(*n)
			continue
		elif sel == 'q':
			print('\n\t\t\tGoodbye!)')
			time.sleep(1)
			quit()
		else:
			print('\n[-] Wrong variant.')
			continue

main()
