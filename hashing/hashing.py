import hashlib

with open('hashing.txt', 'w') as file:
  file.write("Esse arquivo é para mostrar um exemplo na cadeira de sistemas distribuídos.")

with open('hashing.txt', 'rb') as file:
  hash_file = hashlib.sha256(file.read())

with open('hashing/hashing.py', 'rb') as file:
  hash_own_file = hashlib.sha256(file.read())

print(hash_file.hexdigest())
print(hash_own_file.hexdigest())




