import string

alphabet = string.ascii_uppercase
cyper = "WUYMULCMZCMBS"
op = []

for i in range(26):
    key = i
    temp = {}
    l = 0

    for j in range(i, len(alphabet)):
        temp[l] = alphabet[j]
        l += 1

    for k in range(0, i):
        temp[l] = alphabet[k]
        l += 1

    org = ""

    for o in cyper:
        for key, value in temp.items():  
            if value == o:
                org += chr(key + ord('a'))

    op.append(org.upper())
    temp.clear()
print(op)