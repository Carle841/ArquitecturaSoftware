<?php

class PaymentContext {
    private $paymentStrategy;

    public function setPaymentStrategy(PaymentStrategy $strategy) {
        $this->paymentStrategy = $strategy;
    }

    public function executePayment($amount) {
        if ($this->paymentStrategy === null) {
            throw new Exception("No se ha establecido una estrategia de pago");
        }
        $this->paymentStrategy->pay($amount);
    }
}