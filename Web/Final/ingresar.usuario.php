<?php
$username=$_POST['email'];
$password=$_POST['password'];
require("bd.login.php");
$sqli="SELECT * FROM cocinero WHERE email = '$username' AND password ='$password'";

$proceso=$conn->query($sqli);

if ($proceso)
 {
  session_start();
	$resultado=mysqli_fetch_array($proceso);
	//var_dump($resultado);
  /*exit();*/
  $_SESSION['name']=$resultado['nombre'];
  $_SESSION['ID']=$resultado['IDcocinero'];
  $_SESSION['receta']=NULL;
  //var_dump($_SESSION['ID']);
  echo '<script type="text/javascript">
    alert("Bienvenido");
    location.href="index.php";
  </script>';
  //header("Location: index.php");
}else {
  echo '<script type="text/javascript">
  alert("Usuario o contraseña incorrectos ")
  location.href="index.php";
  </script>';
}
 ?>
