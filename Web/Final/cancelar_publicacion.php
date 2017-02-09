<?php
$sql = "DELETE receta WHERE IDreceta = '$_SESSION['receta']'";
if ($conn->query($sql)) {
  header('Location: /Extra/index.php');

}else{
  echo '<script type="text/javascript">
    alert("Error al cancelar");
    location.href="index.php";
  </script>';
}

 ?>
