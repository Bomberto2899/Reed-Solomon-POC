def converter(s):
    j = 0
    i = 0
    while i < len(s):
        if(s[i] == '\n'):
            s = s[:i] + ' '*(1000 - j) + s[i:]
            i += (1000 - j)
            j = 0
            print("yo")
        if j > 1000:
            print("Yo, wtf")
        j += 1
        i += 1

    # print(s)
    # i = 0
    # while(i < len(s)):
    #     print(s[i])
    #     i+=1000
    return s