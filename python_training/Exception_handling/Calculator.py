from ArithCalculations import ArithCalculations
from AgeNotEnoughError import AgeNotEnoughError

n1=int(input("Enter first number: "))
n2=int(input("Enter second number: "))
age = int(input('Age'))


calc = ArithCalculations(n1,n2)

print(f'{calc.add()}')
print(f'{calc.sub()}')
print(f'{calc.multiply()}')

try:
    if n2==0:
        raise ZeroDivisionError('num2 is 0')
    if age <18 :
        raise AgeNotEnoughError('You are Minor')
except ZeroDivisionError as zde:
    print(f'{zde}')
except AgeNotEnoughError as anee:
    print(f'{anee}')
else:
    try:
        l1=[1,5,7,3]
        val=l1[1]
        res=calc.div()
    except ZeroDivisionError as zde:
        print(f'{zde}- 0 in denominator')

    except IndexError as ie:
        print(f'{ie} - Index not available')
    except:
        print('Oops !!')
    else:
        print(val)
        print(res)
    finally:
        print('Done!')