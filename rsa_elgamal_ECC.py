import math
import random

def rsa_menu():
    print(f" RSA ".center(50,'='))
    n = 221
    e = 5

    for i in range (2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            p, q = i, n // i
            break

    phi = (p - 1) * (q - 1)
    d = pow(e, -1, phi)

    print(f" Step A: Finding d in RSA ".center(50,'*'))
    print(f"Selected Factors: n = 221 and e = 5")
    print(f"Discovered Prime Factors: p = {p}, q = {q}")
    print(f"Private Key: d = {d}\n")

    message = "HOW ARE YOU"

    ptext = [26 if ch == " " else ord(ch) - ord("A") for ch in message]

    ctext = [pow(P, e, n) for P in ptext]

    print(" Step B: Message Encryption ".center(50,'*'))
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

def ecc_curve():
    print(f" Elliptic Curve Cryptography (ECC) ".center(50,'='))
    print(f" Curve Parameters ".center(50,'*'))

    curve_notation = "E67(2, 3)"
    p = 67
    a = 2
    b = 3
    print(f" Step 1: Extracting Parameteres from Curve {curve_notation}")
    print(f" Standard form: Ep(a, b) -> y^2 = x^3 + ax + b (mod p)")
    print(f" Given Elliptic Curve = y^2 = x^3 + 2x + 3")
    print(f" Therefore, p = 67, a = 2, b = 3")

    prime = all(p % i != 0 for i in range(2, int(math.sqrt(p)) + 1))
    discriminant = (4 * (a ** 3) + 27 * (b ** 2)) % p

    print(f" Step 2: Verifying Curve ")
    print(f" Prime Check (p = {p} > 3): {'Valid Prime' if prime and p > 3 else 'Invalid'}")
    print(f" Calculation: (4*{a}^3 + 27*{b}^2) mod {p} = {4*(a**3) + 27*(b**2)} mod {p} = {discriminant}")
    print(f" Status: {'Valid (Non-zero, curve has no sharp cusps or self-intersections)' if discriminant != 0 else 'Invalid'}\n")

def ecc_algorithm():
    print(f" Alice and Bob Messaging ".center(50,'='))
    p = 67
    a = 2
    b = 3

    def ecc_math(P1, P2=none, k=1)

    if k > 1 and P2 is None:
        result = None
        addend = P1
        while k > 0:
            if k & 1:
                result = ecc_math(result, addend)
            addend = ecc_math(addend, addend)
            k >>= 1
        return result
    
    if P1 is None:
        return P2
    if P2 is None:
        return P1

    x1, y1 = P1
    x2, y2 = P2

    if P1 == P2:
        numerator = (3 * (x1 ** 2) + a) % p
        denominator = pow(x2 - x1, -1, p)

    lam = (numerator * denominator) % p
    x3 = (lam ** 2 - x1 - x2) % p
    y3 = (lam * (x1 - x3) - y1) % p
    return (x3, y3)

print(f" Part A: Bob's Key ".center(50,'*'))
e1 = (2, 22)
d = 4
e2 = ecc_math(e1, k=d)
print(f" Generator Point (e1) = {e1}")
print(f" Bob's Private key (d) = {d}")
print(f" Bob's Public Key (e2 = d * e1) = {d} * {e1} = {e2}\n")


# def main():

#     print("Please select an option from the menu below...")
#     print("1. RSA")
#     print("2. Elgamal/Diffie-Hellman")
#     print("3. ECC")
#     print("4. Exit")
#     menu_select = input("Please enter 1, 2, 3, or 4: ")


elgamal()