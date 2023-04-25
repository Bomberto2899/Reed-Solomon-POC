# Initialization
from reedsolo import RSCodec, ReedSolomonError
import hashlib
from s1 import s1
from s2 import s2
from ReedSolomonOlikaLangdConverterare import converter

extraPunkter = int(len(s1)/2)
s1 = converter(s1)
s2 = converter(s2)
print(len(s1))
i = 0
while 2**i-1 < len(s1):
    i += 1
bigNumber = 2**i-1

print(extraPunkter)
rsc = RSCodec(extraPunkter, nsize=bigNumber)  # 10 ecc symbols

RS = rsc.encode(s1)
Hash = hashlib.sha256(str(s1).encode())

RSend = RS[-extraPunkter:]


print('Vad som ska lagras: Hash: ' + str(Hash.hexdigest()) + ' Extra punkter: ' + str([e for e in RSend]) )

#print(''.join(chr(i) for i in RS))
#RSend = ''.join(chr(i) for i in RSend)

#stupid way to make correct array =)
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
        print("To much error1")
except:
    print("To much error2")
