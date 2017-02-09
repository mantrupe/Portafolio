<?php
  require 'bd.login.php';
  $nombre = $_POST['ni'];
  $sql = "INSERT INTO ingredientes VALUES (NULL,'$nombre')";
  $conn->query($sql);
  $retunData = array(
    "response" => 1,
    "reason" => "Ok"
  );
echo json_encode($retunData);
 ?>
