import hashlib

print(hashlib.algorithms_available)

val = 'Ananthlakshmi'
res = val.encode()
print('primary hash value using sha512 algorithm :',hashlib.sha512(res).hexdigest())
print('secondary hash value using sha224 algorithm :' ,hashlib.sha224(res).hexdigest())
length =16
print('the third hash value using shake256 algorithm :' , hashlib.shake_256(res).hexdigest(length))

