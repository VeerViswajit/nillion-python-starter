from nada_dsl import *

def nada_main():
    party1 = Party(name="Party1")
    my_int1 = SecretInteger(Input(name="my_int1", party=party1))
    my_int2 = SecretInteger(Input(name="my_int2", party=party1))

    r = my_int1 * my_int2
    r3 = my_int1 / my_int2
    r_mod = my_int1 % my_int2  # Modulo operation

    # Function to find the maximum of two numbers
    def max(a: SecretInteger, b: SecretInteger) -> SecretInteger:
        return (a < b).if_else(b, a)

    # Function to find the minimum of two numbers
    def min(a: SecretInteger, b: SecretInteger) -> SecretInteger:
        return (a < b).if_else(a, b)

    r1 = max(my_int1, my_int2)
    r6 = min(my_int1, my_int2)
    r5 = Integer(0)

    out1 = Output(r1, "Maximum of two Numbers", party1)
    out2 = Output(r, "Multiplication of Two Numbers", party1)
    out3 = Output(r3, "Division of Two Numbers", party1)
    out4 = Output(r6, "Minimum of two Numbers", party1)
    out5 = Output(r_mod, "Modulo of Two Numbers", party1)
    out6 = Output(r5, "Welcome to Hacker House GOA", party1)

    return [out1, out2, out3, out4, out5, out6]
