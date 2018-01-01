import crypt
from Crypto.Cipher import AES
import string
import random
from time import time

total_encryption_algorithm_time = 0
total_encryption_library_time = 0

total_decryption_algorithm_time = 0
total_decryption_library_time = 0

encrypt_correct = 0
decrypt_correct = 0

tries = 1000

for i in range(0, tries):
    key = ''.join([random.choice(string.ascii_letters + string.digits) for n in range(16)])
    text = ''.join([random.choice(string.ascii_letters + string.digits) for n in range(16)])

    myAes = crypt.Aes.parse_text(text, key)
    aes = AES.new(bytes(key, 'utf-8'), AES.MODE_ECB)

    before = time()
    myAes.encrypt()
    after = time()
    total_encryption_algorithm_time += (after - before)

    before = time()
    encrypted_text = aes.encrypt(bytes(text, 'utf-8'))
    after = time()
    total_encryption_library_time += (after - before)

    if ''.join(myAes.message) == encrypted_text.hex():
        encrypt_correct += 1

    before = time()
    myAes.decrypt()
    after = time()
    total_decryption_algorithm_time += (after - before)

    before = time()
    decrypted_text = aes.decrypt(encrypted_text)
    after = time()
    total_decryption_library_time += (after - before)

    if ''.join(myAes.message) == decrypted_text.decode("utf-8"):
        decrypt_correct += 1

print('Algorithm Average Encryption Time:', total_encryption_algorithm_time / tries)
print('Library Average Encryption Time:', format(total_encryption_library_time / tries, '.20f'))

print("-" * 100)

print('Algorithm Average Decryption Time:', total_decryption_algorithm_time / tries)
print('Library Average Decryption Time:', format(total_decryption_library_time / tries, '.20f'))

print("-" * 100)

print(str(encrypt_correct), 'correct encryptions out of', str(tries), 'tries')

print(str(decrypt_correct), 'correct decryptions out of', str(tries), 'tries')
