#BANKING MANAGEMENT SYSTEM
'''
Problem Statement:
1. Give a prompt to the user asking if they wish to create a new Savings Account or access an existing
one.
2. If the user would want to create a new account, accept their name and initial deposit, and
create a 5 digit random number and make it as the a/c number of their new Savings Account.
3. If they are accessing an existing account, accept their name and account number to validate
the user, and give them options to withdraw, deposit, display their available balance.
'''
from abc import ABCMeta, abstractmethod
from random import randint
class Account(metaclass = ABCMeta):
    @abstractmethod
    def createAccount():
        return 0
    @abstractmethod
    def authenticate():
        return 0 
    @abstractmethod
    def withdraw():
        return 0
    @abstractmethod
    def deposit():
        return 0
    @abstractmethod
    def displayBalance():
        return  0

    
class SavingsAccount(Account):

    def __init__(self):
        #[key][0] = name; [key][1] = balance
        self.savingsAccount = {}    #savingsAccount is the dictionary/placeholder where we are going to store the information

    def createAccount(self, name, initialDeposit):
        self.accountNumber = randint(10000,99999)   #as mentioned in problem statement, a/c no is 5 digit random no, this we have acheived using randint()
        self.savingsAccount[self.accountNumber] = [name, initialDeposit]        #here the 'accountNumber' generated in the previous statement will be viewed as the key to the dictionary 'savingsAccount'
        print('Account created. Your a/c number is:',self.accountNumber)

    def authenticate(self, name, accountNumber):    #this method is called when th user wants to access an existing a/c
        if accountNumber in self.savingsAccount.keys(): #checking whether the accountNumber provided by the user is existing in the key of the dictionary
            if self.savingsAccount[accountNumber][0] == name:    #checking whether the name index in the dictionary is matching with the name as provided by the user
                print('Authentication is successfull!')
                self.accountNumber = accountNumber      #if the authentication is successfull, then this accountNumber is to be considered as the instance attribute for the rest of the process
                return True
            else:
                print('Authentication Failed!')
                return False
        else:
            print('Authentication Failed!')
            return False

    def withdraw(self, withdrawAmount):
        if withdrawAmount > self.savingsAccount[self.accountNumber][1]:     #checking whether the a/c balance in the dictionary for a particular account is lesser than the withdrawl amt
            print('Insufficient Balance')
        else:
            self.savingsAccount[self.accountNumber][1] -= withdrawlAmount   #if the amt in the dictionary for an a/c number is greater than the withdrawl amt, then (balance-withdrawl_amt)
            print('Withdrawl Successful!')
            self.displayBalance()                                           #calling the displayBalance method, to show the balance

    def deposit(self, depositAmount):
        self.savingsAccount[self.accountNumber][1] += depositAmount         #updating the a/c with the deposit_amt, (balance+deposit_amt)
        print('Deposit was successful!')
        self.displayBalance()                                               #calling the displayBalance method, to show the balance
    def displayBalance(self):
        print('Balance in a/c:',self.savingsAccount[self.accountNumber][1])

savingsAccount = SavingsAccount()

#MENU CREATION:
while True:
    print('Enter 1 to create a new Account')
    print('Enter 2 to access an existing account')
    print('Enter 3 to exit')
    userChoice = int(input())                                               #ask the user which function does he want to perform?
    if userChoice is 1:
        print('Enter your Name:')
        name = input()
        print('Enter Initial Deposit Account:')
        deposit = int(input())
        savingsAccount.createAccount(name, deposit)                         #here we are adding the name and initial deposit to the dictionary which we have previously created savingsAccount
    elif userChoice is 2:
        print('Enter your name:')
        name = input()
        print('Enter your A/C no:')
        accountNumber = int(input())
        autheticationStatus = savingsAccount.authenticate(name, accountNumber)  #here we have created a new placeholder by the name autheticationStatus, which will be helping to authenticate whether or not the name and a/c number we provide is correct or not?
        if autheticationStatus is True:
            while True:
                print('Enter 1 to withdraw')
                print('Enter 2 to deposit')
                print('Enter 3 to display balance')
                print('Enter 4 to return to previous menu')
                userChoice = int(input())
                if userChoice is 1:
                    print('Enter withdrawl amount:')
                    withdrawlAmount = int(input())
                    savingsAccount.withdraw(withdrawlAmount)        #will refer to the withdraw method in the SavingsAccount class and perform its functionalities, refer to that for more knowledge
                elif userChoice is 2:
                    print('Enter deposit amount:')
                    depositAmount = int(input())
                    savingsAccount.deposit(depositAmount)           #will refer to the deposit method in the SavingsAccount class and perform its functionalities, refer to that for more knowledge
                elif userChoice is 3:
                    savingsAccount.displayBalance()
                elif userChoice is 4:
                    break                                           #break out of the infinite while loop
    elif userChoice is 3:
        quit()
        
        
