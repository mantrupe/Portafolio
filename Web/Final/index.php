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
    <div class="header">
      <a href="index.php"><img src="img/logo.jpg" alt="" class="logo"/></a>
      <label class="op" id="recetas"><span></span><a href="index.php">Recetas</a></label>
      <label class="op" id="tipo" ><span></span>Tipo</label>
      <label class="op" id="sabores"><span></span>Sabores</label>
      <label class="op" id="tiempos"><span></span>Tiempos</label>
      <?php
      session_start();
        if (isset($_SESSION['name'])) {
          echo "<label class='po' id='user'>".$_SESSION['name']."</label>";
        }else {
          echo "<label class='po' id='login' >Login</label>";
        }
       ?>
    </div>
  <!-- menus -------------------------->
    <div class="Mtipo">
      <div class="ftip"><label class="ftip" id="desayuno">Desayuno</label><br><hr></div>
      <div class="ftip"><label class="ftip" id="comida">Comida</label><br><hr></div>
      <div class="ftip"><label class="ftip" id="cena">Cena</label><br><hr></div>
      <div class="ftip"><label class="ftip" id="snack">Snack</label><br><hr></div>
      <div class="ftip"><label class="ftip">Bebida</label><br><hr></div>
    </div>
    <div class="Msabor">
      <label>Dulce</label><br><hr>
      <label>Salado</label><br><hr>
      <label>Acido</label><br>
    </div>
    <div class="Mtiempo">
      <label>Entrada</label><br><hr>
      <label>Plato Fuerte</label><br><hr>
      <label>Postre</label><br>
    </div>
    <!----Menu.Usuario------->
    <div class="MUser">
      <a href="#Nrecipe">Agregar receta</a><br><hr>
      <label class="confi">Configuracion</label><br><hr>
      <a href="cerrar.sesion.php"><label>Cerrar Session</label></a><br>

    </div>
    <form class="" action="ingresar.usuario.php" method="post">
      <div class="MLogin">
        <div class="email">
          <label class="Earea">Email</label>
          <input type="text" name="email" value="" class="Etext"><br>
        </div>
        <div class="password">
          <label class="logArea">Contraseña</label>
          <input type="password" name="password" value="" class="logText"><br>
        </div>
        <a href="#regis" class="modal">REGISTRARSE</a>
        <input type="submit" name="enviar" value="Entrar" class="LogBut">
      </div>
    </form>
    <!---------Modal-Agregar.receta--------->
    <div class="fondoModal2" id="Nrecipe">
            <?php require 'modal_receta.php';?>
    </div>
<!--</div> -->
    <!---------- fin menus------>
    <!------------Registros------------>
    <div class="fondoModal" id="regis">
      <form class="registro" action="registro.cocinero.php"  method="post">
        <a href="#close" title="Close" class="close">X</a>
        <h1>Registrarse</h1> <br>
        <label>Nombre:</label> <input type="text" name="nombre" value="" class="Rnombre"><br>
        <label>Email</label>   <input type="text" name="email" value="" class="Remail"><br>
        <label>Contraseña</label> <input type="password" name="password" value="" class="Rpass"><br>
        <label>Confirme contraseña</label> <input type="password" name="cpassword" value="" class="Rconfirm"><br>
        <input type="submit" name="regbutton" value="Registrarse" class="Rbutton" >
      </form>
    </div>
    <div class="contenido" id="contenido">
      <?php require 'todas.recetas.php'; ?>
    </div>
      <!---JavaScript-------------------->
      <script type="text/javascript" src="js/jquery-1.11.3.min.js"></script>
      <script type="text/javascript" src="js/general.js"></script>
    </body>
  </html>
