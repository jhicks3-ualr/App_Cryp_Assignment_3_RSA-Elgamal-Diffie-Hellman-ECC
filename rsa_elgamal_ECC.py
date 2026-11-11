import math

def rsa_menu():
    n = 221
    e = 5

    for i in range (2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            p, q = i, n // i
            break

    phi = (p - 1) * (q - 1)
    d = pow(e, -1, phi)

    print(f" Finding d in RSA ".center(100,'-'))
    print(f"Selected Factors: n = 221 and e = 5")
    print(f"Discovered Prime Factors: p = {p}, q = {q}")
    print(f"Private Key: d = {d}\n")

    message = "HOW ARE YOU"

    ptext = [26 if ch == " " else ord(ch) - ord("A") for ch in message]

    ctext = [pow(P, e, n) for P in ptext]

    print(" Message Encryption ".center(100,'-'))
    for ch, P, C in zip(message, plaintext_blocks, ciphertext_blocks):
        label = "SPACE" if ch == " " else ch
        print(f" {label:<5} -> P = {P:02d} -> C = {C}")

    print(f"Ciphertext list: {ctext}")


# def main():

#     print("Please select an option from the menu below...")
#     print("1. RSA")
#     print("2. Elgamal/Diffie-Hellman")
#     print("3. ECC")
#     print("4. Exit")
#     menu_select = input("Please enter 1, 2, 3, or 4: ")

rsa_menu()
