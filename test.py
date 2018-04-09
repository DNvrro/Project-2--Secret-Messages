

def affine(a, b):
    for i in range(26):
        print((chr(i + 65)) + " : " + chr(((a*i+b)%26)+65))

affine(5, 8)