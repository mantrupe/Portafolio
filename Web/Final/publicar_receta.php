<?php
if(! isset($_SESSION))
  session_start();
require 'bd.login.php';

$nombre =$_POST['name'];
$preparacion =$_POST['Rprep'];
$tipo =$_POST['tipo'];
$tiempo = $_POST['tmpo'];
$sabores =$_POST['sabor'];
$ingredientes = $_POST['ingredientes'];
$consulta = "SELECT IDtiempo FROM tiempo WHERE nombre = '".$tiempo."'";
$proceso = $conn->query($consulta);
$array =mysqli_fetch_array($proceso);
$idTm = $array['IDtiempo'];
$consulta = "SELECT IDtipo FROM tipo WHERE nombre = '$tipo'";
$proceso = $conn->query($consulta);
$array= mysqli_fetch_array($proceso);
$idTp = $array['IDtipo'];
$tem = "temporal";
$idU = $_SESSION['ID'];
$sql_receta = "INSERT INTO receta VALUES(NULL,'".$preparacion."','".$tem."','".$idU."','".$idTm."','".$idTp."','".$nombre."')";
if($conn->query($sql_receta)){

  /*----Bandera id receta----------------*/
  $sql = "SELECT IDreceta FROM receta WHERE nombre = '$nombre'";
  $proceso = $conn->query($sql);
  $array = mysqli_fetch_array($proceso);
  $idR = $array['IDreceta'];
  $_SESSION['receta'] = $idR;
  //Insercion de sabores
  $a = count($sabores);
  var_dump($a);
  for ($i=0; $i < $a ; $i++) {
    $sabor = $sabores[$i];
    var_dump($sabor);
    $consulta = "SELECT IDsabor FROM sabor WHERE nombre = '$sabor'";
    $proceso = $conn->query($consulta);
    $array = mysqli_fetch_array($proceso);
    $idS = $array['IDsabor'];
    $sentencia = "INSERT INTO receta_sabor VALUES('".$idR."','".$idS."')";
    echo $sentencia;
    var_dump($i);
    if($conn->query($sentencia) == false){
      $retunData = [
        "response" => 1,
        "reason" => "Error al insertar sabores"
      ];
    }
  }
  /*foreach ($sabores as $sabor) {
    var_dump($sabor);
    //print_r($sabor);
  //  echo "  ";
    $consulta = "SELECT IDsabor FROM sabor WHERE nombre = '$sabor'";
    $proceso = $conn->query($consulta);
    $array = mysqli_fetch_array($proceso);
    $idS = $array['IDsabor'];
    $sentencia = "INSERT INTO receta_sabor VALUES('".$idR."','".$idS."')";
    //print_r($idR);
  //  echo "   ";
    //print_r($idS);
    $proceso = $conn->query($sentencia);
    if ($proceso) {
      //Insercion  de ingredientes

    }else {
      $retunData = [
        "response" => 1,
        "reason" => "Error al insertar sabores"
      ];
    }
  }*/
  $a = count($ingredientes);
  for ($i=0; $i <$a ; $i++) {
    $Inom = $ingredientes[$i]['nombre'];
    var_dump($Inom);
    $consulta ="SELECT IDingrediente FROM ingredientes WHERE nombre = '$Inom'";
    $proceso= $conn->query($consulta);
    $array = mysqli_fetch_array($proceso);
    $idI = $array['IDingrediente'];
    var_dump($idI);
    //print_r($idI);
    $cantidad = $ingredientes[$i]['cantidad'];
    $medida = $ingredientes[$i]['medida'];
    $si = "INSERT INTO receta_ingrediente VALUES('".$idR."','".$cantidad."','".$medida."','".$idI."')";
    echo $si;
      if ($conn->query($si)) {
        $retunData = [
          "response" => 1,
          "reason" => "Receta publicada"
        ];
      }else {
        $retunData = [
          "response" => 1,
          "reason" => "Error al insertar ingrediente"
        ];
      }
  }
  /*foreach ($ingredientes as $ingre) {
    //print_r($ingre);
    $Inom = $ingre['nombre'];
    $consulta ="SELECT IDingrediente FROM ingredientes WHERE nombre = '$Inom'";
    $proceso= $conn->query($consulta);
    $array = mysqli_fetch_array($proceso);
    $idI = $array['IDingrediente'];
    //print_r($idI);
    $cantidad = $ingre['cantidad'];
    $medida = $ingre['medida'];
    $si = "INSERT INTO receta_ingrediente VALUES('".$idR."','".$cantidad."','".$medida."','".$idI."')";
    if ($conn->query($si)) {
      $retunData = [
        "response" => 1,
        "reason" => "Receta publicada"
      ];
    }else{
      $retunData = [
        "response" => 1,
        "reason" => "Error al insertar ingredientes"
      ];
    }
  }*/
}else{
  $retunData = [
    "response" => 1,
    "reason" => "Error al publicar receta"
  ];

}
echo json_encode($retunData);
 ?>
