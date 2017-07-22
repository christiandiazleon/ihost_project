$(document).ready(function($) {

// Acomodar el cuerpo de la página (articulos) dinámicamente al tamaño de la pantalla

  var winWidth = $(window).width();

    function mainResize () {
            // encontrar el tamaño del wrapper del documento
            var wrapWidht = $(".wrapper").width();
            // Encontrar el tamaño de la columnda donde esta el mapa y los filtros
            var searchColumnWidth = $(".search-column").width()
            // definir el ancho del cuerpo de la pagina restando el wrapper menos la columna y la margen (10px)
            $("main").width(wrapWidht - searchColumnWidth - 10)
    } mainResize ();

// Cuando la pagina alcance un punto de quiebre añade una clase para que los artículos de dos columnas pasen a ser de solo una
    if (winWidth < 1004) {
        $("article").addClass("full-width-mobile");
    } else {
        $("article").removeClass("full-width-mobile");
    }

// En esta función van todos los comportamientos que debe ejecutarse cuando la pantalla cambia de tamaño
  $(window).resize(function () {
        winWidth = $(this).width();
    mainResize ();
        if (winWidth < 1004) {
            $("article").addClass("full-width-mobile");
        } else {
            $("article").removeClass("full-width-mobile");
        }
  });

});
