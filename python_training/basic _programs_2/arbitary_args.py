def add_numbers(*args):
    total = 0
    for num in args:
        total += num
        print(f'The sum is : {total}')
add_numbers(10,20)
add_numbers(10,20,30)
