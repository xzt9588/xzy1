#!/usr/bin/env python3
import sys
import csv
import configparser
import getopt
import datetime
import time
today = datetime.date.today()
#print(today)
now = time.strftime("%H:%M:%S")
#print(today,now)
cf = configparser.ConfigParser()
class Args(object):
	def __init__(self):
		try:
			l = sys.argv[1:]
			self.c = l[l.index('-c')+1]
			self.d = l[l.index('-d')+1]
			self.o = l[l.index('-o')+1]
		except ValueError:
			print("invalid input")

args = Args()
if sys.argv[1] == 'C':
	sha,city = getopt.getopt(sys.argv[1:],'-C')
else:
	city = ['DEFAULT']
#print(args.c)
#print('testchallenge.cfg')
#cf.read('testchallenge.cfg')
cf.read(args.c)
opts = cf.items(str.upper(city[0]))
#print(opts)
#print(opts[0][0])
class Config(object):
	def __init__(self):
		self.config = self._read_config()
	def _read_config(self):
#		try:
			config = {}
			i = 0
		#	with open(args.c) as f:
#			for i in opts:
			while i < len(opts):
				#print('opts[0]:',opts[i][0])
				#print('opts[1]:',opts[i][1])
				config[opts[i][0]] = float(opts[i][1])
				i += 1
			#print(config)
			return config	
#		except TypeError:
			print("invalid input")
config = Config()

class UserData(object):
	def __init__(self):
		with open(args.d) as f:
			data = list(csv.reader(f))
		self.u = data

userdata = UserData().u
class IncomeTaxCalculator(object):
	def __init__(self):
		self.income = self.calc_for_all_userdata()
	def calc_for_all_userdata(self):
		i = 0
		global bfinal
		global Shebao
		global Nrate
		global Tax
		l = userdata
		bfinal = []
		I = 2
		Nrate = 0
		while I < len(opts):
			Nrate += float(opts[I][1])
			I = I + 1
		#use b to save fina
		Shebao = []
		Tax = []
		while i < len(l):
		# calculate the amount need to pay shebao
			Total = int(l[i][1])
			shebao = 0
			if Total < config.config['jishul']:
				shebao = config.config['jishul'] * Nrate
			elif Total > config.config['jishuh']:
				shebao = config.config['jishuh'] * Nrate
			else:
				shebao = Total * Nrate
			try:
				wrate = Nrate
			#	while j < len(a):
			#tax1: amount need to pay tax
				Total = Total - shebao
				Shebao.append(shebao)
				if Total < 0:
					Total = 0
				tax1 = Total - 3500
				if tax1 <= 1500:
					rate = 0.03
					number = 0
				elif tax1 > 1500 and tax1 <= 4500:
					rate = 0.1
					number = 105
				elif tax1 > 4500 and tax1 <= 9000:
					rate = 0.2
					number = 555
				elif tax1 > 9000 and tax1 <=35000:
					rate = 0.25
					number = 1005
				elif tax1 > 35000 and tax1 <= 55000:
					rate = 0.3
					number = 2755
				elif tax1 > 55000 and tax1 <=80000:
					rate = 0.35
					number = 5505
				elif tax1 > 80000:
					rate = 0.45
					number = 13505
				if tax1 < 0:
					tax = 0
					ftotal = Total
					Tax.append(tax)
					bfinal.append(ftotal)
				else:
					tax = tax1 * rate - number
					ftotal = Total - tax
					bfinal.append(ftotal)
					Tax.append(tax)
				i = i + 1
			except ValueError:
				print("Parameter Error")
income = IncomeTaxCalculator()
filename = args.o
#print('date',datetime.today())
#print('userdata:',userdata)
#print('Shebao:',Shebao)
#print('Tax:',Tax)
#print('bfinal',bfinal)
with open(filename,'w') as file:
	k = 0
	while k < len(userdata):
		line = '{},{},{:.2f},{:.2f},{:.2f},{} {}'.format(userdata[k][0],userdata[k][1],Shebao[k],Tax[k],bfinal[k],today,now)
		file.write(line)
		file.write('\n')
		k = k + 1
	
	
#print(line)
#k = 0
#while k < len(userdata):
#	print('{},{},{:2f},{:2f},{:2f}'.format(userdata[k][0],userdata[k][1],Shebao[k],Tax[k],bfinal[k]))
#	k = k + 1
#print("this is test:")
#print(Shebao)
#print(Nrate)
#print(config.config['JiShuL'])

