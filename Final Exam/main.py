from Users import Customer, Admin
from Bank import Bank

def main():
    bank = Bank('Switch bank', 1000000000000)
    
    trump = Customer("Donald Trump", "trump@gmail.com", "current")
    obama = Customer("Barack Obama", "obama@gmail.com", "savings")
    haley = Customer("Nikki Haley", "haley@gmail.com", "current")
    
    Super_user = Admin("Super_user", "super_admin@gmail.com")
    
    trump.create_account(bank)
    obama.create_account(bank)
    haley.create_account(bank)
    Super_user.create_account(bank)
    
    while True:
        print("1. Deposit Money")
        print("2. Withdraw Money")
        print("3. View Balance")
        print("4. View Transaction History")
        print("5. Take Loan")
        print("6. Transfer Money")
        print("7. Delete User Account")
        print("8. View All Users")
        print("9. View total bank balance")
        print("10. View total bank loan")
        print("11. Switch Loan Feature")
        print("12. Exit")
        
        n = int(input("Enter an option: "))
        
        if n == 1:
            dep = int(input("Enter deposit amount: "))
            trump.deposit(dep)
        elif n == 2:
            draw = int(input("Enter withdraw amount: "))
            trump.withdraw(draw)
        elif n == 3:
            trump.view_balance()
        elif n == 4:
            trump.view_transaction_history()
        elif n == 5:
            amount = int(input("Enter loan amount: "))
            trump.take_loan(amount)
        elif n == 6:
            amount = int(input("Enter transfer amount: "))
            trump.transfer(obama, amount)
        elif n == 7:
            Super_user.delete_user_account(obama.account_number)
        elif n == 8:
            Super_user.view_users()
        elif n == 9:
            Super_user.view_total_balance()
        elif n == 10:
            Super_user.view_total_loan()
        elif n == 11:
            decision = input("Enter decision (y / n): ")
            if(decision == 'y'):
                Super_user.switch_loan_feature(True)
            else:
                Super_user.switch_loan_feature(False)
        
        else:
            break

if __name__ == '__main__':
    main()