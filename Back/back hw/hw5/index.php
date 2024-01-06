<?php

header('Content-Type: text/html; charset=UTF-8');

$user = 'u52894';
$pass = '9698603';

$db = new PDO('mysql:host=localhost;dbname=u52894', $user, $pass, array(PDO::ATTR_PERSISTENT => true));

// =========== GET ===========
if ($_SERVER['REQUEST_METHOD'] == 'GET') {

  $messages = array();
  $errors = array();
  $values = array();
  $powers = array();

  // SAVE PARAMETER
  if (!empty($_COOKIE['save'])) {

    setcookie('save', '', 100000);
    setcookie('login', '', 100000);
    setcookie('pass', '', 100000);

    $messages[] = $_COOKIE['save'];

    if (!empty($_COOKIE['pass'])) {
      $messages['savelogin'] = sprintf('<div>Вы можете <a href="login.php">войти</a> с логином <strong>%s</strong>
        и паролем <strong>%s</strong> для изменения данных.</div>',
        strip_tags($_COOKIE['login']),
        strip_tags($_COOKIE['pass']));
    }

  }

  // ERRORS
  $errors['name'] = empty($_COOKIE['name_error']) ? '' : $_COOKIE['name_error'];
  $errors['email'] = !empty($_COOKIE['email_error']);
  $errors['powers'] = !empty($_COOKIE['powers_error']);
  $errors['bio'] = !empty($_COOKIE['bio_error']);
  $errors['check'] = !empty($_COOKIE['check_error']);

  /// name
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

  $values['name'] = empty($_COOKIE['name_value']) ? '' : strip_tags($_COOKIE['name_value']);
  $values['email'] = empty($_COOKIE['email_value']) ? '' : strip_tags($_COOKIE['email_value']);
  $values['year'] = empty($_COOKIE['year_value']) ? '' : is_numeric(strip_tags($_COOKIE['year_value']));
  $values['gender'] = empty($_COOKIE['gender_value']) ? 'male' : strip_tags($_COOKIE['gender_value']);
  $values['limbs'] = empty($_COOKIE['limbs_value']) ? '4' : is_numeric(strip_tags($_COOKIE['limbs_value']));
  $values['bio'] = empty($_COOKIE['bio_value']) ? '' : strip_tags($_COOKIE['bio_value']);

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

  if (!empty($_COOKIE[session_name()]) &&
      session_start() && !empty($_SESSION['login'])) {

    if (!empty($_GET['quit'])) {
      $_SESSION = array();
      if (ini_get("session.use_cookies")) {
          $params = session_get_cookie_params();
          setcookie(session_name(), '', time() - 42000,
              $params["path"], $params["domain"],
              $params["secure"], $params["httponly"]
          );
      }
      foreach($_COOKIE as $key => $value) {
        setcookie($key, '', 100000);
      }
      session_destroy();
      header('Location: ./');
    }

    $messages[] = '<div>Вы вошли с логином '.$_SESSION['login'].'. <a href="./?quit=1">Выйти</a> из аккаунта.</div>';

    try {

      $stmt = $db->prepare("SELECT * FROM application WHERE login = ?");
      $stmt->execute(array($_SESSION['login']));
      $user_data = $stmt->fetch();

      $values['name'] = strip_tags($user_data['name']);
      $values['email'] = strip_tags($user_data['email']);
      $values['year'] = strip_tags($user_data['year']);
      $values['gender'] = strip_tags($user_data['gender']);
      $values['limbs'] = strip_tags($user_data['limbs']);
      $values['bio'] = strip_tags($user_data['bio']);
      $powers_value = explode(", ", $user_data['powers']);

      $values['powers'] = [];
      foreach ($powers_value as $power) {
        if (!empty($powers[$power])) {
          $values['powers'][$power] = $power;
        }
      }

    } catch(PDOException $e) {
      setcookie('save', 'Ошибка! Результаты не загружены.');
      exit();
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

  if (!empty($_COOKIE[session_name()]) && session_start() && !empty($_SESSION['login'])) {

    try {

      $stmt = $db->prepare("UPDATE application SET name = ?, email = ?, year = ?, gender = ?, limbs = ?, powers = ?, bio = ? WHERE login = ?");
      $stmt->execute(array(
        $_POST['name'],
        $_POST['email'],
        $_POST['year'],
        $_POST['gender'],
        $_POST['limbs'],
        implode(', ', $_POST['powers']),
        $_POST['bio'],
        $_SESSION['login']
      ));

    } catch(PDOException $e) {
      setcookie('save', 'Ошибка! Результаты не сохранены.');
      exit();
    }

  }
  else {
    $user_login = uniqid();
    $user_pass = rand(123456, 999999);
    setcookie('login', $user_login);
    setcookie('pass', $user_pass);

    try {
      $stmt = $db->prepare("INSERT INTO application SET login = ?, pass = ?, name = ?, email = ?, year = ?, gender = ?, limbs = ?, powers = ?, bio = ?");
      $stmt->execute(array(
        $user_login,
        hash('sha256', $user_pass, false),
        $_POST['name'],
        $_POST['email'],
        $_POST['year'],
        $_POST['gender'],
        $_POST['limbs'],
        $_POST['bio']
      ));
    } catch(PDOException $e) {
      setcookie('save', 'Ошибка! Результаты не сохранены.');
      exit();
    }
  }

  setcookie('save', '<div>Спасибо, результаты сохранены!</div>');

  header('Location: ./');}