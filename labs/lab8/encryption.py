def encode(s,k):
    acc = ''
    for c in s:
        i = ord(c)
        x = k + i
        c = (chr(x))
        acc = acc + c
    return acc

def encode_better(s, k):
    acc = ''
    for i in range(len(s)):
        c = s[i]
        key = k[i % len(k)]
        c = ord(c)
        key = ord(key) - 97
        x = key + c
        x = chr(x)
        acc = acc + x
    return acc