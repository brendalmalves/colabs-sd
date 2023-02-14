from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
import csv

secret_key = bytes.fromhex('afc70a3cd0a818c0a00217dac82ec008')
nonce = bytes.fromhex('52f5eda6606c7c239930007f8bf1b18f')
cipher = Cipher(algorithms.Camellia(secret_key), modes.CTR(nonce))

decryptor = cipher.decryptor()
encryptor = cipher.encryptor()

def decryption(cipher_text):
    return decryptor.update(bytes.fromhex(cipher_text)).decode()

def encryption(plan_text):
    return encryptor.update(str(plan_text).encode()).hex()

columns_sum = []
with open('./119111113.csv') as file:
    csv_reader = csv.reader(file)
    for row in csv_reader:
        column_one =  int(decryption(row[0]))
        column_two =  int(decryption(row[1]))
        sum = column_one + column_two
        columns_sum.append(encryption(sum))

    encryptor.finalize()
    decryptor.finalize()


with open('./119111113_result.csv', 'w') as file:
    file.write("\n".join(columns_sum))
