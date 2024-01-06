<!DOCTYPE html>
<html lang="ru">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">
  <link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/4.0.0/css/bootstrap.min.css" integrity="sha384-Gn5384xqQ1aoWXA+058RXPxPg6fy4IWvTNh0E263XmFcJlSAwiGgFAW/dAiS6JXm" crossorigin="anonymous">
  <title>Задание 4</title>
</head>
<body>
  <div class="container py-3">
    <div class="row justify-content-center align-items-center">
      <div class="col-sm-12 col-md-6">

        <?php
        if (!empty($messages)) {
          print('<div id="messages" class="alert alert-primary">');
          foreach ($messages as $message) {
            print($message);
          }
          print('</div>');
        }
        ?>

        <form id="form" action="" method="POST">

          <!-- Имя -->
          <div class="form-group">
            <label for="name-input">Имя</label>
            <input id="name-input" class="form-control <?php if ($errors['name']) {print 'is-invalid';} ?>" type="text" name="name" placeholder="Ваше имя" value="<?php print $values['name']; ?>" />
          </div>

          <!-- Email -->
          <div class="form-group">
            <label for="email-input">Email</label>
            <input id="email-input" class="form-control <?php if ($errors['email']) {print 'is-invalid';} ?>" type="email" name="email" placeholder="Ваше Email" value="<?php print $values['email']; ?>" />
          </div>

          <!-- Год рождения -->
          <div class="form-group">
            <label for="year-select">Год рождения</label>
            <select id="year-select" class="form-control" name="year">
              <?php
              for ($i = 2013; $i > 1960; $i--) {
                print('<option value="'.$i.'" ');
                if ($values['year'] == $i) print('selected ');
                print('>'.$i.'</option> ');
              }
              ?>
            </select>
          </div>

          <!-- Пол -->
          <div class="form-group">
            <label>Пол</label>
            <div class="control">
              <!-- Мужской -->
              <div class="custom-control custom-radio custom-control-inline">
                <input id="gender-radio-1" type="radio" name="gender" class="custom-control-input" value="male" <?php if ($values['gender'] == 'male') print("checked"); ?> />
                <label class="custom-control-label" for="gender-radio-1">Мужской</label>
              </div>
              <!-- Женский -->
              <div class="custom-control custom-radio custom-control-inline">
                <input id="gender-radio-2" type="radio" name="gender" class="custom-control-input" value="female" <?php if ($values['gender'] == 'female') print("checked"); ?> />
                <label class="custom-control-label" for="gender-radio-2">Женский</label>
              </div>
            </div>
          </div>

          <!-- Количество конечностей -->
          <div class="form-group">
            <label>Количество конечностей</label>
            <div class="control">
              <!-- 4 -->
              <div class="custom-control custom-radio custom-control-inline">
                <input id="limbs-radio-1" type="radio" name="limbs" class="custom-control-input" value="4" <?php if ($values['limbs'] == 4) print("checked"); ?> />
                <label class="custom-control-label" for="limbs-radio-1">4</label>
              </div>
              <!-- 6 -->
              <div class="custom-control custom-radio custom-control-inline">
                <input id="limbs-radio-2" type="radio" name="limbs" class="custom-control-input" value="6" <?php if ($values['limbs'] == 6) print("checked"); ?> />
                <label class="custom-control-label" for="limbs-radio-2">6</label>
              </div>
              <!-- 8 -->
              <div class="custom-control custom-radio custom-control-inline">
                <input id="limbs-radio-3" type="radio" name="limbs" class="custom-control-input" value="8" <?php if ($values['limbs'] == 8) print("checked"); ?> />
                <label class="custom-control-label" for="limbs-radio-3">8</label>
              </div>
            </div>
          </div>

          <!-- Сверхспособности -->
          <div class="form-group">
            <label for="powers-select">Сверхспособности</label>
            <select id="powers-select" class="form-control <?php if ($errors['powers']) {print 'is-invalid';} ?>" name="powers[]" multiple size="3">
              <?php
              foreach ($powers as $key => $value) {
                $selected = empty($values['powers'][$key]) ? '' : ' selected="selected" ';
                printf('<option value="%s",%s>%s</option>', $key, $selected, $value);
              }
              ?>
            </select>
          </div>

          <!-- Биография -->
          <div class="form-group">
            <label for="bio-textarea">Биография</label>
            <textarea id="bio-textarea" name="bio" class="form-control <?php if ($errors['bio']) {print 'is-invalid';} ?>" placeholder="Напишите немного о себе..."><?php print $values['bio']; ?></textarea>
          </div>

          <!-- Чекбокс -->
          <div class="form-group">
            <div class="custom-control custom-checkbox">
              <input id="ok-checkbox" type="checkbox" class="custom-control-input <?php if ($errors['check']) {print 'is-invalid';} ?>" name="check">
              <label class="custom-control-label" for="ok-checkbox"> С <a href="#" class="has-text-info">контрактом</a> ознакомлен(а).</label>
            </div>
          </div>

          <!-- Кнопка -->
          <div class="form-group">
            <div class="control">
              <button name="send" type="submit" class="btn btn-primary" value="ok">Отправить</button>
            </div>
          </div>

        </form>
      </div>
    </div>
  </div>
</body>
</html>