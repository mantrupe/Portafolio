<!DOCTYPE html>
<html>
  <head>
    <meta charset="utf-8">
    <title></title>
  </head>
  <body>
    <div class="newR">
      <h1>Agregar Receta</h1>
    </div>
    <div class="usuario">
      <form class="Upload" action="NewReceta.php" method="post">
        <a href="#close" title="close" class="CloseReceta"></a>
        <h1>Nueva Receta</h1>
        <label>Nombre :</label>
        <h3>Ingredientes</h3><br><input type="text" name="ingredientes"  class="ingredientes" value="">
        <h3>Preparacion</h3><br><input type="text" name="preparacion" class="preparacion" value="">
        <label>Imagen</label><input type="file" name="imagen.receta" value="">
        <label>Sabor</label>
        <label>Tiempo</label>
        <label>Tipo</label>
      </form>
    </div>
  </body>
</html>
