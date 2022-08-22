class Customer:
    """Creates an instance of Customer"""
    def __init__(self, fname, lname, email, phone):
        self.fname = fname
        self.lname = lname
        self.email = email
        self.phone = phone


# The code below will use your class to print values to the terminal after
# it has been written. Comment the lines below back in to test it

customer_one = Customer("Theon", "Greyjoy", "t.gj@email.com", "123456789")
print(customer_one)
print(customer_one.fname)
print(customer_one.lname)
print(customer_one.email)
print(customer_one.phone)


print('\n ---------')

customer_two = Customer("Thor", "Hugo", "thor.rocks@email.com", "72462986")
print(customer_two)
print(customer_two.fname)
print(customer_two.lname)
print(customer_two.email)
print(customer_two.phone)
