def add(**nums)-> (dict):
    res=nums['fn']+nums['sn']+nums['tn']
    return res
n1=int(input('Enter a number: '))
n2=int(input('Enter another number: '))
n3=int(input('Enter another number: '))
print(add(fn=n1,sn=n2,tn=n3))

