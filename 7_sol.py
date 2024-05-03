#ps1-Samih Warwar-324888155
#ps2-Maias Omar-322645748
#ps3-Yara Shamali-315892141

import random
import numpy as np
from typing import List
import hashlib

Q=131
g=2
P=2*Q+1
# ill define globaly the three funcions (pk,sk)=Gen() ,C=Enc(m),m=Dec(C)
# we know that pk=(g,h) since we know that g is global we will use h as pk

def Gen():
    sk=random.randint(0,Q-1)
    h=pow(g,sk,P)
    #pk=g,h
    return(h,sk)

def Enc(m,h):# we all know the g so for the pk just gonna send the h
    r=random.randint(0,Q-1)
    gr=pow(g,r,P)
    h=pow(h,r,P)
    C=[gr,(m*h)%P]
    return(C)

def Dec(sk,C:List[int]):
    ca=C[0]
    cb=C[1]
    ca = pow(int(ca),int(sk),int(P))
    cb=(cb*pow(ca,-1,P))%P
    return(cb)

def OGen():
    s=random.randint(0,P-1)
    s=pow(s,2)%P
    return s

class Alice:            #garbler
    m = None #the massage she wants to send
    h_b = None #Bobs public key
    C = None #Bobs encryption
    Cin0_0 = None
    Cin0_1 = None
    aa = np.empty(2)#a1 we want to save it as bits
    ab = np.empty(2)#a2 we want to save it as bits
    wire_label_A00_0 = None #a0[0]
    wire_label_A00_1 = None
    wire_label_x00_0 = None #x0[0]
    wire_label_x00_1 = None
    wire_label_A10_0 = None #a0[1]
    wire_label_A10_1 = None
    wire_label_x10_0 = None #x0[1]
    wire_label_x10_1 = None
    wire_label_A01_0 = None #a1[0]
    wire_label_A01_1 = None
    wire_label_x01_0 = None #x1[0]
    wire_label_x01_1 = None
    wire_label_A11_0 = None #a1[1]
    wire_label_A11_1 = None
    wire_label_x11_0 = None #x1[1]
    wire_label_x11_1 = None

    def Init(aa:int,ab:int):
        Alice.Cin0_0 = generate_random_wire(88)#the first Cin in the first adder
        Alice.Cin0_1 = generate_random_wire(88)#just to make it work
        Alice.aa[1]=aa//2 
        Alice.aa[0]=aa%2
        Alice.ab[1]=ab//2
        Alice.ab[0]=ab%2
        Alice.aa = Alice.aa.astype(int)
        Alice.ab = Alice.ab.astype(int)
        Alice.wire_label_A00_0 = generate_random_wire(88)
        Alice.wire_label_A00_1 = generate_random_wire(88)
        Alice.wire_label_x00_0 = generate_random_wire(88)
        Alice.wire_label_x00_1 = generate_random_wire(88)
        Alice.wire_label_A10_0 = generate_random_wire(88)
        Alice.wire_label_A10_1 = generate_random_wire(88)
        Alice.wire_label_x10_0 = generate_random_wire(88)
        Alice.wire_label_x10_1 = generate_random_wire(88)
        Alice.wire_label_A01_0 = generate_random_wire(88)
        Alice.wire_label_A01_1 = generate_random_wire(88)
        Alice.wire_label_x01_0 = generate_random_wire(88)
        Alice.wire_label_x01_1 = generate_random_wire(88)
        Alice.wire_label_A11_0 = generate_random_wire(88)
        Alice.wire_label_A11_1 = generate_random_wire(88)
        Alice.wire_label_x11_0 = generate_random_wire(88)
        Alice.wire_label_x11_1 = generate_random_wire(88)

        print("Alice.a1:",Alice.aa)
        print("Alice.a2:",Alice.ab)

    def Sending_vars():
        Bob.Cin0_0=Alice.Cin0_0
        if(Alice.aa[0]==0):
            Bob.wire_label_A00=Alice.wire_label_A00_0
        else:
            Bob.wire_label_A00=Alice.wire_label_A00_1
        if(Alice.aa[1]==0):
            Bob.wire_label_A01=Alice.wire_label_A01_0
        else:
            Bob.wire_label_A01=Alice.wire_label_A01_1
        
        if(Alice.ab[0]==0):
            Bob.wire_label_A10=Alice.wire_label_A10_0
        else:
            Bob.wire_label_A10=Alice.wire_label_A10_1
        if(Alice.ab[1]==0):
            Bob.wire_label_A11=Alice.wire_label_A11_0
        else:
            Bob.wire_label_A11=Alice.wire_label_A11_1

    def receiverOne_OT_Two(pka,pkb,ma,mb):
        ca=Enc(ma,pka)
        cb=Enc(mb,pkb)
        return(ca,cb)

class Bob:
    SKs = np.empty(4)
    Cin0_0 = None
    wire_label_A00 = None
    wire_label_x00 = None
    wire_label_A10 = None
    wire_label_x10 = None
    wire_label_A01 = None
    wire_label_x01 = None
    wire_label_A11 = None
    wire_label_x11 = None

    xa = np.empty(2)#x1 we want to save it as bits
    xb = np.empty(2)#x2 we want to save it as bits

    def Init(xa:int,xb:int):
        Bob.xa[1]=xa//2
        Bob.xa[0]=xa%2
        Bob.xb[1]=xb//2
        Bob.xb[0]=xb%2
        Bob.xa = Bob.xa.astype(int)
        Bob.xb = Bob.xb.astype(int)
        print("Bob.x1:",Bob.xa)
        print("Bob.x2",Bob.xb)

    def senderOne_OT_Two(i,b):
        # now we'll run 1 out of 2 OT
        pk,Bob.SKs[i]=Gen()
        pktag=OGen()
        if(b==1):#if true that means our 'b'= 1
            return(pktag,pk)
        else: 
            return(pk,pktag)
        
    def DEC(arr,wire0,wire1):
        print("\nDecrypting:")
        res=generate_128_bit_wire_from176(wire0+wire1)
        #a mask to find if there is a tail of zeros
        bitmask="00000000000000000000000000000000000000000000000000000000000000000000000000000000000000001111111111111111111111111111111111111111"
        bitmask = int(bitmask, 2)
        for i in range (0,4):
            check = (res ^ int.from_bytes(arr[i], byteorder='big'))
            print(check.to_bytes(16, byteorder='big'))
            # Convert the number to a binary string representation
            print((check & bitmask).to_bytes(16, byteorder='big'))
            if (check & bitmask == 0):
                # Extract the first 88 bits as an integer
                first_88_bits = check >> (40)
                # Convert the first 88 bits back to bytes
                first_88_bits_bytes = first_88_bits.to_bytes(11, byteorder='big')
                return first_88_bits_bytes
        exit(-1)


######################### MAIN FUNCTIONS ###################################

def generate_128_bit_wire_from176(wire_176):#takes the 176b wire and give 88b wire
    # Compute the SHA-256 hash of the wire
    sha256_hash = hashlib.sha256(wire_176).digest()

    # Extract the most significant 88 bits from the hash
    desired_bits = 128
    hash_int = int.from_bytes(sha256_hash, byteorder='big')
    wire_88 = hash_int >> (256 - desired_bits)

    return wire_88

def generate_random_wire(length):
    # Generate a random integer with the desired number of bits
    random_number = random.getrandbits(length)

    # Convert the random number to bytes
    wire_bytes = random_number.to_bytes((length + 7) // 8, byteorder='big')

    return wire_bytes

def garbled_AND_fun(wire_label_A0,wire_label_A1,wire_label_B0,wire_label_B1,result_label_0,result_label_1):
    garbledAND = [
        ((generate_128_bit_wire_from176(wire_label_A0 + wire_label_B0))^(int.from_bytes(result_label_0+ b'\x00' * 5, byteorder='big'))).to_bytes(16, byteorder='big'),
        ((generate_128_bit_wire_from176(wire_label_A0 + wire_label_B1))^(int.from_bytes(result_label_0+ b'\x00' * 5, byteorder='big'))).to_bytes(16, byteorder='big'),
        ((generate_128_bit_wire_from176(wire_label_A1 + wire_label_B0))^(int.from_bytes(result_label_0+ b'\x00' * 5, byteorder='big'))).to_bytes(16, byteorder='big'),
        ((generate_128_bit_wire_from176(wire_label_A1 + wire_label_B1))^(int.from_bytes(result_label_1+ b'\x00' * 5, byteorder='big'))).to_bytes(16, byteorder='big')
        ]
    random.shuffle(garbledAND)
    return garbledAND

def garbled_XOR_fun(wire_label_A0,wire_label_A1,wire_label_B0,wire_label_B1,result_label_0,result_label_1):
    garbledXOR = [
        ((generate_128_bit_wire_from176(wire_label_A0 + wire_label_B0))^(int.from_bytes(result_label_0+ b'\x00' * 5, byteorder='big'))).to_bytes(16, byteorder='big'),
        ((generate_128_bit_wire_from176(wire_label_A0 + wire_label_B1))^(int.from_bytes(result_label_1+ b'\x00' * 5, byteorder='big'))).to_bytes(16, byteorder='big'),
        ((generate_128_bit_wire_from176(wire_label_A1 + wire_label_B0))^(int.from_bytes(result_label_1+ b'\x00' * 5, byteorder='big'))).to_bytes(16, byteorder='big'),
        ((generate_128_bit_wire_from176(wire_label_A1 + wire_label_B1))^(int.from_bytes(result_label_1+ b'\x00' * 5, byteorder='big'))).to_bytes(16, byteorder='big')
        ]
    random.shuffle(garbledXOR)
    return garbledXOR

def MUL_STAGE(wire_label_A0_0,wire_label_A0_1,wire_label_A1_0,wire_label_A1_1,wire_label_x0_0,wire_label_x0_1,wire_label_x1_0,wire_label_x1_1):
    #first row
    first_MUL = []
    #rl= result label
    rl0_0 = generate_random_wire(88)
    rl0_1 = generate_random_wire(88)
    first_MUL.append(garbled_AND_fun(wire_label_A0_0,wire_label_A0_1,wire_label_x0_0,wire_label_x0_1,rl0_0,rl0_1))

    rl1_0 = generate_random_wire(88)
    rl1_1 = generate_random_wire(88)
    first_MUL.append(garbled_AND_fun(wire_label_A1_0,wire_label_A1_1,wire_label_x0_0,wire_label_x0_1,rl1_0,rl1_1))

    rl2_0 = generate_random_wire(88)
    rl2_1 = generate_random_wire(88)
    first_MUL.append(garbled_AND_fun(wire_label_A0_0,wire_label_A0_1,wire_label_x1_0,wire_label_x1_1,rl2_0,rl2_1))

    rl3_0 = generate_random_wire(88)
    rl3_1 = generate_random_wire(88)
    first_MUL.append(garbled_AND_fun(wire_label_A1_0,wire_label_A1_1,wire_label_x1_0,wire_label_x1_1,rl3_0,rl3_1))

    #second row

    rl4_0 = generate_random_wire(88)
    rl4_1 = generate_random_wire(88)
    first_MUL.append(garbled_XOR_fun(rl1_0,rl1_1,rl2_0,rl2_1,rl4_0,rl4_1))

    rl5_0 = generate_random_wire(88)
    rl5_1 = generate_random_wire(88)
    first_MUL.append(garbled_AND_fun(rl1_0,rl1_1,rl2_0,rl2_1,rl5_0,rl5_1))

    #third row

    rl6_0 = generate_random_wire(88)
    rl6_1 = generate_random_wire(88)
    first_MUL.append(garbled_AND_fun(rl3_0,rl3_1,rl5_0,rl5_1,rl6_0,rl6_1))

    rl7_0 = generate_random_wire(88)
    rl7_1 = generate_random_wire(88)
    first_MUL.append(garbled_XOR_fun(rl3_0,rl3_1,rl5_0,rl5_1,rl7_0,rl7_1))

    return (rl0_0,rl0_1,rl4_0,rl4_1,rl7_0,rl7_1,rl6_0,rl6_1,first_MUL)

def ADDER_STAGE(A0,A1,B0,B1,Cin0,Cin1):
    first_ADD=[]

    #first row
    rl0_0 = generate_random_wire(88)
    rl0_1 = generate_random_wire(88)
    first_ADD.append(garbled_XOR_fun(A0,A1,B0,B1,rl0_0,rl0_1))

    rl1_0 = generate_random_wire(88)
    rl1_1 = generate_random_wire(88)
    first_ADD.append(garbled_AND_fun(A0,A1,B0,B1,rl1_0,rl1_1))

    #second row
    rl2_0 = generate_random_wire(88)
    rl2_1 = generate_random_wire(88)
    first_ADD.append(garbled_XOR_fun(rl0_0,rl0_1,Cin0,Cin1,rl2_0,rl2_1))

    rl3_0 = generate_random_wire(88)
    rl3_1 = generate_random_wire(88)
    first_ADD.append(garbled_AND_fun(rl0_0,rl0_1,Cin0,Cin1,rl3_0,rl3_1))

    #third row
    rl4_0 = generate_random_wire(88)
    rl4_1 = generate_random_wire(88)
    first_ADD.append(garbled_XOR_fun(rl3_0,rl3_1,rl1_0,rl1_1,rl4_0,rl4_1))

    return(rl2_0,rl2_1,rl4_0,rl4_1,first_ADD) 

def Final_STAGE(s2_0,s2_1,s3_0,s3_1,Cout3_0,Cout3_1):
    Final = []

    #first row
    f0_0 =generate_random_wire(88)
    f0_1 =generate_random_wire(88)
    Final.append(garbled_AND_fun(s2_0,s2_1,s3_0,s3_1,f0_0,f0_1))

    f1_0 =generate_random_wire(88)
    f1_1 =generate_random_wire(88)
    Final.append(garbled_XOR_fun(s2_0,s2_1,s3_0,s3_1,f1_0,f1_1))

    #second row
    f2_0 =generate_random_wire(88)
    f2_1 =generate_random_wire(88)
    Final.append(garbled_XOR_fun(f0_0,f0_1,f1_0,f1_1,f2_0,f2_1))

    #third row
    f3_0 =generate_random_wire(88)
    f3_1 =generate_random_wire(88)
    Final.append(garbled_AND_fun(f2_0,f2_1,Cout3_0,Cout3_1,f3_0,f3_1))

    f4_0 =generate_random_wire(88)
    f4_1 =generate_random_wire(88)
    Final.append(garbled_XOR_fun(f2_0,f2_1,Cout3_0,Cout3_1,f4_0,f4_1))

    #fourth row
    f5_0 =generate_random_wire(88)
    f5_1 =generate_random_wire(88)
    Final.append(garbled_XOR_fun(f3_0,f3_1,f4_0,f4_1,f5_0,f5_1))

    return(Final,f5_0,f5_1)

def OT(b,i,ma,mb):
    pka,pkb=Bob.senderOne_OT_Two(i,b)
    ca,cb=Alice.receiverOne_OT_Two(pka,pkb,ma,mb)
    # Alice.finalOT(i,j,ca,cb)
    if(b==1):
        return(Dec(Bob.SKs[i],cb))
    else:
        return(Dec(Bob.SKs[i],ca))
    
def bytes_to_bits(byte_sequence):
    bits = ""
    for byte in byte_sequence:
        binary_rep = bin(byte)[2:]  # Get the binary representation without the prefix '0b'
        padded_binary = binary_rep.zfill(8)  # Left-pad with zeros to get 8 bits
        bits += padded_binary
    return bits

def bits_to_bytes(bit_string):
    # Convert the NumPy array of bits to a regular Python string
    bit_string = ''.join(map(str, bit_string))

    # Pad the bit string with zeros to make its length a multiple of 8
    padding_needed = (8 - len(bit_string) % 8) % 8
    padded_bit_string = bit_string.zfill(len(bit_string) + padding_needed)

    # Split the padded bit string into chunks of 8 bits each
    chunks = [padded_bit_string[i:i+8] for i in range(0, len(padded_bit_string), 8)]

    # Convert each 8-bit chunk to an integer and then to bytes
    byte_sequence = bytes([int(chunk, 2) for chunk in chunks])

    return byte_sequence

def DEC_MUL_STAGE(arr,A0,A1,x0,x1):
    rl0=Bob.DEC(arr[0],A0,x0)
    rl1=Bob.DEC(arr[1],A1,x0)
    rl2=Bob.DEC(arr[2],A0,x1)
    rl3=Bob.DEC(arr[3],A1,x1)

    rl4=Bob.DEC(arr[4],rl1,rl2)
    rl5=Bob.DEC(arr[5],rl1,rl2)

    rl6=Bob.DEC(arr[6],rl3,rl5)
    rl7=Bob.DEC(arr[7],rl3,rl5)
    return (rl0,rl4,rl7,rl6)

def DEC_ADDER_STAGE(arr,A,B,Cin):
    rl0=Bob.DEC(arr[0],A,B)
    rl1=Bob.DEC(arr[1],A,B)

    rl2=Bob.DEC(arr[2],rl0,Cin)
    rl3=Bob.DEC(arr[3],rl0,Cin)

    rl4=Bob.DEC(arr[4],rl3,rl1)
    return(rl2,rl4,)

def DEC_Final_STAGE(arr,s2,s3,Cout3):
    f0=Bob.DEC(arr[0],s2,s3)
    f1=Bob.DEC(arr[1],s2,s3)

    f2=Bob.DEC(arr[2],f0,f1)

    f3=Bob.DEC(arr[3],f2,Cout3)
    f4=Bob.DEC(arr[4],f2,Cout3)

    f5=Bob.DEC(arr[5],f3,f4)
    return(f5)


########################## MAIN ##########################

aa=int(input ("Enter alice's a1 in range (0-3):"))
ab=int(input ("Enter alice's a2 in range (0-3):"))
xa=int(input ("Enter bob's x1 in range (0-3):"))
xb=int(input ("Enter bob's x2 in range (0-3):"))

Alice.Init(aa,ab)
Bob.Init(xa,xb)

print(f'\n Alice`s view \n')

print(f'Alice garbeling the circuit:')

#  now we will let Alice garbel the circuit 

#MUL stage 
#A00 A10 X00 X10 is on the left the the rest on the other side...
ac0_0,ac0_1,ac1_0,ac1_1,ac2_0,ac2_1,ac3_0,ac3_1,first_MUL = MUL_STAGE(Alice.wire_label_A00_0,Alice.wire_label_A00_1,Alice.wire_label_A10_0,Alice.wire_label_A10_1,Alice.wire_label_x00_0,Alice.wire_label_x00_1,Alice.wire_label_x10_0,Alice.wire_label_x10_1)
bc0_0,bc0_1,bc1_0,bc1_1,bc2_0,bc2_1,bc3_0,bc3_1,second_MUL = MUL_STAGE(Alice.wire_label_A01_0,Alice.wire_label_A01_1,Alice.wire_label_A11_0,Alice.wire_label_A11_1,Alice.wire_label_x01_0,Alice.wire_label_x01_1,Alice.wire_label_x11_0,Alice.wire_label_x11_1)

s0_0,s0_1,Cout0_0,Cout0_1,Zero_ADD = ADDER_STAGE(ac0_0,ac0_1,bc0_0,bc0_1,Alice.Cin0_0,Alice.Cin0_1)
s1_0,s1_1,Cout1_0,Cout1_1,First_ADD = ADDER_STAGE(ac1_0,ac1_1,bc1_0,bc1_1,Cout0_0,Cout0_1)
s2_0,s2_1,Cout2_0,Cout2_1,Second_ADD = ADDER_STAGE(ac2_0,ac2_1,bc2_0,bc2_1,Cout1_0,Cout1_1)
s3_0,s3_1,Cout3_0,Cout3_1,Third_ADD = ADDER_STAGE(ac3_0,ac3_1,bc3_0,bc3_1,Cout2_0,Cout2_1)

#And the final stage...
Final_arr,FINAL0,FINAL1 = Final_STAGE(s2_0,s2_1,s3_0,s3_1,Cout3_0,Cout3_1)
#here we have these array to send them first_MUL,second_MUL,Zero_ADD,First_ADD,Second_ADD,Third_ADD and Final_arr

print("\nfirst_MUL\n",first_MUL,"\nsecond_MUL\n",second_MUL,"\nZero_ADD\n",Zero_ADD,"\nFirst_ADD\n",First_ADD,"\nSecond_ADD\n",Second_ADD,"\nThird_ADD\n",Third_ADD,"\nFinal_arr\n",Final_arr,"\n")
print("Alice finished garbeling the circuit\n")

# now alice will send her values to Bob using OT
print("Alice sending the right wires according to the values of a1,a2\n")
Alice.Sending_vars()

#Here alice sends to bob the x1 x2 using OT
mybits0_0=bytes_to_bits(Alice.wire_label_x00_0)
mybits0_1=bytes_to_bits(Alice.wire_label_x00_1)

mybits1_0=bytes_to_bits(Alice.wire_label_x10_0)
mybits1_1=bytes_to_bits(Alice.wire_label_x10_1)

mybits2_0=bytes_to_bits(Alice.wire_label_x01_0)
mybits2_1=bytes_to_bits(Alice.wire_label_x01_1)

mybits3_0=bytes_to_bits(Alice.wire_label_x11_0)
mybits3_1=bytes_to_bits(Alice.wire_label_x11_1)

bwire_label_x00 = np.empty(len(mybits0_0), dtype=int)
bwire_label_x10 = np.empty(len(mybits1_0), dtype=int)
bwire_label_x01 = np.empty(len(mybits2_0), dtype=int)
bwire_label_x11 = np.empty(len(mybits3_0), dtype=int)

for idx, bit in enumerate(mybits0_0):
    i=0
    bwire_label_x00[idx] = OT(Bob.xa[0], i, int(mybits0_0[idx]), int(mybits0_1[idx]))

for idx, bit in enumerate(mybits1_0):
    i=1
    bwire_label_x10[idx] = OT(Bob.xa[1], i, int(mybits1_0[idx]), int(mybits1_1[idx]))

for idx, bit in enumerate(mybits2_0):
    i=2
    bwire_label_x01[idx] = OT(Bob.xb[0], i, int(mybits2_0[idx]), int(mybits2_1[idx]))

for idx, bit in enumerate(mybits3_0):
    i=3
    bwire_label_x11[idx] = OT(Bob.xb[1], i, int(mybits3_0[idx]), int(mybits3_1[idx]))

Bob.wire_label_x00=bits_to_bytes(bwire_label_x00)
Bob.wire_label_x10=bits_to_bytes(bwire_label_x10)
Bob.wire_label_x01=bits_to_bytes(bwire_label_x01)
Bob.wire_label_x11=bits_to_bytes(bwire_label_x11)

print("Alice sent the labels to Bob using OT.")

print("\nBob's view\n")

print("Bob's wire labels:")
print("X0[0]",Bob.wire_label_x00)
print("X0[1]",Bob.wire_label_x10)
print("X1[0]",Bob.wire_label_x01)
print("X1[1]",Bob.wire_label_x11)
print("A0[0]",Bob.wire_label_A00)
print("A0[1]",Bob.wire_label_A10)
print("A1[0]",Bob.wire_label_A01)
print("A1[1]",Bob.wire_label_A11,"\n")

print("Now Bob will start to decrypt the cuircut\n")

#well dec. in order first_MUL,second_MUL
#Zero_ADD,First_ADD,Second_ADD,Third_ADD,Final_arr    

ac0,ac1,ac2,ac3=DEC_MUL_STAGE(first_MUL,Bob.wire_label_A00,Bob.wire_label_A10,Bob.wire_label_x00,Bob.wire_label_x10)
bc0,bc1,bc2,bc3=DEC_MUL_STAGE(second_MUL,Bob.wire_label_A01,Bob.wire_label_A11,Bob.wire_label_x01,Bob.wire_label_x11)
s0,Cout0=DEC_ADDER_STAGE(Zero_ADD,ac0,bc0,Bob.Cin0_0)
s1,Cout1=DEC_ADDER_STAGE(First_ADD,ac1,bc1,Cout0)
s2,Cout2=DEC_ADDER_STAGE(Second_ADD,ac2,bc2,Cout1)
s3,Cout3=DEC_ADDER_STAGE(Third_ADD,ac3,bc3,Cout2)
FINAL_RES=DEC_Final_STAGE(Final_arr,s2,s3,Cout3)

print(FINAL_RES)
# print(FINAL0)
# print(FINAL1)
if(FINAL_RES==FINAL0):
    print("So the rsult is 0")
elif(FINAL_RES==FINAL1):
    print("So the rsult is 1")

