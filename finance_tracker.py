from transaction import Transaction
import csv as transactions

def main():
    print("Welcome to the Finance Tracker!")
    transaction_file = 'transactions.csv'
    budget = 100.00  
    
    #Get user input for transaction details
    user_transaction = get_transactions()
    #Write transaction to CSV file
    save_to_csv(user_transaction,transaction_file)
    #Read and display transactions from CSV file
    summarise_transactions(transaction_file,budget)


def get_transactions():
     print("Getting user transactions.")
     transaction_name = input("Enter transaction name: ")
     transaction_amount = float(input("Enter transaction amount: "))
     transaction_categories=[
       'Food',
       'Transport',
       'Fun & Leisure',
       'Home',
       'Shopping',
       'General'
    ]
     while True: #infinite loop to ensure valid category selection
         print("Select from available categories:")
         for i, category in enumerate(transaction_categories, start=1): #loops through the list of categories
             print(f"{i}. {category}")
             
         valid_range = f'[1-{len(transaction_categories)}]'
         category_index = int(input(f"Select a category {valid_range}: "))

         if category_index in range(1, len(transaction_categories) + 1): #validates user input
             transaction_category = transaction_categories[category_index - 1]
             print(f'Youve entered: {transaction_name},£{transaction_amount:.2f},{transaction_category}')
             new_transaction = Transaction(name=transaction_name, amount=transaction_amount, category=transaction_category)
             return new_transaction
         else:
            print("Invalid category selection. Please try again.")


def save_to_csv(user_transaction: Transaction,transaction_file):
     print(f'Saving user transactions to CSV file: {user_transaction} to {transaction_file}')
     with open(transaction_file, 'a') as file:
         file.write(f'{user_transaction.name},{user_transaction.amount},{user_transaction.category}\n')


def summarise_transactions(transaction_file,budget):
    print('Summarising transactions from CSV file.')
    expenses:list[Transaction]=[]
    #Read transactions from CSV file
    with open(transaction_file, 'r') as file:
            reader = transactions.reader(file)
            print("Your transactions:")
            for row in reader:
                transaction_name, transaction_amount,transaction_category = row
                line_transaction = Transaction(name=transaction_name, amount=float(transaction_amount), category=transaction_category)
                expenses.append(line_transaction)
                print(transaction_name, transaction_amount, transaction_category)

    #Dictionary to store total amounts by their category
    total_by_category = {}
    for transaction in expenses:
        key = transaction.category
        #If the category already exists, add the amount to it, otherwise create a new entry
        if key in total_by_category:
            total_by_category[key] += transaction.amount
        else:
            total_by_category[key] = transaction.amount
    #Display total amounts by category
    for category, total in total_by_category.items():
        print(f'Total for {category}: £{total:.2f}')

    #Display total amount of all transactions
    total_amount = sum(transaction.amount for transaction in expenses)
    print(f'Total amount of all transactions: £{total_amount:.2f}\nRemaining Budget: £{budget-total_amount:.2f}')





main()

if __name__ == '__main__':
    main()
