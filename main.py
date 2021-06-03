j=[]
while(True):
	x=input()
	if x=="end":
		break

	j=j+[x]

x=""
t=[]
clear=[]



n=0
for n in range(len(j)):
	k=""
	mm=list(j[n])
	for h in range(len(mm)):
		if mm[h]!='"':
			k=k+mm[h]
		else:

			d=0

	clear=clear+[k]




for n in range(len(clear)):
	x = clear[n]
	y = x.split(',')


	z = y[0].split()

	n = 0
	sum = ""
	for n in range(len(z)):
		sum = sum + '*' + z[n]

	k = list(sum)
	n = 0
	sum1 = ""
	for n in range(1, len(k)):
		sum1 = sum1 + k[n]

	t = t + [sum1]


print(t)
print(len(t))









