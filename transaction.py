#Class to store transaction data
class Transaction:
    def __init__(self, name, amount, category): 
        self.name = name
        self.amount = amount
        self.category = category
    
    def __repr__(self):
        return f"Transaction(name={self.name}, amount={self.amount}, category=£{self.category})"
    
