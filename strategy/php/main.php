<?php
$paymentContext = new PaymentContext();

// Pago con Tarjeta de Crédito
$creditCardStrategy = new CreditCardPayment('1234-5678-9012-3456', '123', '12/25');
$paymentContext->setPaymentStrategy($creditCardStrategy);
$paymentContext->executePayment(100.50);

echo "\n";

// Pago con PayPal
$paypalStrategy = new PayPalPayment('usuario@ejemplo.com');
$paymentContext->setPaymentStrategy($paypalStrategy);
$paymentContext->executePayment(75.25);

echo "\n";

// Pago con Transferencia Bancaria
$bankTransferStrategy = new BankTransferPayment('98765432', 'BBVA');
$paymentContext->setPaymentStrategy($bankTransferStrategy);
$paymentContext->executePayment(500.00);
?>