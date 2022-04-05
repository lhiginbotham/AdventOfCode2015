from hashlib import md5

key = 'iwrupvqb'

curVal = 0
while True:
    hash_val = md5((key + str(curVal)).encode('utf-8')).hexdigest()

    found = True
    for x in range(5):
        if hash_val[x] != '0':
            found = False
            break

    if found:
        break

    curVal += 1

print(curVal)
