def calculate(m1,m2,m3):
    total=m1+m2+m3
    avg=total/3
    return total,avg
sname=input('Enter your first name: ')
m1=int(input('Enter your first number: '))
m2=int(input('Enter your second number: '))
m3=int(input('Enter your third number: '))
total=calculate(m1,m2,m3)
avg=calculate(m1,m2,m3)
print(f'Total :{total},Name: {sname}, Avg: {'avg'}' )