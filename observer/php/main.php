<?php

$newsPublisher = new NewsPublisher();

$emailSub1 = new EmailSubscriber('usuario1@ejemplo.com');
$emailSub2 = new EmailSubscriber('usuario2@ejemplo.com');
$smsSub = new SMSSubscriber('+1234567890');

$newsPublisher->attach($emailSub1);
$newsPublisher->attach($emailSub2);
$newsPublisher->attach($smsSub);

$newsPublisher->publishNews('¡Gran evento acontece hoy!');

// Desuscribir un observador
$newsPublisher->detach($emailSub2);

$newsPublisher->publishNews('Actualización importante');