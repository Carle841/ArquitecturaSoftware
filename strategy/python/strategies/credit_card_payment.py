from interfaces.payment_strategy import PaymentStrategy

class CreditCardPayment(PaymentStrategy):
    def __init__(self, card_number, cvv, expiry_date):
        self.card_number = card_number
        self.cvv = cvv
        self.expiry_date = expiry_date

    def pay(self, amount):
        print(f"Pagando ${amount} con Tarjeta de Crédito")
        print(f"Número de tarjeta: {self.card_number}")
        # Lógica de procesamiento de tarjeta de crédito