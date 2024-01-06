
    <?php
        $title="About";
        require("blocks/head.php");
    ?>
    <h1>ABOUT</h1>
    <p>Тут есть писи</p>
    <?php
      $from="vaka@baka.com";
      $to="example@baka.com";
      $message="vakaBaka";
      $subject="Theme";
      $subject="=?utf-8?b?".base64_encode($subject)."?=";
      $headers="From: $from\r   \nReply to: $from\r   \nContent-type:text/plain; charset=utf-8\r\n";
      mail($to,$subject,$message,$headers);
      require ("blocks/foot.php");
    ?>
