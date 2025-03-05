<?php

class BankTransferPayment implements PaymentStrategy {
    private $accountNumber;
    private $bankCode;

    public function __construct($accountNumber, $bankCode) {
        $this->accountNumber = $accountNumber;
        $this->bankCode = $bankCode;
    }

    public function pay($amount) {
        echo "Pagando $" . $amount . " con Transferencia Bancaria\n";
        echo "Número de cuenta: " . $this->accountNumber . "\n";
        // Lógica de transferencia bancaria
    }
}
