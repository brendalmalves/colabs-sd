from argon2 import PasswordHasher
from argon2.exceptions import HashingError 
from argon2.exceptions import VerifyMismatchError, InvalidHash, VerificationError

ph = PasswordHasher()

try:
    hash = ph.hash("119111113")
except HashingError as err:
    print(err)

print(hash)

try:
    ph.verify(hash, input("Qual a senha? "))
    print("senha correta")
except VerifyMismatchError as err:
    print(err)
except InvalidHash as err:
    print(err)
except VerificationError as err:
    print(err)