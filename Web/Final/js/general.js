var ingredientes = [];
var sabores = [];
var img;
$(document).ready(function(){
  var ingC = 0;
/*-------------------Funciones slide del menu ----------------------------*/
    $("#tipo").click(function(){
      $(".Mtipo").slideToggle("slow");
    });
    $("#sabores").click(function(){
      $(".Msabor").slideToggle("slow");
    });
    $("#tiempos").click(function(){
      $(".Mtiempo").slideToggle("slow");
    });
    $("#login").click(function(){
      $(".MLogin").fadeToggle();
    });
    $("#user").click(function(){
      $(".MUser").slideToggle("slow");
    });
    $(".confi").click(function(){
      $(".MUser").slideUp(function() {
        $("#contenido").load("confi_user.php");
      })
    });
/*---------------------consultas------------------------------------*/
$("#desayuno").click(function(){
  $("#contenido").load("php/desayuno.php");
});
$("#comida").click(function(){
  $("#contenido").load("php/desayuno.php");
});
/*-------------------Funcion para generar texto de ingredientes------------------*/
    $("#agregarI").click(function(){
        var ingrediente = {
          'nombre' : $("#radio input[type='radio']:checked").val(),
          'cantidad' : $("#number").val() ,
          'medida' : $("#med").val()
        };
        ingredientes.push(ingrediente);
        $("#fraseIngre").append("<span class='printI' id='lbl" + ingC + "'>"+ ingrediente['cantidad'] + " " + ingrediente['medida']+ " de "+ ingrediente['nombre'] +
        " <i class='fa fa-minus-circle menos' aria-hidden='true' onclick='eliminar("+ingC+")'></i>" +" </span><br>");
        ingC++;
        //alert( $("#number").val() + "  "+ $("#med").val() + " de " + $("#radio input[type='radio']:checked").val() );
    });
});
/*-------------slide add Ingrediente-----------------------*/
function slideI(){
  $(".ADD").show();
  $(".addI").hide();
}
function canSli(){
  $(".ADD").hide();
  $(".addI").show();
}
/*---------------------Funcion para eliminar un ongrediente en texto y en el arrego ingredientes----*/
function eliminar(id){
  $("#lbl"+id).css("display" , "none");
  $("#lbl"+id).remove();
  ingredientes.splice(id,1,"NULL");
  //console.log(ingredientes);
}
/*--------------------Funcion que manda datos a php para agregar un ingrediente nuevo a la base--------------*/
function newI(){
  var data = {
    "ni" : $("#newi").val()
  }
  $.ajax({
					type: "POST",
					url: "/Extra/new_ingrediente.php",
					data: data,
					dataType:"json",
					error: function(){
						alert("error la vida te odia ");  //Error de servidor
					},
					success: function(data){
						if(data["response"] == 1){
							//alert(data["reason"]);
              $(".addI").show();
              $(".ADD").hide();
              $(".ingB").load("carga.ingredientes.php");
						}
						else{
							alert(data["reason"]);
						}
					}
				});
}

/*----------------------------------------------Publicacion de Receta-----------------------------*/

  function publicar(){
    $('#sbr input:checked').each(function(){
      sabores.push($(this).val());
    });
      var datitos = {
      "name" : $("#name").val(),
      "Rprep" : $("#prep").val(),
      "tipo" : $("#tipe").val(),
      "tmpo" : $("#time").val(),
      "sabor" : sabores,
      "ingredientes" : ingredientes
    }
    /////RANDOM SHIT
    $.ajax({
      type: "POST",
      url: "/Extra/publicar_receta.php",
      data: datitos,
      dataType:"json",
      error: function(){
        console.log(data);
        alert(datitos["reason"]);
        //alert("error la vida te odia ");  //Error de servidor
      },
      success: function(data){
        if(data["response"] == 1){
          $("#contenido").load("todas.recetas.php");
          $(location).attr('href','index.php');
        }
        else{
          alert(data["reason"]);
        }
      }
    });
  }


/*------------------------------------Cambion de imagen de fondo----------------------------------*/

  function background_random(){
    switch (Math.floor((Math.random() * 5) + 1)) {
      case 1:
      document.body.style.background ="#f3f3f3 url('img/01-01.jpg') repeat right top";
        break;
      case 2:
      document.body.style.background = "#f3f3f3 url('img/fondo1.jpg') repeat right top";
        break;
      case 3:
      document.body.style.background = "#f3f3f3 url('img/fondo2.jpg') repeat right top";
        break;
      case 4:
      document.body.style.background = "#f3f3f3 url('img/fondo3.jpg') repeat right top";
        break;
      case 5:
      document.body.style.background = "#f3f3f3 url('img/fondo4.jpg') repeat right top";
        break;
      default:


    }
  }
  background_random();
