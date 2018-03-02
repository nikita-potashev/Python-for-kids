
date="15:06:1997"
date=date.replace(':', '')
mass=list(date)

for i, item in enumerate(mass):
    mass[i] = int(item)

summ=sum(mass)
alphabet = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"

print(summ)

def convert(num, to_base=10, from_base=10):

    if isinstance(num, str):
        n = int(num, from_base)
    else:
        n = int(num)
    if n < to_base:
        return alphabet[n]
    else:
        return convert(n // to_base, to_base) + alphabet[n % to_base]


print('oct - '+convert(summ,to_base=8,from_base=10))
print('hex - '+convert(summ,to_base=16,from_base=10))
print('32 - '+convert(summ,to_base=32,from_base=10))
