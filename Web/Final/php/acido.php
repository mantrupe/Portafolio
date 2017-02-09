<?php
require 'bd.login.php';
$sql = "SELECT * FROM receta_sabor WHERE IDsabor = '5'";
$result = $conn->query($sql);
$operacion = mysqli_fetch_array($result);
$R=$opeeracion['IDreceta'];
$sql = "SELECT * FROM receta WHERE IDreceta = '$R'";
$result = $conn->query($sql);
while ($row = $result->fetch_assoc() ) { ?>
  <div class="portada">
    <h3><?php echo $row['nombre']; ?></h3>
    <form class="carga" action="carga.modal.php" method="post">
      <input type="text" class="" style="display:none" name="nom" value="<?php echo $row['IDreceta']; ?>">
      <div class="opaco"><input type="submit" name="name" value="+"></div>
    </form>
    </div>
<?php } ?>
