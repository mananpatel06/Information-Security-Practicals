import random


def generate_key(msg):
    key = list()
    for i in range(len(msg)):
        key.append(random.randint(0, 25))
    return tuple(key)


def encrypt(msg, key):
    cipher_text = str()
    for i in range(len(msg)):
        cipher_text = cipher_text + chr(((ord(msg[i]) - ord('a')) + key[i]) % 26 + ord('a'))
    return cipher_text


def decrypt(cipher_text, key):
    msg = str()
    for i in range(len(cipher_text)):
        msg = msg + chr(((ord(cipher_text[i]) - ord('a')) - key[i]) % 26 + ord('a'))
    return msg


msg = input("Enter message to send : ")
key = generate_key(msg)

cipher_text = encrypt(msg, key)
print("\nEncrypted message : ", cipher_text)

decrypted = decrypt(cipher_text, key)
print("Decrypted message : ", decrypted)
print("\nKeys used : ", key)
    print("\nMade by: Manan Patel ")


