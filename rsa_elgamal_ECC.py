import math
import random

def rsa_menu():
    print(f" RSA ".center(50,'-'))
    n = 221
    e = 5

    for i in range (2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            p, q = i, n // i
            break

    phi = (p - 1) * (q - 1)
    d = pow(e, -1, phi)

    print(f" Step A: Finding d in RSA ".center(25,'*'))
    print(f"Selected Factors: n = 221 and e = 5")
    print(f"Discovered Prime Factors: p = {p}, q = {q}")
    print(f"Private Key: d = {d}\n")

    message = "HOW ARE YOU"

    ptext = [26 if ch == " " else ord(ch) - ord("A") for ch in message]

    ctext = [pow(P, e, n) for P in ptext]

    print(" Step B: Message Encryption ".center(25,'*'))
    for ch, P, C in zip(message, ptext, ctext):
        label = "SPACE" if ch == " " else ch
        print(f" {label:<5} -> P = {P:02d} -> C = {C}")

    print(f"Ciphertext list: {ctext}")


def elgamal():
    print(f" Elgamal/Diffie-Hellman ".center(50,'-'))
    print(f" Step A: e2 Elgamal Calculator ".center(25,'*'))
    p = 31
    print(f" Key Generation ")
    print(" Step 1: Finding Primitive Root (e1) ")

    e1 = None
    for candidate in range(2, p):
        modulo = [pow(candidate, k, p) for k in range(1, p)]
        unique_count = len(set(modulo))
        print(f" Testing candidate {candidate}; which generates {unique_count}/{p - 1} unique values -> {modulo[:6]}...")

    if unique_count == p - 1:
        e1 = candidate
        print(f" Candidate {e1} is the smallest primitive root modulo {p}... ")
        break

    print(" Step 2: Choosing the Private Key (d) ")
    d = 10
    e2 = pow(e1, d, p)

    print(f"")
# def main():

#     print("Please select an option from the menu below...")
#     print("1. RSA")
#     print("2. Elgamal/Diffie-Hellman")
#     print("3. ECC")
#     print("4. Exit")
#     menu_select = input("Please enter 1, 2, 3, or 4: ")


