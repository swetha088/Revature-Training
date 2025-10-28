from  interest_calculations import simple_interest
from interest_calculations import compound_interest
from mensuration_calculations import area_of_circle,cir_of_circle,area_of_rectangle,area_of_square

prin=float(input('Principal:'))
ny=float(input('Years:'))
roi=float(input('Rate of Interest:'))

print(f'Simple Interest:{simple_interest(prin=prin ,ny=ny,roi=roi)[0]}\n'
f'Amount:{simple_interest(prin=prin,ny=ny,roi=roi)[1]} ')

amt = compound_interest(prin=prin, t=ny, roi=roi)
ci = amt - prin
print(f'Compound Interest: {ci}\nAmount: {amt}')


print(f'Area of Circle:{area_of_circle(0)}\n 'f'Cir of Circle:{cir_of_circle(10)}\n '
    f'Area of Rectangle:{area_of_rectangle(10,5)}\n'
    f'Area of Square:{area_of_square(10)}\n ')
