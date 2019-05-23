# -*- coding: utf-8 -*-
"""
Created on Tue May  7 10:31:35 2019

@author: Zigma
"""


class User():
    """ Diplays user info"""
    def __init__(self, first_name, last_name, address, state, country):
        self.first_name = first_name
        self.last_name = last_name
        self.address = address
        self.state = state
        self.country = country
        self.login_attempts = 0

    def describe_user(self):
        """ Simulates a user's profile"""
        print('\nFirst Name: ' + self.first_name.title(), end='\n',)
        print('Last Name: ' + self.last_name.title(), end='\n')
        print('Address: ' + self.address.title(), end='\n',)
        print('State: ' + self.state.title(), end='\n',)
        print('Country: ' + self.country.title())

    def greet_user(self):
        """Greets the user"""
        print("\nHey, " + self.first_name.title() + "!")

    def increment_login_attempts(self, increment):
        """Increases the login attempts by 1"""
        increment == self.login_attempts
        self.login_attempts += 1

    def reset_login_attempt(self, reset):
        """ Resets the login attempts"""
        reset == self.login_attempts
        self.login_attempts -= self.login_attempts


def main():
    zigma = User('Innocent', 'osogwu', 'Sangotedo', 'Lagos', 'nigeria')
    zigma.login_attempts = 10
    inna = User('neke', 'eze', 'Onuiyi Nsukka', 'Enugu', 'nigeria')
    inna.login_attempts = 9
    zigma.increment_login_attempts('')
    inna.reset_login_attempt('')
    print("You have attempted " + str(zigma.login_attempts) + " Logins")
    print("Account has been reset to " + str(inna.login_attempts) + " logins")


if __name__ == '__main__':
    main()
