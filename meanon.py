#!/usr/bin/env python3

import subprocess
import time
import os

#Author - https://github.com/overlor14

def install(targ):
	if not 'socks5.txt' in os.listdir(path=os.getcwd()):
		print('\n[-] socks5.txt not found.')
		return
	if targ == 'proxychains':
		subprocess.call('sudo apt install proxychains && proxychains4', shell=True)
		print('\n[+] Installation proxychains completed succesful.')
		time.sleep(1)
	elif targ == 'MHDDoS':
		subprocess.call('git clone https://github.com/MHProDev/MHDDoS', shell=True)
		print('\n[+] Installation MHDDoS completed succesful.')
		time.sleep(1)
	elif targ == 'TOR':
		print('\n[+] TOR Service download start...')
		time.sleep(1)
		subprocess.call('sudo apt install tor', shell=True)
		print('\n[+] Installation TOR completed succesful.')
		time.sleep(1)
	else:
		print('\n[-] Wrong variant.')
		time.sleep(1)
	


def add_proxies_from_socks5():
	if not 'socks5.txt' in os.listdir(path=os.getcwd()):
		print('\n[-] socks5.txt not found.')
		return
	print('\n[*] Reading socks5.txt...')
	time.sleep(1)
	with open('socks5.txt', 'r') as f:
		arr = [f'socks5 {a.replace(":"," ")}' for a in f.readlines()]
		f1 = open(r'/etc/proxychains4.conf', 'a')
		f2 = open('/etc/proxychains.conf', 'a')
		for i in arr:
			f1.write(i)
			f2.write(i)
		f1.close()
		f2.close()
	print('\n[+] Proxies added succesful!')
	time.sleep(1)


def add_proxy(*proxies):
	with open('/etc/proxychains4.conf', 'a') as f:
		f1 = open('/etc/proxychains.conf', 'a')
		for i in proxies:
			f.write(i+'\n')
			f1.write(i+'\n')
		f1.close()
	print(f'\n[+] {len(proxies)} proxies added sucsessful!')
	time.sleep(1)

def clear_proxychains():
	os.system('sudo cp proxychains.conf /etc/')
	os.system('sudo cp proxychains4.conf /etc/')
	print('\n[+] Proxychains cleaned succesful!')

def reload_proxies():
	print('\n[*] Clear config files.')
	time.sleep(1)
	clear_proxychains()
	print('\n[*] Rewrite new proxies.')
	time.sleep(1)
	add_proxies_from_socks5()
	

def main():
	completed = []
	#os.system('pkg update && upgrade')
	while __name__ == '__main__':
		print("""\nSelect tool:
1. Installer.
2. Edit proxychains.
3. TOR management.
q. Quit""")
		sel = input('>>> ')
		if sel == '1':
			print("""\n1. Proxychains.
2. TOR service
3. MHDDoS
4. <Back.""")
			c = input('>>> ')
			if c == '1':
				install('proxychains')
			elif c == '2':
				install('TOR')
			elif c == '3':
				install('MHDDoS')
			elif c == '4':
				continue
			else:
				print('\n[-] Wrong variant.')
				time.sleep(1)
			continue
		elif sel == '2':
			print("""\nChoice:
1. Add your own proxies.
2. Add new proxies from socks5.txt.
3. Delete all proxies from proxychains.
4. <Back.""")
			ch = input('>>> ')
			if ch == '1':
				print('\n[*] Enter proxies through a comma, like: [PROXY TYPE] [IP] [PORT],[PROXY TYPE] [IP] [PORT],...')
				n = input('>>> ').split(',')
				add_proxy(*n)
			elif ch == '2':
				print("""\n1. Delete current proxies and add new.
2. Add proxies to current proxies""")
				v = input('>>> ')
				if v == '1':
					reload_proxies()
				if v == '2':
					add_proxies_from_socks5()
			elif ch == '3':
				clear_proxychains()
			elif ch == '4':
				continue
			else:
				print('\n[-] Wrong variant.')
				time.sleep(1)
			continue
		elif sel == '3':
			print("""\nAction for TOR:
1. TOR start.
2. TOR stop.
3. <Back.""")
			chs = input('>>> ')
			if chs == '1':
				print('\n[+] Launch TOR.')
				time.sleep(1)
				subprocess.call('sudo service tor start', shell=True)
				subprocess.call('sudo service tor status', shell=True)
				print('\n[+] TOR start process complete succesfull!')
				time.sleep(1)
			elif chs == '2':
				print('\n[*] Stopping TOR.')
				time.sleep(1)
				subprocess.call('sudo service tor stop', shell=True)
				subprocess.call('sudo service tor status', shell=True)
				print('\n[+] Tor stopped succesful!')
				time.sleep(1)
			elif chs == '3':
				continue
			else:
				print('\n[-] Wrong variant.')
				time.sleep(1)
			continue
		elif sel == 'q':
			print('\n\t\t\tGoodbye!)')
			time.sleep(1)
			quit()
		else:
			print('\n[-] Wrong variant.')
			time.sleep(1)
			continue

main()
