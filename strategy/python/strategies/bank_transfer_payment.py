from interfaces.payment_strategy import PaymentStrategy

class BankTransferPayment(PaymentStrategy):
    def __init__(self, account_number, bank_code):
        self.account_number = account_number
        self.bank_code = bank_code

    def pay(self, amount):
        print(f"Pagando ${amount} con Transferencia Bancaria")
        print(f"Número de cuenta: {self.account_number}")
        # Lógica de transferencia bancaria