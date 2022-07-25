import re

lista = ["32 + 698", "3801 - 2", "45 + 43", "123 + 49"]

def arithmetic_arranger(lista, a = 0):
	c = re.findall('([0-9.]+)', lista[0])
	d = re.findall('([0-9.]+)', lista[1])
	e = re.findall('([0-9.]+)', lista[2])
	f = re.findall('([0-9.]+)', lista[3])		
	string1 = '   {}     {}      {}      {}'.format(c[0], d[0], e[0], f[0])
	print(string1)

	string2 = '+ {}    +   {}    + {}    +  {}'.format(c[1], d[1], e[1], f[1])
	print(string2)

	string3 = '-----    -----    ----    -----'
	print(string3)

	if a == True:
		
		g = int(c[0])
		h = int(c[1])
		i = int(d[0])
		j = int(d[1])
		k = int(e[0])
		l = int(e[1])
		m = int(f[0])
		n = int(f[1])
		
		string5 = '  {}     {}      {}      {}'.format(g + h, i - j, k + l, m + n) 
		print(string5)

arithmetic_arranger(lista, True)
