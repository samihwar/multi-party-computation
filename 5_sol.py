import random
import numpy as np

P=107   #we define P as global parameter
counter=0
#numberOfMuls = 22
class Dealer:
    alphaA = 0
    UAs = []
    KUAs = []
    TUAs = []

    VAs = []
    KVAs = []
    TVAs = []

    WAs = []
    KWAs = []
    TWAs = []

    alphaB = 0
    UBs = []
    KUBs = []
    TUBs = []

    VBs = []
    KVBs = []
    TVBs = []

    WBs = []
    KWBs = []
    TWBs = []
    def Init(numberOfMuls):
        Dealer.UAs = [None] * numberOfMuls
        Dealer.KUAs = [None] * numberOfMuls
        Dealer.TUAs = [None] * numberOfMuls
        Dealer.VAs = [None] * numberOfMuls
        Dealer.KVAs = [None] * numberOfMuls
        Dealer.TVAs = [None] * numberOfMuls
        Dealer.WAs = [None] * numberOfMuls
        Dealer.KWAs = [None] * numberOfMuls
        Dealer.TWAs = [None] * numberOfMuls

        Dealer.UBs = [None] * numberOfMuls
        Dealer.KUBs = [None] * numberOfMuls
        Dealer.TUBs = [None] * numberOfMuls
        Dealer.VBs = [None] * numberOfMuls
        Dealer.KVBs = [None] * numberOfMuls
        Dealer.TVBs = [None] * numberOfMuls
        Dealer.WBs = [None] * numberOfMuls
        Dealer.KWBs = [None] * numberOfMuls
        Dealer.TWBs = [None] * numberOfMuls

        for i in range(0,numberOfMuls):                   #creating all uvws
            Dealer.UAs[i]=random.randint(0,P-1)
            Dealer.VAs[i]=random.randint(0,P-1)
            Dealer.WAs[i]=((Dealer.UAs[i]*Dealer.VAs[i])%P)
    
        Dealer.alphaB = random.randint(0,P-1)
        for i in range(0,numberOfMuls):                   #creating uvw to bob
            Dealer.UBs[i]=random.randint(0,P-1)
            Dealer.KUBs[i]=random.randint(0,P-1)
            Dealer.TUBs[i]=(( (Dealer.alphaB*Dealer.UBs[i])%P + Dealer.KUBs[i] )%P)

            Dealer.VBs[i]=random.randint(0,P-1)
            Dealer.KVBs[i]=random.randint(0,P-1)
            Dealer.TVBs[i]=(( (Dealer.alphaB*Dealer.VBs[i])%P + Dealer.KVBs[i] )%P)

            Dealer.WBs[i]=((Dealer.UBs[i]*Dealer.VBs[i])%P)
            Dealer.KWBs[i]=random.randint(0,P-1)
            Dealer.TWBs[i]=(( (Dealer.alphaB*Dealer.WBs[i])%P + Dealer.KWBs[i] )%P)

        Dealer.alphaA = random.randint(0,P-1)
        for i in range (0,numberOfMuls):                  #creating uvw for alice
            Dealer.UAs[i]=((Dealer.UAs[i]-Dealer.UBs[i])%P)
            Dealer.KUAs[i]=random.randint(0,P-1)
            Dealer.TUAs[i]=(( (Dealer.alphaA*Dealer.UAs[i])%P + Dealer.KUAs[i] )%P)

            Dealer.VAs[i]=((Dealer.VAs[i]-Dealer.VBs[i])%P)
            Dealer.KVAs[i]=random.randint(0,P-1)
            Dealer.TVAs[i]=(( (Dealer.alphaA*Dealer.VAs[i])%P + Dealer.KVAs[i] )%P)

            Dealer.WAs[i]=((Dealer.WAs[i]-Dealer.WBs[i])%P)
            Dealer.KWAs[i]=random.randint(0,P-1)
            Dealer.TWAs[i]=(( (Dealer.alphaA*Dealer.WAs[i])%P + Dealer.KWAs[i] )%P)


    def RandA():
        print("\n\n Sending to Alice:")
        print("UAs    :",Dealer.UAs)
        print("UA_Tags:",Dealer.TUAs)
        print("VAs    :",Dealer.VAs)
        print("VA_Tags:",Dealer.TVAs)
        print("WAs    :",Dealer.WAs)
        print("WA_Tags:",Dealer.TWAs)

        print("\nAnd sending the keys to verify Bobs values")
        print("The bethas")
        print("UB_Keys:",Dealer.KUBs)
        print("VB_Keys:",Dealer.KVBs)
        print("WB_Keys:",Dealer.KWBs)
        print("And the alphaB:",Dealer.alphaB)
        return(Dealer.UAs,Dealer.TUAs,Dealer.VAs,Dealer.TVAs,Dealer.WAs,Dealer.TWAs,Dealer.alphaB,Dealer.KUBs,Dealer.KVBs,Dealer.KWBs)

    def RandB():
        print("\n\n Sending to Bob:")
        print("UBs    :",Dealer.UBs)
        print("UB_Tags:",Dealer.TUBs)
        print("VBs    :",Dealer.VBs)
        print("VB_Tags:",Dealer.TVBs)
        print("WBs    :",Dealer.WBs)
        print("WB_Tags:",Dealer.TWBs)

        print("\nAnd sending the keys to verify Alices values:")
        print("The bethas")
        print("UA_Keys:",Dealer.KUAs)
        print("VA_Keys:",Dealer.KVAs)
        print("WA_Keys:",Dealer.KWAs)
        print("And the alphaA:",Dealer.alphaA)
        return(Dealer.UBs,Dealer.TUBs,Dealer.VBs,Dealer.TVBs,Dealer.WBs,Dealer.TWBs,Dealer.alphaA,Dealer.KUAs,Dealer.KVAs,Dealer.KWAs)

    def secret_share(x:int):
        xa=random.randint(0,P-1)
        ka=random.randint(0,P-1)
        ta=(((Dealer.alphaA*xa)%P+ka)%P)

        xb=(x-xa)%P
        kb=random.randint(0,P-1)
        tb=(((Dealer.alphaB*xb)%P+kb)%P)

        return(xa,ka,ta,xb,kb,tb)

class Alice:
    UAs = []
    TUAs =[]

    VAs = []
    TVAs =[]

    WAs = []
    TWAs =[]

    alphaB = 0
    KUBs =[]
    KVBs =[]
    KWBs =[]

    values = []
    tvalues = []
    kvalues = []

    def Init(UAs,TUAs,VAs,TVAs,WAs,TWAs,alphaB,KUBs,KVBs,KWBs,leng):
        print("\nAlice taking:")
        Alice.values = [None] * leng
        Alice.tvalues = [None] * leng
        Alice.kvalues = [None] * leng
        print("The UVWs with the Tags")
        Alice.UAs=UAs
        Alice.TUAs=TUAs
        Alice.VAs=VAs
        Alice.TVAs=TVAs
        Alice.WAs=WAs
        Alice.TWAs=TWAs

        print("The keys of Bobs UVWs")
        Alice.alphaB=alphaB
        Alice.KUBs=KUBs
        Alice.KVBs=KVBs
        Alice.KWBs=KWBs

    def ver(ka,ta,xa):
        print(f'Alice Verifing with value:{xa}, Tag:{ta}, Alpha:{Alice.alphaB} and Betha:{ka}')
        if( ta==( ((Alice.alphaB*xa)%P+ka)%P) ):
            print("successfully verified")
            return 1
        else:
            print("verifing failed")
            print("changing to defult values(0)")
            for i in range(len(Alice.values)):
                Alice.values[i]=0
            exit -1

    def myDE(a,ta,ka,x,tx,kx,counter):
        d,td,kd_b=Alice.myADD(a,ta,ka,Alice.UAs[counter],Alice.TUAs[counter],Alice.KUBs[counter])
        e,te,ke_b=Alice.myADD(x,tx,kx,Alice.VAs[counter],Alice.TVAs[counter],Alice.KVBs[counter])
        return(d,td,kd_b,e,te,ke_b)
    
    def myMULLc(a,t,k_b,c):
        a=(a*c)%P
        t=(t*c)%P
        k_b=(k_b*c)%P
        return(a,t,k_b)
    
    def finalMUL(a,ta,ka_b,b,tb,kb_b,e,d,counter):
        tmpa,ttmpa,ktmpa_b=Alice.myMULLc(a,ta,ka_b,e)
        tmpa,ttmpa,ktmpa_b=Alice.myADD(Alice.WAs[counter],Alice.TWAs[counter],Alice.KWBs[counter],tmpa,ttmpa,ktmpa_b)
        #now we have [w]+e*[a]
        tmpb,ttmpb,ktmpb_b=Alice.myMULLc(b,tb,kb_b,d)
        tmpb,ttmpb,ktmpb_b=Alice.myADDc(tmpb,ttmpb,ktmpb_b,(-e*d)%P)
        #now we have d*[b]+e*d
        tmpb,ttmpb,ktmpb_b=Alice.myADD(tmpa,ttmpa,ktmpa_b,tmpb,ttmpb,ktmpb_b)
        return(tmpb,ttmpb,ktmpb_b)
    
    def myADD(a:int,ta:int,ka:int,b:int,tb:int,kb:int):
        a=(a+b)%P
        ta=(ta+tb)%P
        ka=(ka+kb)%P
        return(a,ta,ka)
    
    def myADDc(x:int,tag:int,key:int,c:int):
        x=(x+c)%P
        key=key
        return(x,tag,key)

class Bob:
    UBs = []
    TUBs =[]

    VBs = []
    TVBs =[]

    WBs = []
    TWBs =[]

    alphaA = 0
    KUAs =[]
    KVAs =[]
    KWAs =[]


    values = []
    tvalues = []
    kvalues = []

    def Init(UBs,TUBs,VBs,TVBs,WBs,TWBs,alphaA,KUAs,KVAs,KWAs,leng):
        print("\nBob taking:")
        Bob.values = [None] * leng
        Bob.tvalues = [None] * leng
        Bob.kvalues = [None] * leng
        print("The UVWs with the Tags")
        Bob.UBs=UBs
        Bob.TUBs=TUBs
        Bob.VBs=VBs
        Bob.TVBs=TVBs
        Bob.WBs=WBs
        Bob.TWBs=TWBs

        print("The keys of Alices UVWs")
        Bob.alphaA=alphaA
        Bob.KUAs=KUAs
        Bob.KVAs=KVAs
        Bob.KWAs=KWAs
    
    def ver(kb,tb,xb):
        print(f'Bob Verifing with value:{xb}, Tag:{tb}, Alpha:{Bob.alphaA} and Betha:{kb}')
        if( tb==( ((Bob.alphaA*xb)%P+kb)%P) ):
            print("successfully verified")
            return 1
        else:
            print("verifing failed")
            print("changing to defult values(0)")
            for i in range(len(Bob.values)):
                Bob.values[i]=0
            exit (1)
    
    def myDE(a,ta,ka,x,tx,kx,counter):
        d,td,kd_a=Bob.myADD(a,ta,ka,Bob.UBs[counter],Bob.TUBs[counter],Bob.KUAs[counter])
        e,te,ke_a=Bob.myADD(x,tx,kx,Bob.VBs[counter],Bob.TVBs[counter],Bob.KVAs[counter])
        return(d,td,kd_a,e,te,ke_a)
    
    def myMULLc(a,t,k_a,c):
        a=(a*c)%P
        t=(t*c)%P
        k_a=(k_a*c)%P
        return(a,t,k_a)
    
    def finalMUL(a,ta,ka_a,b,tb,kb_a,e,d,counter):
        tmpa,ttmpa,ktmpa_a=Bob.myMULLc(a,ta,ka_a,e)
        tmpa,ttmpa,ktmpa_a=Bob.myADD(Bob.WBs[counter],Bob.TWBs[counter],Bob.KWAs[counter],tmpa,ttmpa,ktmpa_a)
        #now we have [w]+e*[a]
        tmpb,ttmpb,ktmpb_a=Bob.myMULLc(b,tb,kb_a,d)
        tmpb,ttmpb,ktmpb_a=Bob.myADDc(tmpb,ttmpb,ktmpb_a,(-e*d)%P)
        #now we have d*[b]-e*d
        tmpb,ttmpb,ktmpb_a=Bob.myADD(tmpa,ttmpa,ktmpa_a,tmpb,ttmpb,ktmpb_a)
        return(tmpb,ttmpb,ktmpb_a)

    
    def myADD(a:int,ta:int,ka:int,b:int,tb:int,kb:int):
        a=(a+b)%P
        ta=(ta+tb)%P
        ka=(ka+kb)%P
        return(a,ta,ka)
    
    def myADDc(x:int,tag:int,key:int,c:int):
        x=x
        key=(key-(c*Bob.alphaA)%P)%P
        return(x,tag,key)


###########################################################

def MYMUL(a_a,ta_a,ka_b,x_a,tx_a,kx_b,a_b,ta_b,ka_a,x_b,tx_b,kx_a,counter):

    d_b,td_b,kd_a,e_b,te_b,ke_a=Bob.myDE(a_b,ta_b,ka_a,x_b,tx_b,kx_a,counter)
    d_a,td_a,kd_b,e_a,te_a,ke_b=Alice.myDE(a_a,ta_a,ka_b,x_a,tx_a,kx_b,counter)

    print(f'\nAlice sending d:{d_a} to bob to open it')
    Bob.ver(kd_a,td_a,d_a)
    print(f'Bob sending d:{d_b} to alice to open it')
    Alice.ver(kd_b,td_b,d_b)
    d=(d_a+d_b)%P

    print(f'\nAlice sending e:{e_a} to bob to open it')
    Bob.ver(ke_a,te_a,e_a)
    print(f'Bob sending e:{e_b} to alice to open it')
    Alice.ver(ke_b,te_b,e_b)
    e=(e_a+e_b)%P

    print(f'now we have e={e} and d={d}')

    res_b,rest_b,resk_a=Bob.finalMUL(a_b,ta_b,ka_a,x_b,tx_b,kx_a,e,d,counter)
    res_a,rest_a,resk_b=Alice.finalMUL(a_a,ta_a,ka_b,x_a,tx_a,kx_b,e,d,counter)
    counter=counter+1
    return(res_a,rest_a,resk_b,res_b,rest_b,resk_a,counter)


def  myCircuit(counter):
    TheCircuit = []
    #layers=int(input("How many layers in the circuit?"))
    layers=int(len(Mainvalues)/2)
    ogates=pow(2,layers-1)
    gates=ogates
    TheCircuit = [["X" for i in range(gates)] for j in range(layers)]
    # inp = "y" #"exit"
    print("to define MUL gate type M, and to define ADD gate type A")
    for i in range(layers):
        for j in range(gates):
            TheCircuit[i][j]=str(input(f'In the number {i+1} layer input the number {j+1} gate:'))
        gates=int(gates/2)

    print("\nEntering the circuit:\n")
    i=0
    j=0
    k=0
    inpArray_A = np.copy(Alice.values)
    kinpArray_A = np.copy(Alice.kvalues)
    tinpArray_A = np.copy(Alice.tvalues)
        
    leng = int(len(Mainvalues)/2)
    outArray_A = [0]*leng
    toutArray_A = [0]*leng
    koutArray_A = [0]*leng

    kinpArray_B = np.copy(Bob.kvalues)
    tinpArray_B = np.copy(Bob.tvalues)
    inpArray_B = np.copy(Bob.values)

    outArray_B = [0]*leng
    toutArray_B = [0]*leng
    koutArray_B = [0]*leng
    i=0
    gates=ogates
    for i in range(layers):
        k=0
        for j in range(gates):
            if(TheCircuit[i][j]=="M"):
                outArray_A[j],toutArray_A[j],koutArray_A[j],outArray_B[j],toutArray_B[j],koutArray_B[j],counter = MYMUL(inpArray_A[k],tinpArray_A[k],kinpArray_A[k],inpArray_A[k+1],tinpArray_A[k+1],kinpArray_A[k+1],inpArray_B[k],tinpArray_B[k],kinpArray_B[k],inpArray_B[k+1],tinpArray_B[k+1],kinpArray_B[k+1],counter)
            else:
                outArray_A[j],toutArray_A[j],koutArray_A[j] = Alice.myADD(inpArray_A[k],tinpArray_A[k],kinpArray_A[k],inpArray_A[k+1],tinpArray_A[k+1],kinpArray_A[k+1])
                outArray_B[j],toutArray_B[j],koutArray_B[j] = Bob.myADD(inpArray_B[k],tinpArray_B[k],kinpArray_B[k],inpArray_B[k+1],tinpArray_B[k+1],kinpArray_B[k+1])
            k=k+2   #next values
        gates=int(gates/2)  #updating number of the gates in the layer

        inpArray_A= []
        tinpArray_A= []
        kinpArray_A= []
        inpArray_B= []
        tinpArray_B= []
        kinpArray_B= []

        inpArray_A=np.copy(outArray_A)
        tinpArray_A=np.copy(toutArray_A)
        kinpArray_A=np.copy(koutArray_A)
        inpArray_B=np.copy(outArray_B)
        tinpArray_B=np.copy(toutArray_B)
        kinpArray_B=np.copy(koutArray_B)

        outArray_A= [0]*gates
        toutArray_A= [0]*gates
        koutArray_A= [0]*gates
        outArray_B= [0]*gates
        toutArray_B= [0]*gates
        koutArray_B= [0]*gates

    print(f'\n finishing the Circuit\n')
    return(inpArray_A[0],tinpArray_A[0],kinpArray_A[0],inpArray_B[0],tinpArray_B[0],kinpArray_B[0],counter)


#Main
Mainvalues = []
print(f'\n Offline Phase: \n')
#Offline Phase
P=int(input ("Enter the prime number P:"))
numberOfMuls=int(input("Enter the number of the MUL Gates:"))
print("Please insert the values in order how you gonna use them in the circuit!")
while True:
    number = input("Enter a number (or 'q' to quit): ")
    
    if number.lower() == 'q':
        break
    
    try:
        number = int(number)
        Mainvalues.append(number)
    except ValueError:
        print("Invalid input. Please enter a valid number or 'q' to quit.")

print("Numbers entered:", Mainvalues)

x = -1
i = 0
while(x!=-1):
    Mainvalues[i]=int(input(f'Enter the {i+1} value:')%P)

Dealer.Init(numberOfMuls)
UAs,TUAs,VAs,TVAs,WAs,TWAs,alphaB,KUBs,KVBs,KWBs = Dealer.RandA()
Alice.Init(UAs,TUAs,VAs,TVAs,WAs,TWAs,alphaB,KUBs,KVBs,KWBs,len(Mainvalues))

UBs,TUBs,VBs,TVBs,WBs,TWBs,alphaA,KUAs,KVAs,KWAs = Dealer.RandB()
Bob.Init(UBs,TUBs,VBs,TVBs,WBs,TWBs,alphaA,KUAs,KVAs,KWAs,len(Mainvalues))

print(f'\n online Phase: \n')
#online Phase

print("The Dealer secret sharing the values ")

i=0
for i in range(len(Mainvalues)):
    (Alice.values[i],Bob.kvalues[i],Alice.tvalues[i],Bob.values[i],Alice.kvalues[i],Bob.tvalues[i])=Dealer.secret_share(Mainvalues[i])
#secret sharing the values from Mainvalues

#now each one of them has the secret share of the values and there own UVW arrays using th MACs

ra,rta,rka,rb,rtb,rkb,counter=myCircuit(counter)

print(f'\nBob sending his C with the MACs')
Alice.ver(rka,rtb,rb)
print(f'Alice verified and opening the answer={(rb+ra)%P}')

print(f'\nAlice sending her C with the MACs')
Bob.ver(rkb,rta,ra)
print(f'Bob verified and opening the answer={(rb+ra)%P}')
