
# -*- coding: utf-8 -*-
"""
Created on Thu May 23 10:58:01 2019

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

    def describe_user(self):
        """ Simulates a user's profile"""
        print('\nFirst Name: ' + self.first_name.title(), end='\n',)
        print('Last Name: ' + self.last_name.title(), end='\n')
        print('Address: ' + self.address.title(), end='\n',)
        print('State: ' + self.state.title(), end='\n',)
        print('Country: ' + self.country.title())

    def greet_user(self):
        print("\nHey, " + self.first_name.title() + "!")


class Privileges():
    """Displays the priveleges of an Admin"""
    def __init__(self, a_privileges):
        """ Initializes Privileges attribute"""
        self.a_privileges = []

    def show_privileges(self, a_privileges):
        """ Lists the privileges of the Admin"""
        print("The Admin: ")
        for a_privilege in a_privileges:
            print("- " + a_privilege)


class Admin(User):
    """ Represents previlees specific to the Admin"""
    def __init__(self, first_name, last_name, address, state, country):
        """Initializes attributes of the parent class admin"""

        super(a_privileges).__init__(first_name, last_name, address, state, country)
        self.privileges = Privileges()


admin_privileges = [
            'can add post',
            'can ban user',
            'can  delete post',
            'can add user',
            'can censor post',
            ]
admin = Admin(
            'Innocent',
            'Chizoba',
            'Sangotedo',
            'Lagos',
            'Nigeria',
            )
admin.privileges.show_privileges(admin_privileges)
