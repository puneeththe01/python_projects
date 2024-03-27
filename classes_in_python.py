class PrintName():
    def __init__(self):
        self.name = ''
        self.age = 0

    def print_name(self):
        self.name = input("Enter Your Name>> ")
        return self.name
    def return_age(self):
        print(f'Your Name is {user_details["UserName"]}')
        self.age = int(input('Enter Your Age>> '))
        return self.age
number = 0
user_details = {}
user_details['UserName'] = PrintName().print_name()
user_details['Age'] = PrintName().return_age()
print(user_details)

