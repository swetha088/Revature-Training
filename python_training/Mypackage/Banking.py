from Mypackage.interest_calculations import simple_interest,compound_interest
prin=float(input('please enter principal amount: '))
ny = float(input('please enter no of years: '))
roi=float(input('please enter roi: '))

si,amt=simple_interest(prin=prin,ny=ny,roi=roi)
print(f'SI : {si} Amount : {amt}')

amt=compound_interest(prin=prin, t=ny,roi=roi)
print(f'Amount: {amt}')