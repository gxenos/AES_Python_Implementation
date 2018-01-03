# AES Python Implementation
A Python implementation of AES with 128 bits key.

## Installing

You only need Python 3.x

For test.py you need pycryptodome module. 
To install with pip:
```
pip install pycryptodome
```

## Usage Example

Define text and key:
```
text = 'Two One Nine Two'
key = 'Thats my Kung Fu'
```
To create the cipher object:
```
cipher = crypt.Aes.parse_text(text, key) # Constructor.
```
To encrypt:
```
cipher.encrypt() 
print(cipher.message) # Byte list of encrypted message.
```
To decrypt:
```
cipher.decrypt()
print(cipher.message) # String of decrypted original message.
```
