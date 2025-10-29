from Employee import Employee


empid = int(input('Employee id: '))
ename = str(input('Employee name: '))
bp = int(input('Basic pay: '))

employee = Employee(empid, ename, bp )

print(f'Employee ID: {employee.empid} \n Name: {employee.ename} \n '
      f'Gross Pay: {employee.calc_grosspay()} \n'
      f'Net Pay: {employee.calc_netpay()}')