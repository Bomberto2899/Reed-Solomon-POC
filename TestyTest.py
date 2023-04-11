### Reed Solomon Algorithm ###
  #         maybe          #
from mod import Mod
import random 
from s1 import s1
from s2 import s2


# Funny math here

x = Mod(5, 7)      # x ≡ 5 (mod 7)

(x + 2) == 0       # True: 5 + 2 ≡ 7 ≡ 0 (mod 7)
(x + 7) == x       # True: 5 + 7 ≡ 12 ≡ 5 (mod 7)
(x**3) == (x + 1)  # True: 5³ ≡ 125 ≡ 6 (mod 7)
(1 // x) == 3      # True: 5 × 3 ≡ 15 ≡ 1 (mod 7) ⇒ 5⁻¹ ≡ 3 (mod 7)

#test: 

# values = [random.randint(-100, 100) for i in range(15)] 
# print(values)
# modValues = [Mod(value, 103) for  value in values]
# print([i._value for i in modValues])
# print(len(values) - len(modValues))
symbols = ".,!?#$%&/()[]=@£;:`*'-\""
text1 = ""
text2 = ""

for e in s1:
    if e not in symbols:
        text1 += e

for e in s2:
    if e not in symbols:
        text2 += e


list1 = text1.split()
list2 = text2.split()

index = {}
for counter, e in enumerate("abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"):
    index[e] = counter+1

#print(index)

def constructUniqueNumber(s : str):
  resultingNumber = 0
  for counter, e in enumerate(s):
     resultingNumber += index[e]*51**counter
  return resultingNumber


# print(constructUniqueNumber("Hi"), 34+9*51)

func1 = [constructUniqueNumber(i) for i in list1]
func2 = [constructUniqueNumber(i) for i in list2]

print(func1 == func2)
print(func1)
