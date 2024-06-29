from nada_dsl import *


def nada_main():
    party1 = Party(name="Party1")
    my_int1 = SecretInteger(Input(name="my_int1", party=party1))
    my_int2 = SecretInteger(Input(name="my_int2", party=party1))
    
    r=my_int1+my_int2
    r2=my_int1-my_int2
    # write the computation for your program here - use my_int1 and my_int2 as inputs
    # make sure you change the output below to be your new output
    out1=Output(r,"addtion",party1)
    out2=Output(r2,"subdtraction",party1)
    r3=my_int1-Integer(496)
    r4=my_int2-Integer(1)
    r5=Integer(0)
    out3=Output(r3,"Start Date: ",party1)
    out4=Output(r4,"End Date: ",party1)
    out5=Output(r5,"Welcome to Hacker House 2024 GOA",party1)
    return [out1,out2,out3,out4,out5]