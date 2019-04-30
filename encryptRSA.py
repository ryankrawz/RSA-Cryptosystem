# RSA Cryptosystem (Public Key Approach)
# Ryan Krawczyk


# Performs modular exponentiation by divide and conquer
def modExp(b, p, n):
    if p == 0: return 1
    halfway = modExp(b, p//2, n) % n
    return (halfway**2 * b**(p%2)) % n


# Converts string to base 256 number using ASCII code
def codeText(s):
    if len(s) == 0: return 0
    return 256 * codeText(s[:-1]) + ord(s[-1])


# Converts base 256 number to string using ASCII code
def decode(n):
    if n == 0: return ""
    return decode(n // 256) + chr(n % 256)


def main():
    p = long(raw_input("\nEnter p: "))
    q = long(raw_input("Enter q: "))
    e = long(raw_input("Enter e: "))
    d = long(raw_input("Enter d: "))
    n = p * q
    print("\nN = p * q = " + str(n))
    print("(d * e) % ((p - 1) * (q - 1)) = " + str((d*e)%((p-1)*(q-1))))
    s = raw_input("\nEnter a string for the encryption: ")
    coded = codeText(s)
    encr = modExp(coded, e, n)
    decr = modExp(encr, d, n)
    result = decode(decr)
    print("\n----------------------------")
    print("\nCoding:")
    print(s + " --> " + str(coded))
    print("\nEncryption:")
    print(str(coded) + " ^ e (mod N) = " + str(encr))
    print("\nDecryption:")
    print(str(encr) + " ^ d (mod N) = " + str(decr))
    print("\nDecoding:")
    print(str(decr) + " --> " + result + "\n")


main()
