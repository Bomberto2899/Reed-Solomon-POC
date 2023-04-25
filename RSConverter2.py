from s1 import s1

def converter(s):
    s = s.split('\n')
    i = 0
    while i < len(s):
        if s[i] == '':
            print(s.pop(i))
        i += 1
    for e in s:
        index = ord(e[4]) + ord(e[-4]) - 61*2
        print(index)
        print(e)

    return s


converter(s1)