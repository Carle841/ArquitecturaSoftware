from payment_context import PaymentContext
from strategies.credit_card_payment import CreditCardPayment
from strategies.paypal_payment import PayPalPayment
from strategies.bank_transfer_payment import BankTransferPayment

def main():
    payment_context = PaymentContext()

    # Pago con Tarjeta de Crédito
    credit_card_strategy = CreditCardPayment('1234-5678-9012-3456', '123', '12/25')
    payment_context.set_payment_strategy(credit_card_strategy)
    payment_context.execute_payment(100.50)

    print("\n")

    # Pago con PayPal
    paypal_strategy = PayPalPayment('usuario@ejemplo.com')
    payment_context.set_payment_strategy(paypal_strategy)
    payment_context.execute_payment(75.25)

    print("\n")

    # Pago con Transferencia Bancaria
    bank_transfer_strategy = BankTransferPayment('98765432', 'BBVA')
    payment_context.set_payment_strategy(bank_transfer_strategy)
    payment_context.execute_payment(500.00)

if __name__ == "__main__":
    main()