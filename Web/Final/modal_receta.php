<?php
if(! isset($_SESSION))
  session_start();
/*if ($_SESSION['receta'] = NULL) {
 echo "<form class='imgR' action='upload_img.php' enctype='multipart/form-data' method='post'>
   <label><h2>Seleccione una imagen</h2></label>
   <input type='file' name='img' value=''> <br><br>
   <button type='submit' name='button'>Publicar</button>
 </form>";
}else{*/
    ?>
    <form class="MReceta" action="" method="post">
      <input type="text" name="name" placeholder="NOMBRE" value="" id="name" class="Rname">
      <div class="preparacion">
        <label><h3>Preparacion</h3></label>
        <textarea name="Rprep" id="prep" rows="18" cols="20" class="pretxt"></textarea>
      </div>

      <div class="IngC">
        <label><h3>Ingredientes</h3></label>
        <div class="ingB">
            <?php require 'carga.ingredientes.php';?>

        </div>
      <div class="cantymed">
        <div class="ingcant">
          <label><h5>Cantidad</h5></label>
          <label><h5>Medida</h5></label>
       </div>
          <div class="ingmed">
            <input  id="number" type="number" name="cantidad" value="" min="0" class="num">

            <select class="med" name="medida" id="med">
              <option value="cucharadas">Cucharadas</option>
              <option value="gramos">gramos</option>
              <option value="onzas">Onza</option>
              <option value="pizca">Pizca</option>
              <option value="ml">Mililitros</option>
              <option value="lt">Litros</option>
              <option value="piezas">Piezas</option>
              <option value="tazas">Tazas</option>
              <option value="rebanadas">Rebanadas</option>
            </select>

          </div>
          <input type="button" name="prev" value="Agregar" id="agregarI">
      </div>
      </div>
      <div class="tercero">
        <label><h5>Sabor</h5></label>
      <div id="sbr">
        <input type="checkbox" name="sabor" value="Salado"  >Salado
        <input type="checkbox" name="sabor" value="Dulce" >Dulce
        <input type="checkbox" name="sabor" value="Acido"  >Acido <br>
      </div>
      <div class="cont">
      <div class="tipo">
        <label><h5>Tipo</h5></label><br>
        <label><h5>Tiempo</h5></label>

      </div>
            <div class="tiempo">
              <select class="tipe" name="tipo" id="tipe">
                <option value="Desayuno">Desayuno</option>
                <option value="Comida">Comida</option>
                <option value="Cena">Cena</option>
                <option value="Snack">Snack</option>
              </select>
            <select class="time" name="tmpo" id="time">
              <option value="Entrada">Entrada</option>
              <option value="Plato fuerte">Plato fuerte</option>
              <option value="postre">postre</option>
            </select>
          </div>
          </div>
          <div class="ingri" id="fraseIngre">

          </div>
          <a href="#close"><input type="button" name="name" value="Cancelar"></a>

          <button type="button" onclick="publicar()" name="NR">Publicar</button>
        </div>
      </form>
    <?php
//}
 ?>
