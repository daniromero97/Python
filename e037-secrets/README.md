# secrets

- The secrets module is used for generating cryptographically strong random numbers suitable for managing data such as passwords, account authentication, security tokens, and related secrets.
- In particularly, secrets should be used in preference to the default pseudo-random number generator in the random module, which is designed for modelling and simulation, not security or cryptography.


### Random numbers

##### choice(sequence)

- Return a randomly-chosen element from a non-empty sequence.

```
print(''.join(secrets.choice(string.ascii_letters) for i in range(8)))
print(''.join(secrets.choice(string.digits) for i in range(8)))
print(''.join(secrets.choice(string.ascii_letters + string.digits) for i in range(8)))

"""
output:
    mHwCaXyj
    57873877
    QSvum9D5
"""
```


##### randbelow(n)

- Return a random int in the range [0, n).

```
print(secrets.randbelow(100))
print(secrets.randbelow(100))
print(secrets.randbelow(100))


"""
output:
    43
    13
    14
"""
```


##### randbits(k)

- Return an int with k random bits.

```
print(secrets.randbits(10))
print(secrets.randbits(10))
print(secrets.randbits(10))


"""
output:
    636
    146
    171
"""
```


### Generating tokens

##### token_bytes([nbytes=None])

- Return a random byte string containing nbytes number of bytes. If nbytes is None or not supplied, a reasonable default is used.

```
print(secrets.token_bytes())
print(secrets.token_bytes(5))
print(secrets.token_bytes(10))


"""
output:
    b'%\xb4\xebO*\xde\xd5\xef\xca\x15\xf8\xceh\xf7\xa8,\xe4<\x9d\xbe\xd2,Cj\xf3@|\xc4\xba\x00\xcd\x05'
    b"\x84\x9e'<\xb0"
    b"\xd4\x9d'\x99^\x0cC\xffDn"
"""
```

##### token_hex([nbytes=None])

- Return a random text string, in hexadecimal. The string has nbytes random bytes, each byte converted to two hex digits. If nbytes is None or not supplied, a reasonable default is used.

```
print(secrets.token_hex())
print(secrets.token_hex(5))
print(secrets.token_hex(10))


"""
output:
    0bbf2bf2c3c33dfe0e3c6aea0cb78877d120bda5cf57e34707806c34269a1f6e
    114d5d9676
    58f8338979e0b926043a
"""
```

##### token_urlsafe([nbytes=None])

- Return a random URL-safe text string, containing nbytes random bytes. The text is Base64 encoded, so on average each byte results in approximately 1.3 characters. If nbytes is None or not supplied, a reasonable default is used.

```
print(secrets.token_urlsafe())
print(secrets.token_urlsafe(5))
print(secrets.token_urlsafe(10))


"""
output:
    pe1ePdY1EOjCwr73mHLiD2zPrAkdNcnfYvV1abFLEz4
    S5tS_Rg
    E0p5kfo0AX-Jow
"""
```







