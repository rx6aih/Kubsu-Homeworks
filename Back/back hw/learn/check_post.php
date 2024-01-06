<?php
$inga=$_POST["username"];
$mail=$_POST['email'];
$pas=$_POST['password'];

if($inga=="Инга")
echo "пися";

if(trim($inga)=="")
echo "Не туда ты зашёл дружок";

if(trim($mail)=='' || trim($pas)=='' || trim($_POST['info'])=='')
echo "Гони сюда данные сучара";
else{
   header('Location:https://vk.com/saintsrx');
   exit;
}