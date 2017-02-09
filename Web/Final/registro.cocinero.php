<?php
/*if(! isset($_SESSION))
  session_start();*/
require ("bd.login.php");

$user=$_POST['nombre'];
$email=$_POST['email'];
$password=$_POST['password'];
$confirm=$_POST['cpassword'];
if ($password == $confirm) {
$sql= "INSERT INTO cocinero VALUES(NULL,'$user','$email','$password')";
$conn->query($sql);
/*  mysqli_query("INSERT INTO cocinero VALUES('','$user','$email','$password','')");*/
  echo'<script type="text/javascript">
    alert("Registro exitoso");
    location.href="index.php";
  </script>';
  $conn->close();
}else {
  echo'<script type="text/javascript">
    alert("Las contraseñas no coinciden");
    location.href="index.php";
  </script>';
}  ?>
