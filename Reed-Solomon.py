# Initialization
from reedsolo import RSCodec, ReedSolomonError
import hashlib
from s1 import s1
from s2 import s2

extraPunkter = 10

rsc = RSCodec(extraPunkter, nsize=4095)  # 10 ecc symbols

RS = rsc.encode(s1)
Hash = hashlib.sha256(str(s1).encode())

RSend = RS[-extraPunkter:]


print('Vad som ska lagras: Hash: ' + str(Hash.hexdigest()) + ' Extra punkter: ' + str([e for e in RSend]) )

#print(''.join(chr(i) for i in RS))
#RSend = ''.join(chr(i) for i in RSend)

rscS2 = RSCodec(0, nsize=4095)

s2RS = rscS2.encode(s2)
s2RS.extend(RSend)


#s2RS = s2.join(RSend)
try:
    mes, mesWithECC, errpos = rsc.decode(s2RS)
    mes = ''.join(chr(i) for i in mes)

    Hash2 = hashlib.sha256(str(mes).encode())

    if Hash.hexdigest() == Hash2.hexdigest():
        print("position of errors are: " + str([e for e in errpos]))
    else:
        print("To much error")
except:
    print("To much error")
