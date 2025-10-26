sqnum=[]
numbers=[10,20,30,40,50]
for num in  numbers:
    print(num)
    sqnum.append(num*num)
print(sqnum)
tupsq= tuple(sqnum)
print(tupsq)
setsq= set(sqnum)
print(setsq)
dnum=dict()
for num in  numbers:
    dnum[num] =num*num
print(dnum)


