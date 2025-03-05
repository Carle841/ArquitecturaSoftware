from interfaces.payment_strategy import PaymentStrategy

class PayPalPayment(PaymentStrategy):
    def __init__(self, email):
        self.email = email

    def pay(self, amount):
        print(f"Pagando ${amount} con PayPal")
        print(f"Email de PayPal: {self.email}")
        # Lógica de procesamiento de PayPal