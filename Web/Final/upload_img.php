<?php
if(! isset($_SESSION))
  session_start();
$dir = "/img/imgRecetas/";
$tipo = pathinfo($tar_file,PATHINFO_EXTENSION);
$idR = $_SESSION['receta'];
$sql = "SELECT nombre from receta WHERE IDreceta = '$idR'";
$nombre = $conn->query($sql);
//$tar_file = $dir .basename($_FILES["fileToUpload"][$nombre])
$tar = "$dir.$nombre.".".$tipo";
//revisar si es una imagen
if(isset($_POST["submit"])) {
    $check = getimagesize($_FILES["fileToUpload"]["tmp_name"]);
    if($check !== false) {
      //subir imagen
      if (move_uploaded_file($_FILES["fileToUpload"]["tmp_name"], $tar)) {
              unset($_SESSION['receta']);
              $sql = "UPDATE receta WHERE IDreceta = '$_SESSION['receta']' SET img ='$tar'"
              if ($conn->query($sql)) {
                  header('Location: Extra/index.php');
              }else {
                echo '<script type="text/javascript">
                  alert("Error");
                  location.href="index.php";
                </script>';
              }

          } else {
            $default = "/img/logo.jpg";
            $sql = "UPDATE receta WHERE IDreceta = '$_SESSION['receta']' SET img ='$default'"
            $conn->query($sql);
          /*  echo '<script type="text/javascript">
              alert("Error al subir el archivo");
              location.href="index.php";
            </script>';*/
          }

    } else {
      header('Location: Extra/index.php');
      echo '<script type="text/javascript">
        alert("El archivo no es una imagen");
        location.href="index.php";
      </script>';


    }
}

 ?>
