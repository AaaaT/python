payroll = {'emp1': {'name': 'Precious', 'job': 'Mgr', 'Wage': 50000},
     'emp2': {'name': 'Kim', 'job': 'Dev', 'Wage': 60000},
     'emp3': {'name': 'Sam', 'job': 'Dev', 'Wage': 70000}}


# Add one more employee
payroll['emp4'] = {'name': 'Max', 'job': 'Admin', 'Wage': 30000}

# Print information about all employees
for id, info in payroll.items():
    print(f'\n------------\nEmployee ID: {id}')
    for key in info:
        print(f'{key} : {info[key]}')
