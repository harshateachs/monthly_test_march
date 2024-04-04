import uuid

# Dictionary to store account details
accounts = {}


def create_account(customer_name, opening_balance):
    # Generate unique account ID
    account_id = str(uuid.uuid4())

    # Save account details
    accounts[account_id] = {
        'customer_name': customer_name,
        'balance': opening_balance
    }

    # Return account ID
    return account_id


def deposit_money(account_id, amount):
    # Check if account exists
    if account_id in accounts:
        # Validate deposit amount
        if amount > 0:
            # Add deposited amount to account balance
            accounts[account_id]['balance'] += amount
            print(f"Rs. {amount} deposited into account {account_id}")
        else:
            print("Invalid deposit amount. Amount must be greater than 0.")
    else:
        print("Account not found.")


def withdraw_money(account_id, amount):
    # Check if account exists
    if account_id in accounts:
        # Validate withdrawal amount
        if amount > 0:
            # Check if sufficient balance
            if accounts[account_id]['balance'] >= amount:
                # Deduct withdrawal amount from account balance
                accounts[account_id]['balance'] -= amount
                print(f"Rs. {amount} withdrawn from account {account_id}")
            else:
                print("Insufficient balance.")
        else:
            print("Invalid withdrawal amount. Amount must be greater than 0.")
    else:
        print("Account not found.")


def transfer_money(from_account_id, to_account_id, amount):
    # Check if both accounts exist
    if from_account_id in accounts and to_account_id in accounts:
        # Validate transfer amount
        if amount > 0:
            # Check if sufficient balance in source account
            if accounts[from_account_id]['balance'] >= amount:
                # Transfer amount from source account to destination account
                accounts[from_account_id]['balance'] -= amount
                accounts[to_account_id]['balance'] += amount
                print(f"Rs. {amount} transferred from account {from_account_id} to account {to_account_id}")
            else:
                print("Insufficient balance in the source account.")
        else:
            print("Invalid transfer amount. Amount must be greater than 0.")
    else:
        print("One or both accounts not found.")


def check_balance(account_id):
    # Check if account exists
    if account_id in accounts:
        # Return account balance
        return accounts[account_id]['balance']
    else:
        print("Account not found.")


def main():
    # Suresh opens an account with Rs. 50,000
    suresh_account_id = create_account("Suresh", 50000)
    # Nithil opens an account with Rs. 100,000
    nithil_account_id = create_account("Nithil", 100000)

    # Suresh deposits another Rs. 50,000
    deposit_money(suresh_account_id, 50000)

    # Nithil withdraws Rs. 95,000 from his account
    withdraw_money(nithil_account_id, 95000)

    # Nithil asks Suresh for a loan of Rs. 20,000 and Suresh transfers Rs. 20,000 to Nithil
    transfer_money(suresh_account_id, nithil_account_id, 20000)

    # Check the balance of Suresh's account
    suresh_balance = check_balance(suresh_account_id)
    print(f"Account Balance: Suresh: Rs.{suresh_balance}")

    # Check the balance of Nithil's account
    nithil_balance = check_balance(nithil_account_id)
    print(f"Account Balance: Nithil: Rs.{nithil_balance}")


if __name__ == "__main__":
    main()
