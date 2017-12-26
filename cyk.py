def cyk():
	j = 0
	n = 5
	while j < n:
		for x in range(8):
			if f[x][1] == word[j]:
				l[0][j] += f[x][0]  # Vi1 = {A | A -> a是G中的产生式, a是x的第i个符号}
		j += 1
	j = 1
	while j < n:
		i = 0
		while i < n - j + 1:
			l[j][i] = ''  # Vij = 空
			k = 0
			while k < j - 1:
				x = 0
				while x < 8:
					if (f[x][1] in l[k][i]) and (f[x][2] in l[j-k][i+k]):
						l[j][i] += f[x][0]  # Vij = Vij并上{A | A -> BC是G中的产生式, 且B属于Vik, C属于Vi+k,j-k}
					x += 1
				k += 1
			i += 1
		j += 1
	if 'S' in l[4][0]:
		print('Success')
	else:
		print('Success')


print('Input the character:')
word = input()
# Vij表
l = [['', '', '', '', ''], ['', '', '', '', ''], ['', '', '', '', ''], ['', '', '', '', ''], ['', '', '', '', '']]
# 产生式
f = [['', '', ''], ['', '', ''], ['', '', ''], ['', '', ''], ['', '', ''], ['', '', ''], ['', '', ''], ['', '', '']]
for a in range(8):
	print('Input the rule:')
	f[a] = input()
cyk()
