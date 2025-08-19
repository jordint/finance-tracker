from transaction import Transaction


def main():
    print("Welcome to the Finance Tracker!")
    
    #Get user input for transaction details
    user_transaction = get_transactions()
    #Write transaction to CSV file
    save_to_csv()
    #Read and display transactions from CSV file
    summarise_transactions()


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
             # print(f'Youve entered: {transaction_name},{transaction_amount},£{transaction_category}')
             new_transaction = Transaction(name=transaction_name, amount=transaction_amount, category=transaction_category)
             return  new_transaction
         else:
            print("Invalid category selection. Please try again.")


def save_to_csv():
     print("Saving user transactions to CSV file: {transaction}")


def summarise_transactions():
    print("Summarising transactions from CSV file.")

main()

if __name__ == "__main__":
    main()
