import random
import numpy as np

P=107#we define P as global parameter
counter=0
numberOfMuls = 22
class Dealer:
    alphaA = 0
    UAs = np.arange(numberOfMuls)
    KUAs = np.arange(numberOfMuls)
    TUAs = np.arange(numberOfMuls)

    VAs = np.arange(numberOfMuls)
    KVAs = np.arange(numberOfMuls)
    TVAs = np.arange(numberOfMuls)

    WAs = np.arange(numberOfMuls)
    KWAs = np.arange(numberOfMuls)
    TWAs = np.arange(numberOfMuls)

    alphaB = 0
    UBs = np.arange(numberOfMuls)
    KUBs = np.arange(numberOfMuls)
    TUBs = np.arange(numberOfMuls)

    VBs = np.arange(numberOfMuls)
    KVBs = np.arange(numberOfMuls)
    TVBs = np.arange(numberOfMuls)

    WBs = np.arange(numberOfMuls)
    KWBs = np.arange(numberOfMuls)
    TWBs = np.arange(numberOfMuls)
    def Init():
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

    aa = 0 #a1
    taa =0
    kaa_b=0

    ab = 0 #a2
    tab =0
    kab_b=0

    xa = 0 #x1
    txa =0
    kxa_b=0

    xb = 0 #x2
    txb =0
    kxb_b =0

    def Init(UAs,TUAs,VAs,TVAs,WAs,TWAs,alphaB,KUBs,KVBs,KWBs):
        print("\nAlice taking:")

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

    def gettingaa(aa_a,taa_a,kaa_b):
        Alice.aa=aa_a
        Alice.taa=taa_a
        Alice.kaa_b=kaa_b

    def gettingab(ab_a,tab_a,kab_b):
        Alice.ab=ab_a
        Alice.tab=tab_a
        Alice.kab_b=kab_b

    def gettingxa(xa_a,txa_a,kxa_b):
        Alice.xa=xa_a
        Alice.txa=txa_a
        Alice.kxa_b=kxa_b

    def gettingxb(xb_a,txb_a,kxb_b):
        Alice.xb=xb_a
        Alice.txb=txb_a
        Alice.kxb_b=kxb_b

    def ver(ka,ta,xa):
        print(f'Alice Verifing with value:{xa}, Tag:{ta}, Alpha:{Alice.alphaB} and Betha:{ka}')
        if( ta==( ((Alice.alphaB*xa)%P+ka)%P) ):
            print("successfully verified")
            return 1
        else:
            print("verifing failed")
            print("changing to defult values(0)")
            Alice.aa=0
            Alice.ab=0
            Alice.xa=0
            Alice.xb=0
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
    
    def myADD(a,ta,ka,b,tb,kb):
        a=(a+b)%P
        ta=(ta+tb)%P
        ka=(ka+kb)%P
        return(a,ta,ka)
    
    def myADDc(x,tag,key,c):
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

    aa = 0 #a1
    taa =0
    kaa_a=0

    ab = 0 #a2
    tab =0
    kab_a=0

    xa = 0 #x1
    txa =0
    kxa_a=0

    xb = 0 #x2
    txb =0
    kxb_a =0

    def Init(UBs,TUBs,VBs,TVBs,WBs,TWBs,alphaA,KUAs,KVAs,KWAs):
        print("\nBob taking:")

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

    def gettingaa(aa_b,taa_b,kaa_a):
        Bob.aa=aa_b
        Bob.taa=taa_b
        Bob.kaa_a=kaa_a

    def gettingab(ab_b,tab_b,kab_a):
        Bob.ab=ab_b
        Bob.tab=tab_b
        Bob.kab_a=kab_a

    def gettingxa(xa_b,txa_b,kxa_a):
        Bob.xa=xa_b
        Bob.txa=txa_b
        Bob.kxa_a=kxa_a

    def gettingxb(xb_b,txb_b,kxb_a):
        Bob.xb=xb_b
        Bob.txb=txb_b
        Bob.kxb_a=kxb_a
    
    def ver(kb,tb,xb):
        print(f'Bob Verifing with value:{xb}, Tag:{tb}, Alpha:{Bob.alphaA} and Betha:{kb}')
        if( tb==( ((Bob.alphaA*xb)%P+kb)%P) ):
            print("successfully verified")
            return 1
        else:
            print("verifing failed")
            print("changing to defult values(0)")
            Bob.aa=0
            Bob.ab=0
            Bob.xa=0
            Bob.xb=0
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
        #now we have d*[b]+e*d
        tmpb,ttmpb,ktmpb_a=Bob.myADD(tmpa,ttmpa,ktmpa_a,tmpb,ttmpb,ktmpb_a)
        return(tmpb,ttmpb,ktmpb_a)

    
    def myADD(a,ta,ka,b,tb,kb):
        a=(a+b)%P
        ta=(ta+tb)%P
        ka=(ka+kb)%P
        return(a,ta,ka)
    
    def myADDc(x,tag,key,c):
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
    print("\nEntering the circuit:\n")
    amul_a,tamul_a,kamul_a,amul_b,tamul_b,kamul_b,counter =MYMUL(Alice.aa,Alice.taa,Alice.kaa_b,Alice.xa,Alice.txa,Alice.kxa_b,Bob.aa,Bob.taa,Bob.kaa_a,Bob.xa,Bob.txa,Bob.kxa_a,counter)
    bmul_a,tbmul_a,kbmul_a,bmul_b,tbmul_b,kbmul_b,counter =MYMUL(Alice.ab,Alice.tab,Alice.kab_b,Alice.xb,Alice.txb,Alice.kxb_b,Bob.ab,Bob.tab,Bob.kab_a,Bob.xb,Bob.txb,Bob.kxb_a,counter)
    #Done the left and the right mul

    cmul_a,ctmul_a,ktmul_a = Alice.myADD(amul_a,tamul_a,kamul_a,bmul_a,tbmul_a,kbmul_a)
    cmul_b,ctmul_b,ktmul_b = Bob.myADD(amul_b,tamul_b,kamul_b,bmul_b,tbmul_b,kbmul_b)
    #now we have the result C

    resa_a,tresa_a,kresa_a=Alice.myADDc(cmul_a,ctmul_a,ktmul_a,-1)
    resa_b,tresa_b,kresa_b=Bob.myADDc(cmul_b,ctmul_b,ktmul_b,-1)
    #1_mul (C * (C-1))
    resa_a,tresa_a,kresa_a,resa_b,tresa_b,kresa_b,counter=MYMUL(cmul_a,ctmul_a,ktmul_a,resa_a,tresa_a,kresa_a,cmul_b,ctmul_b,ktmul_b,resa_b,tresa_b,kresa_b,counter)

    #now we do -2 -3
    resb_a,tresb_a,kresb_a=Alice.myADDc(cmul_a,ctmul_a,ktmul_a,-2)
    resb_b,tresb_b,kresb_b=Bob.myADDc(cmul_b,ctmul_b,ktmul_b,-2)

    resc_a,tresc_a,kresc_a=Alice.myADDc(cmul_a,ctmul_a,ktmul_a,-3)
    resc_b,tresc_b,kresc_b=Bob.myADDc(cmul_b,ctmul_b,ktmul_b,-3)
    #2_mul( (c-2)*(c-3) )
    resb_a,tresb_a,kresb_a,resb_b,tresb_b,kresb_b,counter=MYMUL(resb_a,tresb_a,kresb_a,resc_a,tresc_a,kresc_a,resb_b,tresb_b,kresb_b,resc_b,tresc_b,kresc_b,counter)

    #and here we mul(1_mul*2_mul) so if one of the values is 0 the result will be 0 that means that the number(C) is less than 4
    resa_a,tresa_a,kresa_a,resa_b,tresa_b,kresa_b,counter=MYMUL(resa_a,tresa_a,kresa_a,resb_a,tresb_a,kresb_a,resa_b,tresa_b,kresa_b,resb_b,tresb_b,kresb_b,counter)

    print(f'\n finishing the Circuit\n')
    return(resa_a,tresa_a,kresa_a,resa_b,tresa_b,kresa_b,counter)


#Main

print(f'\n Offline Phase: \n')
#Offline Phase
P=int(input ("Enter the prime number P:"))

aa=int(input ("Enter alice's a1 in range (0-3):"))
ab=int(input ("Enter alice's a2 in range (0-3):"))
xa=int(input ("Enter bob's x1 in range (0-3):"))
xb=int(input ("Enter bob's x2 in range (0-3):"))

Dealer.Init()
UAs,TUAs,VAs,TVAs,WAs,TWAs,alphaB,KUBs,KVBs,KWBs = Dealer.RandA()
Alice.Init(UAs,TUAs,VAs,TVAs,WAs,TWAs,alphaB,KUBs,KVBs,KWBs)

UBs,TUBs,VBs,TVBs,WBs,TWBs,alphaA,KUAs,KVAs,KWAs = Dealer.RandB()
Bob.Init(UBs,TUBs,VBs,TVBs,WBs,TWBs,alphaA,KUAs,KVAs,KWAs)

print(f'\n online Phase: \n')
#online Phase

print("The Dealer secret sharing a1,a2,x1,x2 ")

(aa_a,kaa_a,taa_a,aa_b,kaa_b,taa_b)=Dealer.secret_share(aa)
Alice.gettingaa(aa_a,taa_a,kaa_b)
Bob.gettingaa(aa_b,taa_b,kaa_a)

(ab_a,kab_a,tab_a,ab_b,kab_b,tab_b)=Dealer.secret_share(ab)
Alice.gettingab(ab_a,tab_a,kab_b)
Bob.gettingab(ab_b,tab_b,kab_a)

(xa_a,kxa_a,txa_a,xa_b,kxa_b,txa_b)=Dealer.secret_share(xa)
Alice.gettingxa(xa_a,txa_a,kxa_b)
Bob.gettingxa(xa_b,txa_b,kxa_a)

(xb_a,kxb_a,txb_a,xb_b,kxb_b,txb_b)=Dealer.secret_share(xb)
Alice.gettingxb(xb_a,txb_a,kxb_b)
Bob.gettingxb(xb_b,txb_b,kxb_a)

#now each one of them has the secret share of a1,a2,x1,x2 and there own UVW arrays using th MACs

ra,rta,rka,rb,rtb,rkb,counter=myCircuit(counter)
print(f'\nBob sending his C with the MACs')
Alice.ver(rka,rtb,rb)
print(f'Alice verified and opening C={(rb+ra)%P}')
if((rb+ra)%P):print("that means its 1")
else:print("that means its 0")

print(f'\nAlice sending her C with the MACs')
Bob.ver(rkb,rta,ra)
print(f'Bob verified and opening C={(rb+ra)%P}')
if((rb+ra)%P):print("that means its 1")
else:print("that means its 0")
