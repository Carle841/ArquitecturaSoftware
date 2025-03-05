class PaymentContext:
    def __init__(self):
        self._payment_strategy = None

    def set_payment_strategy(self, strategy):
        """Establecer la estrategia de pago"""
        self._payment_strategy = strategy

    def execute_payment(self, amount):
        """Ejecutar el pago con la estrategia actual"""
        if self._payment_strategy is None:
            raise ValueError("No se ha establecido una estrategia de pago")
        
        self._payment_strategy.pay(amount)