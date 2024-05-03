import random

class Dealer:
	R=-1#send it to alice
	C=-1#send it to bob
	TRC=[[-1 for _ in range(4)] for _ in range(4)]
	MB=[[-1 for _ in range(4)] for _ in range(4)]
	MA=[[-1 for _ in range(4)] for _ in range(4)]


	def TRC(r,c):
		TT = [[-1 for _ in range(4)] for _ in range(4)]
		for a in range (0,4):
			for x in range (0,4):
				if((a*x)>=4):
					TT[a][x]=1
				else:
					TT[a][x]=0
		TT = [row[-c:] + row[:-c] for row in TT]		#shift cols with c
		TT = TT[-r:] + TT[:-r]							#shift rows with r
		return(TT)


	def MB():
		MB = [[-1 for _ in range(4)] for _ in range(4)]
		for i in range(0,4):
			for j in range(0,4):
				MB[i][j]=random.randint(0,1)
		return(MB)


	def MA(MB,TRC):
		MA = [[-1 for _ in range(4)] for _ in range(4)]
		for i in range(0,4):
			for j in range(0,4):
				MA[i][j]=(MB[i][j]+TRC[i][j]) %2
		return(MA)


	def Init():
		Dealer.R=(random.randint(0,3))#randA
		Dealer.C=(random.randint(0,3))#randB
		Dealer.TRC=Dealer.TRC(Dealer.R,Dealer.C)
		Dealer.MB=Dealer.MB()
		Dealer.MA=Dealer.MA(Dealer.MB,Dealer.TRC)

		print(f'R={Dealer.R}')#
		print(f'C={Dealer.C}')#

		print('TRC original')#
		for row in Dealer.TRC:#
			print(row)#

		print(f'MB')#
		for row in Dealer.MB:#
			print(row)#

		print(f'MA')#
		for row in Dealer.MA:#
			print(row)#

	def RandA():
		return(Dealer.R)

	def RandB():
		return(Dealer.C)

	def sendingToA():
		return(Dealer.MA)

	def sendingToB():
		return(Dealer.MB)
class Alice:
	Zb=-1
	v=-1
	u=-1
	x=-1
	r=-1#Dealer.RandA
	MA=[[-1 for _ in range(4)] for _ in range(4)]

	def Init(x:int,r:int):
		Alice.x=x			#her number
		Alice.r=r			#shift rows
		Alice.MA=Dealer.sendingToA()	#shifted the xor matrix

		print(f'x={Alice.x}')#

		print(f'R={Alice.r}')#

		print(f'MA')#
		for row in Alice.MA:#
			print(row)#

	def Send():
		Alice.u = ( Alice.x + Alice.r ) %4
		print(f'Alice sending u= {Alice.u}')
		return(Alice.u)

	def Receive(v:int,Zb:int):
		print(f'Alice received v and Zb')
		Alice.v=v
		Alice.Zb=Zb
		

	def Output():
		return((Alice.MA[Alice.u][Alice.v]+Alice.Zb)%2)


class Bob:
	Zb=-1
	v=-1
	y=-1
	c=-1#Dealer.RandB
	MB=[[-1 for _ in range(4)] for _ in range(4)]

	def Init(y,c):
		Bob.y=y
		Bob.c=c
		Bob.MB=Dealer.sendingToB()

		print(f'y={Bob.y}')#

		print(f'C={Bob.c}')#

		print(f'MB')#
		for row in Bob.MB:#
			print(row)#

	def Receive(u):
		Bob.v=(Bob.y+Bob.c)%4
		print(f'Bob recieved u')
		Bob.Zb=Bob.MB[u][Bob.v]

	def Send():
		print(f'Bob sending Zb[u][v] = {Bob.Zb} and v={Bob.v}')
		return(Bob.v,Bob.Zb)


print(f'\n Offline Phase: \n')
#Offline Phase

x=int(input ("Enter alice's number:"))
y=int(input ("Enter bob's number:"))

print(f'\nInitializing the Dealer:')
Dealer.Init()

print(f'\nInitializing Alice:')
Alice.Init(x,Dealer.RandA())

print(f'\nInitializing Bob:')
Bob.Init(y,Dealer.RandB())

print(f'\n Online Phase: \n')
#Online Phase

Bob.Receive(Alice.Send())
print(f'\n')
result_a, result_b = Bob.Send()
Alice.Receive(result_a,result_b)
print(f'\n')
z=Alice.Output()
print(f'the Output is {z}')
					