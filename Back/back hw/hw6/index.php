<!DOCTYPE html>
<html lang="ru">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">
  <link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/4.0.0/css/bootstrap.min.css" integrity="sha384-Gn5384xqQ1aoWXA+058RXPxPg6fy4IWvTNh0E263XmFcJlSAwiGgFAW/dAiS6JXm" crossorigin="anonymous">
  <title>Задание 6</title>
</head>
<body>


<!-- PHP CODE -->
<?php

if (empty($_SERVER['PHP_AUTH_USER']) ||
    empty($_SERVER['PHP_AUTH_PW']) ||
    $_SERVER['PHP_AUTH_USER'] != 'admin' ||
    md5($_SERVER['PHP_AUTH_PW']) != md5('admin')) {
    header('HTTP/1.1 401 Unanthorized');
    header('WWW-Authenticate: Basic realm="application1"');
    print('<h1>401 Требуется авторизация. Пожалуйста, обновите страницу.</h1>');
    exit();
}

$token = md5($_SERVER['PHP_AUTH_USER']);
setcookie('token', $token, time() + 24 * 60 * 60);

$db_user = 'u52894';
$db_pass = '9698603';

$db = new PDO('mysql:host=localhost;dbname=u52894', $db_user, $db_pass, array(PDO::ATTR_PERSISTENT => true));

if ($_SERVER['REQUEST_METHOD'] == 'POST') {
  if ($_POST['token'] === $_COOKIE['token']) {
    try {
      $stmt = $db->prepare('DELETE FROM application1 WHERE login = ?');
      $stmt->execute(array($_POST['delete']));
    } catch (PDOException $e) {
      echo 'Ошибка: ' . $e->getMessage();
    }
    header('Location: ./');
  }
}

try {
  $stmt = $db->query('SELECT * FROM application1');

?>
<!-- ./ PHP CODE -->


  <div class="table-responsive">
    <form method="POST">
      <input type="hidden" name="token" value="<?php print($token); ?>">
      <table class="table table-striped table-bordered table-hover table-sm">
        <thead class="thead-dark">
          <tr>
            <th>ID</th>
            <th>Логин</th>
            <th>Пароль</th>
            <th>Имя</th>
            <th>Email</th>
            <th>Год гождения</th>
            <th>Пол</th>
            <th>Кол-во конеч.</th>
            <th>Способности</th>
            <th>Биография</th>
            <th>Удалить</th>
          </tr>
        </thead>
        <tbody>


<?php
while ($row = $stmt->fetch(PDO::FETCH_ASSOC)) {
  print('<tr>');
  foreach ($row as $cell) {
    print('<td>' . strip_tags($cell) . '</td>');
  }
  print('<td><button class="btn btn-outline-danger" name="delete" type="submit" value="'
  . strip_tags($row['login'])
  . '">x</button></td>');
  print('</tr>');
}
?>


        </tbody>
      </table>
    </form>
  </div>

<?php
} catch (PDOException $e) {
    echo 'Ошибка: ' . $e->getMessage();
    exit();
}
?>

</body>
</html>