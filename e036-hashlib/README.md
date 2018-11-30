# hashlib

- In any project for the storage of data of a user, one or several hashing algorithms must be used to protect certain information.
- Hashlib allows hashing with the algorithms SHA1, SHA224, SHA256, SHA384, SHA512 and MD5.


### constant

##### algorithms_guaranteed

- A set containing the names of the hash algorithms guaranteed to be supported by this module on all platforms. Note that ‘md5’ is in this list despite some upstream vendors offering an odd “FIPS compliant” Python build that excludes it.

```
print(hashlib.algorithms_guaranteed)

"""
output:
    {'sha3_384', 'blake2b', 'blake2s', 'sha384', 'md5', 'sha224', 'sha3_256', 'sha3_512', 'sha3_224', 'shake_128', 'sha512', 'shake_256', 'sha1', 'sha256'}
"""
```

##### algorithms_available

- A set containing the names of the hash algorithms that are available in the running Python interpreter. These names will be recognized when passed to new(). algorithms_guaranteed will always be a subset. The same algorithm may appear multiple times in this set under different names (thanks to OpenSSL).

```
print(hashlib.algorithms_available)

"""
output:
    {'SHA256', 'blake2s', 'sha384', 'whirlpool', 'MD4', 'sha224', 'MD5-SHA1', 'sha3_512', 'sha512', 'sha1', 'sha256', 'md5-sha1', 'sha3_384', 'RIPEMD160', 'BLAKE2s256', 'sha3_224', 'SHA224', 'SHA512', 'blake2s256', 'SHA1', 'blake2b512', 'shake_256', 'md4', 'MD5', 'SHA384', 'blake2b', 'md5', 'BLAKE2b512', 'sha3_256', 'shake_128', 'ripemd160'}
"""
```

##### digest_size

- The size of the resulting hash in bytes.

```
print(hashlib.sha1().digest_size)
print(hashlib.sha256().digest_size)
print(hashlib.sha3_512().digest_size)

"""
output:
    20
    32
    64
"""
```

##### block_size

- The internal block size of the hash algorithm in bytes.

```
print(hashlib.sha1().block_size)
print(hashlib.sha256().block_size)
print(hashlib.sha3_512().block_size)

"""
output:
    64
    64
    72
"""
```


### methods

##### update(data)

- Update the hash object with the bytes-like object. Repeated calls are equivalent to a single call with the concatenation of all the arguments: m.update(a); m.update(b) is equivalent to m.update(a+b).
- Changed in version 3.1: The Python GIL is released to allow other threads to run while hash updates on data larger than 2047 bytes is taking place when using hash algorithms supplied by OpenSSL.

##### digest()

-Return the digest of the data passed to the update() method so far. This is a bytes object of size digest_size which may contain bytes in the whole range from 0 to 255.

##### hexdigest()

- Like digest() except the digest is returned as a string object of double length, containing only hexadecimal digits. This may be used to exchange the value safely in email or other non-binary environments.

##### copy()

- Return a copy (“clone”) of the hash object. This can be used to efficiently compute the digests of data sharing a common initial substring.


### SHAKE variable length digests

- The shake_128() and shake_256() algorithms provide variable length digests with length_in_bits//2 up to 128 or 256 bits of security. As such, their digest methods require a length. Maximum length is not limited by the SHAKE algorithm.

```
for algorithm in hashlib.algorithms_guaranteed:
    print("Algorithm name:", algorithm)
    my_hash = hashlib.new(algorithm)
    my_hash.update(b"Hello world!!")
    if algorithm != "shake_128" and algorithm != "shake_256":
        print(my_hash.hexdigest())

"""
output:
    Algorithm name: sha3_512
    19b6e4f6a60af2188dfca1fd022cab12f2f6cc32ce2ebfdf340c2fb56bb555299e16117f123b6e0d7b996b4730ccf9208ebe12b28f80e3f98f3a20d392a0ecb0
    Algorithm name: sha3_256
    e5f75033441bbb88188df76f2805fe0fb3e9aea71d0ad2acd95fcf60927270b9
    Algorithm name: shake_256
    Algorithm name: sha224
    1f0271763e49e3316ae82074f1b113a0d29a6f2ec61b7b4369d6f2ed
    Algorithm name: sha512
    bd459c27b064aa5a528e0e6bac88d601cc25068d8cf9324cc684b8622a475cc3a1deb183ddb91aa7a7a30d6a40408a77142825796f928458e0dcb03748b23236
    Algorithm name: sha3_224
    73343cab6866560869c99144a3c22a4d17365a344d223baa43d80f90
    Algorithm name: sha1
    a59b02741bff27a4c3e236332f29aa604c723e85
    Algorithm name: blake2s
    00e46a62a1d9a32453e3c7c46228a6ca0b9a025d8ee800c8bd178616811446b5
    Algorithm name: shake_128
    Algorithm name: md5
    1d94dd7dfd050410185a535b9575e184
    Algorithm name: blake2b
    318d71f8b0bd6babf2917a4bf60ec9cc4dac3a35b12f10c0c57b2d1833031d97df8c9bbd387ca4d15a10c2114fe8ada55d4db2f915ba0fb327e549e8c9b8a4fb
    Algorithm name: sha384
    7fdcf502174d61601491925e77f46ca56816f4f8889e242b98d3a6f51535738bafc00ef80258984e8c22e459a9b49a6e
    Algorithm name: sha3_384
    92f9b2bb820c5526be5766a5155aac67cd58946450115e8ae5b7840c4be0ff48667f9c6adc17a1101bbfa4b9a69816ff
    Algorithm name: sha256
    bbca77170621e018f9b8d17c850d2c7efe3cf9998cf741edf8e7dffbaeeb160e
"""
```


### Examples:

```
my_hash = hashlib.sha1()
my_hash.update(("Hello world!!").encode('utf-8'))
# -------- or --------
# my_hash.update(b"Hello world!!")
print(my_hash.digest())
print(my_hash.hexdigest())

"""
output:
    b"\xa5\x9b\x02t\x1b\xff'\xa4\xc3\xe263/)\xaa`Lr>\x85"
    a59b02741bff27a4c3e236332f29aa604c723e85
"""
```

##### More condensed

```
print(hashlib.sha1(("Hello world!!").encode('utf-8')).hexdigest())

"""
output:
    a59b02741bff27a4c3e236332f29aa604c723e85
"""
```


### Oficial documentation:

- https://docs.python.org/3/library/hashlib.html



