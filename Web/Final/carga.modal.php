<!DOCTYPE html>
<html>
  <head>
    <link href='https://fonts.googleapis.com/css?family=Roboto' rel='stylesheet' type='text/css'>
    <link rel="stylesheet" href="css/general.css" media="screen" title="no title" charset="utf-8">
    <link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/font-awesome/4.5.0/css/font-awesome.min.css">
    <meta charset="utf-8">
    <title></title>
  </head>
  <body>
    <?php
    require 'bd.login.php';
    $nombre = $_POST['nom'];
    $sql ="SELECT * FROM receta WHERE IDreceta = '$nombre'";
    $result = $conn->query($sql);
    $receta = mysqli_fetch_array($result);
     ?>
    <div class='fondo3'>
      <div class='reci'>
        <h1><?php echo $receta['nombre']; ?></h1>
        <div class="reciP">
          <h3>Preparacion</h3><br><br>
        <?php echo $receta['preparacion']; ?>
        </div>
        <div class="reciI">
          <h3>ingredientes</h3>
       <?php
       $sql = "SELECT * FROM receta_ingrediente WHERE  IDreceta = '$nombre'";
       $result = $conn->query($sql);
       while ( $row = $result->fetch_assoc() ) {
         //var_dump($row);
         $IDI = $row['IDingrediente'];
         $sql = "SELECT * FROM ingredientes WHERE  IDingrediente = '$IDI'";
         $result = $conn->query($sql);
         $ingrediente = mysqli_fetch_array($result);
         //var_dump($ingrediente);
         ?>
         <label class="diente"><?php echo $row['cantidad'] ."  ".$row['medida']." de ".$ingrediente['nombre']; ?></label>

      <?php }  ?>
        </div>
        <form class="" action="/Extra/index.php" method="post">
          <input type="submit" name="name" value="Regresar">
        </form>
      </div>
    </div>
  </body>
</html>
