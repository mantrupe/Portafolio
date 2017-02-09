
  <?php
  require 'bd.login.php';
  $sql = "SELECT * FROM receta WHERE IDtiempo = '4' ";
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
