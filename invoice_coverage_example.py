class Invoice:
    def __init__(self, client_name, items):
        self.client_name = client_name
        self.items = items
        self.total_amount = sum(item.amount for item in items)
        
    def generate_invoice(self):
        invoice = f"Invoice for {self.client_name}:\n"
        for item in self.items:
            invoice += f"- {item.name}: {item.amount}$\n"
        invoice += f"Total: {self.total_amount}$"
        return invoice
    
    def send_invoice(self):
        # logic to send the invoice via email
        pass
        
    def not_covered(self):
        pass

class Item:
    def __init__(self, name, amount):
        self.name = name
        self.amount = amount
