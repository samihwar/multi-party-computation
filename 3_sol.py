import random
import numpy as np

class Dealer:
    UAs = np.arange(22)
    VAs = np.arange(22)
    WAs = np.arange(22)
    UBs = np.arange(22)
    VBs = np.arange(22)
    WBs = np.arange(22)
    def Init():
        for i in range(0,22):                   #creating all uvws
            Dealer.UAs[i]=random.randint(0,1)
            Dealer.VAs[i]=random.randint(0,1)
            Dealer.WAs[i]=(Dealer.UAs[i]*Dealer.VAs[i])%2

        for i in range(0,22):                   #creating uvw to bob
            Dealer.UBs[i]=random.randint(0,1)
            Dealer.VBs[i]=random.randint(0,1)
            Dealer.WBs[i]=(Dealer.UBs[i]*Dealer.VBs[i])%2

        for i in range (0,22):                  #creating uvw for alice
            Dealer.UAs[i]=(Dealer.UAs[i]+Dealer.UBs[i])%2
            Dealer.VAs[i]=(Dealer.VAs[i]+Dealer.VBs[i])%2
            Dealer.WAs[i]=(Dealer.WAs[i]+Dealer.WBs[i])%2

    def RandA():
        print("sending UAs to Alice:",Dealer.UAs)
        print("sending VAs to Alice:",Dealer.VAs)
        print("sending WAs to Alice:",Dealer.WAs)
        return(Dealer.UAs,Dealer.VAs,Dealer.WAs)

    def RandB():
        print("sending UBs to Bob:",Dealer.UBs)
        print("sending VBs to Bob:",Dealer.VBs)
        print("sending WBs to Bob:",Dealer.WBs)
        return(Dealer.UBs,Dealer.VBs,Dealer.WBs)

class Alice:
    UAs = []
    VAs = []
    WAs = []
    aa = np.arange(2)#a1 we want to save it as bits
    ab = np.arange(2)#a2 we want to save it as bits
    xa = np.arange(2)#x1 we want to save it as bits
    xb = np.arange(2)#x2 we want to save it as bits

    def Init(aa:int,ab:int,tempa,tempb,tempc):
        print("Alice taking the UVWs")
        Alice.UAs=tempa
        Alice.VAs=tempb
        Alice.WAs=tempc

        Alice.aa[1]=aa//2
        Alice.aa[0]=aa%2
        Alice.ab[1]=ab//2
        Alice.ab[0]=ab%2
        print("Alice.a1:",Alice.aa)#
        print("Alice.a2:",Alice.ab)#

    def senda():
        tempaa = np.arange(2)       #doing the share to a1 and a2 and sending to Bob
        tempab = np.arange(2)
        for i in range (0,2):
            tempaa[i] = random.randint(0,1)#for Bob
            Alice.aa[i]=(Alice.aa[i]+tempaa[i])%2
            tempab[i] = random.randint(0,1)#for Bob
            Alice.ab[i]=(Alice.ab[i]+tempab[i])%2
        print("Alice takes")
        print("Alice.a1A:",Alice.aa)
        print("Alice.a2A:",Alice.ab)
        return(tempaa,tempab)   #sending secret sharing of a1 a2 to bob

    def receive(xa,xb):
        Alice.xa=xa
        Alice.xb=xb
        print("Alice recieved")
        print("Alice.x1A:",Alice.xa)
        print("Alice.x2A:",Alice.xb)

    def XOR(x:int,y:int):
        return((x+y)%2)

    def finalStageAND(aa:int,xa:int,wa:int,e:int,d:int):
        tempa=Alice.XOR(wa,(e*aa))
        tempb=Alice.XOR((d*xa),(e*d))
        return(Alice.XOR(tempa,tempb))

class Bob:
    UBs = []
    VBs = []
    WBs = []
    xa = np.arange(2)#x1 we want to save it as bits
    xb = np.arange(2)#x2 we want to save it as bits
    aa = np.arange(2)#a1 we want to save it as bits
    ab = np.arange(2)#a2 we want to save it as bits

    def Init(xa:int,xb:int,tempa,tempb,tempc):
        print("Bob taking the UVWs")
        Bob.UBs=tempa
        Bob.VBs=tempb
        Bob.WBs=tempc

        Bob.xa[1]=xa//2
        Bob.xa[0]=xa%2
        Bob.xb[1]=xb//2
        Bob.xb[0]=xb%2
        print("Bob.x1:",Bob.xa)
        print("Bob.x2",Bob.xb)

    def sendx():
        tempxa = np.arange(2)
        tempxb = np.arange(2)
        for i in range (0,2):
            tempxa[i] = random.randint(0,1) #for Alice
            Bob.xa[i]=(Bob.xa[i]+tempxa[i])%2
            tempxb[i] = random.randint(0,1) #for Alice
            Bob.xb[i]=(Bob.xb[i]+tempxb[i])%2
        print("Bob takes")
        print("Bob.x1B:",Bob.xa)
        print("Bob.x2B:",Bob.xb)
        return(tempxa,tempxb)   #sending secret sharing of x1 x2 to Alice

    def receive(aa,ab):
        Bob.aa=aa
        Bob.ab=ab
        print("Bob recieved")
        print("Bob.a1B:",Bob.aa)
        print("Bob.a2B:",Bob.ab)

    def XOR(x:int,y:int):
        return((x+y)%2)

    def finalStageAND(ab:int,xb:int,wb:int,e:int,d:int):
        tempa=Bob.XOR(wb,(e*ab))
        tempb=d*xb
        return(Bob.XOR(tempa,tempb))

############################################################

def XOR (aa,xa,ab,xb):
    print("entering XOR")
    za=Alice.XOR(aa,xa)
    zb=Bob.XOR(ab,xb)
    print("XOR returning for alice, for bob:",za,zb)
    return(za,zb)

def finalStageAND(aa,xa,wa,ab,xb,wb,e,d):
    return(Alice.finalStageAND(aa,xa,wa,e,d),Bob.finalStageAND(ab,xb,wb,e,d))

def AND (aa:int,xa:int,ua:int,va:int,wa:int,ab:int,xb:int,ub:int,vb:int,wb:int,counter:int):#the first 5 elements from alice and the rest from bob
    print("Entering AND number:",counter)
    da,db=XOR(aa,ua,ab,ub)
    #now we want to open [d]
    #we did it like if bob send it throu the "xor" function and then alice did the final xor
    d=Alice.XOR(da,db)
    ea,eb=XOR(xa,va,xb,vb)
    #now we want to open [e]
    #we did it like if bob send it throu the "xor" function and then alice did the final xor
    e=Alice.XOR(ea,eb)
    za,zb=finalStageAND(aa,xa,wa,ab,xb,wb,e,d)
    counter+=1
    print("AND returning for alice, for bob:",za,zb)
    return(za,zb,counter)

#how to use AND XOR

#XOR e.x a1 xor a2 => 
#ALICE.res , BOB.res = XOR(Alice.a1,Alice.a2,Bob.a1,Bob.a2)

#AND e.x a1 AND a2 =>
#ALICE.res , BOB.res , counter = AND(Alice.a1,Alice.a2,Alice.u[counter],Alice.v[counter],Alice.w[counter],Bob.a1,Bob.a2,Bob.u[counter],Bob.v[counter],Bob.w[counter],counter)


#          A0 ,     A1 ,    x0 ,   x1                          A0 ,    A1 ,   x0 ,    x1      A1 A0 * X1 X0 = C3 C2 C1 C0
def myMult(Aaa:int,Aab:int,Axa:int,Axb:int,Au:[],Av:[],Aw:[],Baa:int,Bab:int,Bxa:int,Bxb:int,Bu:[],Bv:[],Bw:[],counter:int):
    #T=temp R=result
    RAa,RBa,counter = AND(Aaa,Axa,Au[counter],Av[counter],Aw[counter],Baa,Bxa,Bu[counter],Bv[counter],Bw[counter],counter)
    TAa,TBa,counter = AND(Aab,Axa,Au[counter],Av[counter],Aw[counter],Bab,Bxa,Bu[counter],Bv[counter],Bw[counter],counter)
    TAb,TBb,counter = AND(Aaa,Axb,Au[counter],Av[counter],Aw[counter],Baa,Bxb,Bu[counter],Bv[counter],Bw[counter],counter)
    TAc,TBc,counter = AND(Aab,Axb,Au[counter],Av[counter],Aw[counter],Bab,Bxb,Bu[counter],Bv[counter],Bw[counter],counter)

    RAb,RBb = XOR(TAa,TAb,TBa,TBb)

    TAd,TBd,counter = AND(TAa,TAb,Au[counter],Av[counter],Aw[counter],TBa,TBb,Bu[counter],Bv[counter],Bw[counter],counter)
    
    RAc,RBc = XOR(TAd,TAc,TBd,TBc)

    RAd,RBd,counter = AND(TAd,TAc,Au[counter],Av[counter],Aw[counter],TBd,TBc,Bu[counter],Bv[counter],Bw[counter],counter)

    return(RAa,RAb,RAc,RAd,RBa,RBb,RBc,RBd,counter)#c0 c1 c2 c3 counter

def fullAdder(Aa:int,Ab:int,Acin:int,Au:[],Av:[],Aw:[],Ba:int,Bb:int,Bcin:int,Bu:[],Bv:[],Bw:[],counter:int):
    TAa,TBa = XOR(Aa,Ab,Ba,Bb)
    TAb,TBb,counter = AND(Aa,Ab,Au[counter],Av[counter],Aw[counter],Ba,Bb,Bu[counter],Bv[counter],Bw[counter],counter)
    
    Sa,Sb=XOR(TAa,Acin,TBa,Bcin)

    TAc,TBc,counter=AND(Acin,TAa,Au[counter],Av[counter],Aw[counter],Bcin,TBa,Bu[counter],Bv[counter],Bw[counter],counter)
    Acout,Bcout = XOR(TAc,TAb,TBc,TBb)

    return(Sa,Sb,Acout,Bcout,counter)

#              |4 vectors[2]  + 3 arrays||4 vectors[2] + 3 arrays|
def  myCircuit(Aaa:[],Aab:[],Axa:[],Axb:[],Au:[],Av:[],Aw:[],Baa:[],Bab:[],Bxa:[],Bxb:[],Bu:[],Bv:[],Bw:[],counter:int):
     print("\nEntering the circuit:\n")
     #first mull => A0*X0=M0
     MaAa,MaAb,MaAc,MaAd,MaBa,MaBb,MaBc,MaBd,counter = myMult(Aaa[0],Aaa[1],Axa[0],Axa[1],Au,Av,Aw,Baa[0],Baa[1],Bxa[0],Bxa[1],Bu,Bv,Bw,counter)
     #second mull => A1*X1=M1
     MbAa,MbAb,MbAc,MbAd,MbBa,MbBb,MbBc,MbBd,counter = myMult(Aab[0],Aab[1],Axb[0],Axb[1],Au,Av,Aw,Bab[0],Bab[1],Bxb[0],Bxb[1],Bu,Bv,Bw,counter)
     
     #the first full adder ==>
     TAa,TBa = XOR(MaAa,MbAa,MaBa,MbBa)
     TAb,TBb,counter = AND(MaAa,MbAa,Au[counter],Av[counter],Aw[counter],MaAb,MbAb,Bu[counter],Bv[counter],Bw[counter],counter)
     
     #here the cin is 0 so
     Saa=Alice.XOR(TAa,0)
     Sba=TBa

     TAc=TAa*0
     TBc=TBa*0
     Acouta,Bcouta = XOR(TAc,TAb,TBc,TBb)

     print("\nDone with the first adder:\n")
     # and then we continue the rest of the full adders
     Sab,Sbb,Acoutb,Bcoutb,counter = fullAdder(MaAb,MbAb,Acouta,Au,Av,Aw,MaBb,MbBb,Bcouta,Au,Av,Aw,counter)
     Sac,Sbc,Acoutc,Bcoutc,counter = fullAdder(MaAc,MbAc,Acoutb,Au,Av,Aw,MaBc,MbBc,Bcoutb,Au,Av,Aw,counter)
     Sad,Sbd,Acoutd,Bcoutd,counter = fullAdder(MaAd,MbAd,Acoutc,Au,Av,Aw,MaBd,MbBd,Bcoutc,Au,Av,Aw,counter)

     # here we have Saa Acouta Sab Acoutb Sac Acoutc Sad Acoutd for Alice
     # here we have Sba Bcouta Sbb Bcoutb Sbc Bcoutc Sbd Bcoutd for Bob

     print("\n Sxa = s for x the first one,  Sxb = s for x the second one...")
     print("\n and the Xcouta = Cout for x the first one,    Xcoutb = Cout for x the second one...\n")
     print(f"Alice takes Saa:{Saa}  Acouta:{Acouta}     Sab:{Sab}   Acoutb:{Acoutb}     Sac:{Sac}   Acoutc:{Acoutc}     Sad:{Sad}   Acoutd:{Acoutd}")
     print(f"Bob takes   Sba:{Sba}  Bcouta:{Bcouta}     Sbb:{Sbb}   Bcoutb:{Bcoutb}     Sbc:{Sbc}   Bcoutc:{Bcoutc}     Sbd:{Sbd}   Bcoutd:{Bcoutd}")
     print("and now for the final check")

     TAd,TBd,counter = AND(Sac,Sad,Au[counter],Av[counter],Aw[counter],Sbc,Sbd,Bu[counter],Bv[counter],Bw[counter],counter)
     TAe,TBe = XOR(Sac,Sad,Sbc,Sbd)

     TAf,TBf = XOR(TAd,TAe,TBd,TBe)

     TAg,TBg,counter = AND(TAf,Acoutd,Au[counter],Av[counter],Aw[counter],TBf,Bcoutd,Bu[counter],Bv[counter],Bw[counter],counter)
     TAh,TBh = XOR(TAf,Acoutd,TBf,Bcoutd)

     RA,RB = XOR(TAg,TAh,TBg,TBh)

     print(f'\n finishing the Circuit and sending RA={RA}, RB={RB} \n')
     return(RA,RB,counter)


#Main

print(f'\n Offline Phase: \n')
#Offline Phase

aa=int(input ("Enter alice's a1 in range (0-3):"))
ab=int(input ("Enter alice's a2 in range (0-3):"))
xa=int(input ("Enter bob's x1 in range (0-3):"))
xb=int(input ("Enter bob's x2 in range (0-3):"))

Dealer.Init()
tempa,tempb,tempc = Dealer.RandA()
Alice.Init(aa,ab,tempa,tempb,tempc)
tempa,tempb,tempc = Dealer.RandB()
Bob.Init(xa,xb,tempa,tempb,tempc)

print(f'\n online Phase: \n')
#online Phase
aa,ab=Alice.senda()#two arrays
Bob.receive(aa,ab)
xa,xb=Bob.sendx()#two arrays
Alice.receive(xa,xb)
#now each one of them has the secret share of a1,a2,x1,x2 and there own UVW arrays
counter=0

RA,RB,counter = myCircuit(Alice.aa,Alice.ab,Alice.xa,Alice.xb,Alice.UAs,Alice.VAs,Alice.WAs,Bob.aa,Bob.ab,Bob.xa,Bob.xb,Bob.UBs,Bob.VBs,Bob.WBs,counter)
#here we want to open it
print(f'\n opening the result => \n')

print(f'Bob sending RB to Alice \n')
Result=Alice.XOR(RB,RA)
print(f'\nThe result is {Result} \n')