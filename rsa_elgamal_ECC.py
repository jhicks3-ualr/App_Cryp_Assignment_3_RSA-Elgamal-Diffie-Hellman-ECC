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
    print(f" Elgamal/Diffie-Hellman ".center(50,'='))
    print(f" Part A: e2 Elgamal Calculator ".center(50,'*'))
    p = 31
    print(f" Key Generation ")
    print(" ***Step A.1: Finding Primitive Root (e1)*** ")

    e1 = None
    for candidate in range(2, p):
        modulo = [pow(candidate, k, p) for k in range(1, p)]
        unique_count = len(set(modulo))
        print(f" Testing candidate {candidate}; which generates {unique_count}/{p - 1} unique values -> {modulo[:6]}...")

        if unique_count == p - 1:
            e1 = candidate
            print(f" Candidate {e1} is the smallest primitive root modulo of {p}...\n")
            break

    print(" Step A.2: Choosing the Private Key (d) ")
    d = random.randint(2, p - 2)
    print(f" Valid range for d: 2 <= d <= 29 ")
    print(f" Randomly selected Private Key = {d}\n")

    print(" Step A.3: Calculating Public Key (e2) ")
    power = e1 ** d
    e2 = pow(e1, d, p)
    print(f" Formula: e2 = (e1^d) mod p")
    print(f" Calculation: ({e1}^{d}) mod {p} = {power} mod {p} = {e2}")
    print(f" Public Key (e1, e2, p) = {e1}, {e2}, {p}")
    print(f" Private Key (d) = {d}\n")

    print(f" Part B: Message Encryption ".center(50,'*'))

    message = "HELLO"

    ptext = [ord(ch) - ord("A") for ch in message]
    ctext_pairs = []

    for ch, P in zip(message, ptext):
        r = random.randint(2, p - 2)
        C1 = pow(e1, r, p)
        C2 = (P * pow(e2, r, p)) % p
        ctext_pairs.append((C1, C2))
        print(f" {ch} (P = {P:02d}) | r = {r:02d} -> C1 = {e1}^{r:02d} mod {p} = {C1:02d}, C2 = ({P:02d} * {e2}^{r:02d}) mod {p} = {C2:02d}")

    print(" ")
    print(f" Part C: Message Decryption ".center(50,'*'))
    decrypted_chars = []

    for (C1, C2) in ctext_pairs:
        s = pow(C1, d, p)
        s_inv = pow(s, -1, p)
        P_recovered = (C2 * s_inv) % p
        ch = chr(P_recovered + ord("A"))
        decrypted_chars.append(ch)
        print(f" (C1, C2) = ({C1:02d}, {C2:02d}) | s = {C1:02d}^{d:02d} mod {p} = {s:02d}, s^-1 = {s_inv:02d} -> P = ({C2:02d} * {s_inv:02d}) mod {p} = {P_recovered:02d} ({ch})")

    print(f" Recovered Message: {''.join(decrypted_chars)} ")

# def main():

#     print("Please select an option from the menu below...")
#     print("1. RSA")
#     print("2. Elgamal/Diffie-Hellman")
#     print("3. ECC")
#     print("4. Exit")
#     menu_select = input("Please enter 1, 2, 3, or 4: ")


elgamal()