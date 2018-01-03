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

```
text = 'Two One Nine Two'
key = 'Thats my Kung Fu'
```
```
cipher = crypt.Aes.parse_text (text, key) # Constructor.
```
```
encrypted_text = cipher.encrypt() # Byte list of encrypted message.
```
```
decrypted_text = cipher.decrypt()# String of decrypted original message.
```
