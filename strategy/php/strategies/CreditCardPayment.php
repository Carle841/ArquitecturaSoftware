<?php

class CreditCardPayment implements PaymentStrategy {
    private $cardNumber;
    private $cvv;
    private $expiryDate;

    public function __construct($cardNumber, $cvv, $expiryDate) {
        $this->cardNumber = $cardNumber;
        $this->cvv = $cvv;
        $this->expiryDate = $expiryDate;
    }

    public function pay($amount) {
        echo "Pagando $" . $amount . " con Tarjeta de Crédito\n";
        echo "Número de tarjeta: " . $this->cardNumber . "\n";
        // Lógica de procesamiento de tarjeta de crédito
    }
}