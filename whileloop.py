## Make a program to find Hcf of 2 no.

c = 12576
d = 4052
r = c % d
while r != 0:
    q = c // d
    c = d
    d = r
    r = c % d
print(d)

