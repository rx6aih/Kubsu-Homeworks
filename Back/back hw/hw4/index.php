<?php

header('Content-Type: text/html; charset=UTF-8');

// =========== GET ===========
if ($_SERVER['REQUEST_METHOD'] == 'GET') {

  $messages = array();
  $errors = array();
  $values = array();
  $powers = array();

  // SAVE PARAMETER
  if (!empty($_COOKIE['save'])) {
    setcookie('save', '', 100000);
    $messages[] = $_COOKIE['save'];
  }

  // ERRORS
  $errors['name'] = empty($_COOKIE['name_error']) ? '' : $_COOKIE['name_error'];
  $errors['email'] = !empty($_COOKIE['email_error']);
  $errors['powers'] = !empty($_COOKIE['powers_error']);
  $errors['bio'] = !empty($_COOKIE['bio_error']);
  $errors['check'] = !empty($_COOKIE['check_error']);

  // name
  if ($errors['name'] == '1') {
    setcookie('name_error', '', 100000);
    $messages[] = '<div>Заполните имя.</div>';
  }
  else if ($errors['name'] == '2') {
      setcookie('name_error', '', 100000);
      $messages[] = '<div>Недопустимые символы. Разрешены только русские и английские буквы,
      длина имени от 2 до 24 сиволов, обязательно начинается с заглавной.</div>';
  }

  // email
  if ($errors['email']) {
    setcookie('email_error', '', 100000);
    $messages[] = '<div>Заполните почту.</div>';
  }

  // powers
  if ($errors['powers']) {
    setcookie('powers_error', '', 100000);
    $messages[] = '<div>Заполните способности.</div>';
  }

  // bio
  if ($errors['bio']) {
    setcookie('bio_error', '', 100000);
    $messages[] = '<div>Заполните биографию.</div>';
  }

  // checkbox
  if ($errors['check']) {
    setcookie('check_error', '', 100000);
    $messages[] = '<div>Нельзя отправить форму без согласия с контрактом.</div>';
  }

  // VALUES
  $powers['immortality'] = 'Бессмертие';
  $powers['night-vision'] = 'Ночное зрение';
  $powers['levitation'] = 'Левитация';

  $values['name'] = empty($_COOKIE['name_value']) ? '' : $_COOKIE['name_value'];
  $values['email'] = empty($_COOKIE['email_value']) ? '' : $_COOKIE['email_value'];
  $values['year'] = empty($_COOKIE['year_value']) ? '' : $_COOKIE['year_value'];
  $values['gender'] = empty($_COOKIE['gender_value']) ? 'male' : $_COOKIE['gender_value'];
  $values['limbs'] = empty($_COOKIE['limbs_value']) ? '4' : $_COOKIE['limbs_value'];
  $values['bio'] = empty($_COOKIE['bio_value']) ? '' : $_COOKIE['bio_value'];

  if (!empty($_COOKIE['powers_value'])) {
      $powers_value = json_decode($_COOKIE['powers_value']);
  }

  $values['powers'] = [];
  if (isset($powers_value) && is_array($powers_value)) {
      foreach ($powers_value as $power) {
          if (!empty($powers[$power])) {
              $values['powers'][$power] = $power;
          }
      }
  }

  include('form.php');
}
// =========== POST ===========
else {
  // ERRORS
  $errors = FALSE;

  // name
  if (empty($_POST['name'])) {
    setcookie('name_error', '1', time() + 24 * 60 * 60);
    $errors = TRUE;
  }
  else if (!preg_match('/^([А-Я]{1}[а-яё]{1,23}|[A-Z]{1}[a-z]{1,23})$/u', $_POST["name"])) {
      setcookie('name_error', '2', time() + 24 * 60 * 60);
      $errors = TRUE;
  }
  else {
    setcookie('name_value', $_POST['name'], time() + 30 * 24 * 60 * 60);
  }

  // email
  if (empty($_POST['email'])) {
    setcookie('email_error', '1', time() + 24 * 60 * 60);
    $errors = TRUE;
  }
  else {
    setcookie('email_value', $_POST['email'], time() + 30 * 24 * 60 * 60);
  }

  // powers
  $powers = array();

  foreach ($_POST['powers'] as $key => $value) {
      $powers[$key] = $value;
  }

  if (!sizeof($powers)) {
    setcookie('powers_error', '1', time() + 24 * 60 * 60);
    $errors = TRUE;
  }
  else {
    setcookie('powers_value', json_encode($powers), time() + 30 * 24 * 60 * 60);
  }

  // bio
  if (empty($_POST['bio'])) {
    setcookie('bio_error', '1', time() + 24 * 60 * 60);
    $errors = TRUE;
  }
  else {
    setcookie('bio_value', $_POST['bio'], time() + 30 * 24 * 60 * 60);
  }

  // checkbox
  if (empty($_POST['check'])) {
    setcookie('check_error', '1', time() + 24 * 60 * 60);
    $errors = TRUE;
  }

  // other
  setcookie('year_value', $_POST['year'], time() + 30 * 24 * 60 * 60);
  setcookie('gender_value', $_POST['gender'], time() + 30 * 24 * 60 * 60);
  setcookie('limbs_value', $_POST['limbs'], time() + 30 * 24 * 60 * 60);

  if ($errors) {
    header('Location: index.php');
    exit();
  }
  else {
    setcookie('name_error', '', 100000);
    setcookie('email_error', '', 100000);
    setcookie('powers_error', '', 100000);
    setcookie('bio_error', '', 100000);
    setcookie('check_error', '', 100000);
  }

  $user = 'u52894';
  $pass = '9698603';
  $db = new PDO('mysql:host=localhost;dbname=u52894', $user, $pass, array(PDO::ATTR_PERSISTENT => true));

  try {
    $stmt = $db->prepare("INSERT INTO application SET name = ?, email = ?, year = ?, gender = ?, limbs = ?, bio = ?");
    $stmt -> execute(array(
        $_POST['name'],
        $_POST['email'],
        $_POST['year'],
        $_POST['gender'],
        $_POST['limbs'],
        $_POST['bio']
    ));
    setcookie('save', 'Спасибо, результаты сохранены!');
  }
  catch(PDOException $e){
    setcookie('save', 'Ошибка! Результаты не сохранены.');
    exit();
  }

  header('Location: index.php');
}