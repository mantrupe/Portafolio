<?php

   require 'bd.login.php';
   $sql = "SELECT * FROM Ingredientes";

  // $consulta =$conn->query($sql);
   $consulta = mysqli_query($conn, $sql);

   ?>
  <!--  <form class="ingForm" action="index.html" method="post"> -->
  <div id = "radio">
    <?php
   while ($row = mysqli_fetch_assoc($consulta) ) {
     ?><label class="cargaI"> <input type="radio" name="ingrediente" id="ingre" value="<?php  echo  $row ["nombre"] ?>"> <?php echo $row['nombre'] ?> </input></label>
     <?php //echo "<input type='radio' name='ingrediente' value=$row[1]>";
       } ?>
  </div>
  <div class="ADD">

   <input type="text" id="newi" name="ni" value="" placeholder="Nombre" class="intext">
    <input type="button"  name="newi" value="Agregar" onclick="newI()">
    <input type="button" name="no" value="Cancelar" id="canbb" onclick="canSli()">

  </div>
  <label class="addI" onclick="slideI()"><i title="Nuevo Ingrediente" class="fa fa-plus-circle" aria-hidden="true"></i></label>
  <!--  </form> -->
  <?php
  $conn->close();
 ?>
