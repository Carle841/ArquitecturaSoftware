<?php

class PayPalPayment implements PaymentStrategy {
    private $email;

    public function __construct($email) {
        $this->email = $email;
    }

    public function pay($amount) {
        echo "Pagando $" . $amount . " con PayPal\n";
        echo "Email de PayPal: " . $this->email . "\n";
        // Lógica de procesamiento de PayPal
    }
}