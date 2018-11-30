import hashlib

print("###################### 1 ######################")
print(hashlib.algorithms_guaranteed)

"""
output:
    {'sha3_384', 'blake2b', 'blake2s', 'sha384', 'md5', 'sha224', 'sha3_256', 'sha3_512', 'sha3_224', 'shake_128', 'sha512', 'shake_256', 'sha1', 'sha256'}
"""


print("###################### 2 ######################")
print(hashlib.algorithms_available)

"""
output:
    {'SHA256', 'blake2s', 'sha384', 'whirlpool', 'MD4', 'sha224', 'MD5-SHA1', 'sha3_512', 'sha512', 'sha1', 'sha256', 'md5-sha1', 'sha3_384', 'RIPEMD160', 'BLAKE2s256', 'sha3_224', 'SHA224', 'SHA512', 'blake2s256', 'SHA1', 'blake2b512', 'shake_256', 'md4', 'MD5', 'SHA384', 'blake2b', 'md5', 'BLAKE2b512', 'sha3_256', 'shake_128', 'ripemd160'}
"""


print("###################### 3 ######################")
print(hashlib.sha1().digest_size)
print(hashlib.sha256().digest_size)
print(hashlib.sha3_512().digest_size)

"""
output:
    20
    32
    64
"""


print("###################### 4 ######################")
print(hashlib.sha1().block_size)
print(hashlib.sha256().block_size)
print(hashlib.sha3_512().block_size)

"""
output:
    64
    64
    72
"""


print("###################### 5 ######################")
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


print("###################### 6 ######################")
print(hashlib.sha1(("Hello world!!").encode('utf-8')).hexdigest())

"""
output:
    a59b02741bff27a4c3e236332f29aa604c723e85
"""


print("###################### 7 ######################")
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
