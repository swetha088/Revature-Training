def add(n1,n2,n3=0,n4=0):
    total=n1+n2+n3+n4
    return total
n1=int(input('Enter a number: '))
n2=int(input('Enter another number: '))
n3=int(input('Enter another number: '))
n4=int(input('Enter another number: '))
print(add(n1,n2,n3))
print(add(n1,n2,n3,n4))
print(add(n1,n2))