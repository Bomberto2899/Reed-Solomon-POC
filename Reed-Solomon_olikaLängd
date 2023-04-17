from reedsolo import RSCodec, ReedSolomonError
import hashlib
from s1 import s1
from s2 import s2


extraPunkter = 10

rsc = RSCodec(extraPunkter)  # 10 ecc symbols

RS = rsc.encode(bytes(s1, 'ascii'))
Hash = hashlib.sha256(str(s1).encode())

RSend = RS[:245]



print(RSend)

#print('Vad som ska lagras: Hash: ' + str(Hash.hexdigest()) + ' Extra punkter: ' + str([e for e in RSend]) )