#!/usr/bin/env python3
import sys
import csv
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
class Config(object):
	def __init__(self):
		self.config = self._read_config()
	def _read_config(self):
		try:
			config = {}
			with open(args.c) as f:
				for i in f.readlines():
					l = i.split('=')
					config[l[0].strip()] = float(l[1].strip())
			return config
	#	
	#		file1 = open(args.c)
	#		l = file1.readlines()
	#		i = 0
	#		ll = []
	#		while i < len(l):
	#			ll.append(l[i].split('='))
	#			ll[i][0] = ll[i][0].strip(' ')
	#			ll[i][1] = ll[i][1].strip(' ')
	#			ll[i][0] = ll[i][0].strip('\n')
	#			ll[i][1] = ll[i][1].strip('\n')
	#			config[ll[i][0]] = ll[i][1]
	#			i = i + 1
	#		file1.close()
	#	
		except TypeError:
			print("invalid input")
config = Config()
class UserData(object):
	try:
		def __init__(self):
			self.userdata = self._read_users_data()
		def _read_users_data(self):
			userdata = []
			file1 = open(args.d)
			i = 0
			ID = []
			Salary = []
			ll = []
			l = file1.readlines()
			while i < len(l):
				ll.append(l[i].split(','))
				ll[i][0] = ll[i][0].strip('\n')
				ll[i][1] = ll[i][1].strip('\n')
				ID = ll[i][0]
				salary = ll[i][1]
				userdata.append((ID,salary))
				i = i + 1
			file1.close()
			return userdata
	except ValueError:
		print("invalid value")
userdata = UserData()
print(userdata.userdata)

class IncomeTaxCalculator(object):
	def __init__(self):
		self.income = self.calc_for_all_userdata()
	def calc_for_all_userdata(self):
		i = 0
		global bfinal
		global Shebao
		global Nrate
		global Tax
		l = userdata.userdata
		bfinal = []
		Nrate = config.config['YangLao'] + config.config['YiLiao'] + config.config['ShiYe'] + config.config['GongShang'] + config.config['ShengYu'] + config.config['GongJiJin']
		#use b to save final
		Shebao = []
		Tax = []
		while i < len(l):
		# calculate the amount need to pay shebao
			Total = int(l[i][1])
			shebao = 0
			if Total < config.config['JiShuL']:
				shebao = config.config['JiShuL'] * Nrate
			elif Total > config.config['JiShuH']:
				shebao = config.config['JiShuH'] * Nrate
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
				else:
					tax = tax1 * rate - number
					ftotal = Total - tax
					Tax.append(tax)
				bfinal.append(ftotal)
				i = i + 1
		#		k = 0
		#		while k < len(l):
		#		d = l[k][0]
		#		c = bfinal[k]
		#		print("{}:{:6.2f}".format(d,c))
		#		print(i)
			#	k = k + 1
			except ValueError:
				print("Parameter Error")
		print(bfinal)
	def export(self,default = 'csv'):
		result = self/calc_for_all_userdata()
		with open(IncomeTaxCalculator.index('-o')) as f:
			writer = csv.writer(f)
			writer.writerows(result)
income = IncomeTaxCalculator()
k = 0
#print(userdata.userdata)
#print(Shebao)
#print(Tax)
#print(bfinal)
filename = args.o
with open(filename,'w') as file:
	k = 0
	while k < len(userdata.userdata):
		line = '{},{},{},{},{}'.format(userdata.userdata[k][0],userdata.userdata[k][1],Shebao[k],Tax[k],bfinal[k])
		file.write(line)
		k = k + 1
	
	
print(line)
while k < len(userdata.userdata):
	print('{},{},{},{},{}'.format(userdata.userdata[k][0],userdata.userdata[k][1],Shebao[k],Tax[k],bfinal[k]))
#	print(config.config)
	k = k + 1
'''
print("this is test:")
print(Shebao)
print(Nrate)

if __name__ == '__main__':
	print('finish')
print(config.config['JiShuL'])
'''
