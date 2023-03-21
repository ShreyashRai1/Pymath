## Make a program that prints all odd numbers from 1 -100

for i in range(1,100):
    if i%2 != 0:
        print(i)



## Make a program to print all pythagorean tiplets from 1-100

for i in range(2,101): # triplets of 1 dont exist
    x = 2*i    # 2m -: smallest pythagorean triplet
    y = i*i-1  # m^2-1 -: middle triplet
    z = i*i+1  # m^2+1 -: highest triplet

    if x >= 100:
        break
    if y >= 100:
        break
    if z >= 100:
        break
    else:
        print(x,y,z)
    print("---------------------------")



## Make a program to show weather 1-100 has more integer square roots or 600-700

import math
listx = []
listy = []
for i in range(1,101):
    x = math.sqrt(i)
    if x.is_integer():
        listx.append(x)

for z in range(600,701):
    y = math.sqrt(z)
    if y.is_integer():
        listy.append(y)

r1 = len(listx)
r2 = len(listy)

if r1<r2:
    print("600-700 has more" )
if r2<r1:
    print("1-100 has more" )
if r1==r2:
    print("both are equal" )

print(r1,r2)


## Make a program to add every consecutive no. from 1-100 and find differnce between the next sum of every number

listx = []
listy = []
for i in range(1-101):
    if i%2 == 0:
        even_no = i
        even_no.append(i)
    if i%2 != 0:
        odd_no = i
        odd_no.append(i)
print(listx-listy)
