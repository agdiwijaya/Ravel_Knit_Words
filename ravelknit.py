print("Ravelling")
print("=" * 50)

def ravel(n):
    hasil = ""
    for baris in range(len(n)):
        for kolom in range(baris + 1):
            hasil += n[kolom]
            hasil += ""
    hasil += ""
    return hasil

print(ravel('Purwadhika'))
print(ravel('Digital'))
print(ravel('Coding'))
print(ravel('School'))

print("=" * 50)
print("Knitting")
print("=" * 50)

def knit(n):
    a = n[0]
    b = n.split(a)
    hasil = a + b[-1]
    return hasil

print(knit('PPuPurPurwPurwaPurwadPurwadhPurwadhiPurwadhikPurwadhika'))
print(knit('DDiDigDigiDigitDigitaDigital'))
print(knit('CCoCodCodiCodinCoding'))
print(knit('SScSchSchoSchooSchool'))