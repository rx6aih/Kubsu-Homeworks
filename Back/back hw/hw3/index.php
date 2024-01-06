<?php

header('Content-Type: text/html; charset=UTF-8');

// =========== GET ===========
if ($_SERVER['REQUEST_METHOD'] == 'GET') {

    if (!empty($_GET['save'])) {
        print('<div class="alert alert-success col-sm-12 col-md-3 mt-3 mx-auto">Спасибо, результаты сохранены!</div>');
    }

    include('form.php');

    exit();
}

// =========== POST ===========

// Errors
$errors = FALSE;

// name
if (empty($_POST['name'])) {
    print('Заполните имя.<br/>');
    $errors = TRUE;
}

// email
if (empty($_POST['email'])) {
    print('Заполните почту.<br/>');
    $errors = TRUE;
}

// powers
if (empty($_POST['powers'])) {
    print('Заполните способности.<br/>');
    $errors = TRUE;
}

// bio
if (empty($_POST['bio'])) {
    print('Заполните биографию.<br/>');
    $errors = TRUE;
}

// checkbox
if (empty($_POST['check'])) {
    print('Нельзя отправить форму без согласия с контрактом.<br/>');
    $errors = TRUE;
}

// exit if errors
if ($errors) {
    exit();
}

$user = 'u52894';
$pass = '9698603';

$db = new PDO('mysql:host=localhost;dbname=u52894', $user, $pass,  [PDO::ATTR_PERSISTENT => true, PDO::ATTR_ERRMODE => PDO::ERRMODE_EXCEPTION]);

try {
    $stmt = $db->prepare("INSERT INTO application SET name = ?, email = ?, year = ?, gender = ?, limbs = ?, bio = ?");
    $stmt->execute(array(
        $_POST['name'],
        $_POST['email'],
        $_POST['year'],
        $_POST['gender'],
        $_POST['limbs'],
        $_POST['bio']
    ));
} catch (PDOException $e) {
    print('Ошибка: ' . $e->getMessage());
    exit();
}

header('Location: ?save=1');
