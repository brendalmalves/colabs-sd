from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
import csv
import binascii

secret_key = bytes.fromhex('afc70a3cd0a818c0a00217dac82ec008')
nonce = bytes.fromhex('52f5eda6606c7c239930007f8bf1b18f')
cipher = Cipher(algorithms.Camellia(secret_key), modes.CTR(nonce))

def decryption(cipher_text):
    decryptor = cipher.decryptor()
    return decryptor.update(bytes.fromhex(cipher_text)) + decryptor.finalize()

def encryption(plan_text):
    encryptor = cipher.encryptor()
    return encryptor.update(plan_text) + encryptor.finalize()

columns_sum = []
with open('./119111113.csv', 'r') as file:
    csv_reader = csv.reader(file)
    for row in csv_reader:
        column_one = decryption(row[0])
        column_two =  decryption(row[1])
        columns_sum.append(int.from_bytes(column_one, byteorder='big') + int.from_bytes(column_two, byteorder='big'))

with open('./119111113_result.csv', 'w') as file:
    for value in columns_sum:
        encrypt_value = encryption(int(value).to_bytes(2, byteorder='big'))
        writer = csv.writer(file)
        result =  binascii.hexlify(encrypt_value)
        writer.writerow([result.decode()])