$(document).ready(function(i){function l(){var l=i(".wrapper").width(),o=i(".search-column").width();i("main").width(l-o-10)}var o=i(window).width();l(),o<1004?i("article").addClass("full-width-mobile"):i("article").removeClass("full-width-mobile"),i(window).resize(function(){o=i(this).width(),l(),o<1004?i("article").addClass("full-width-mobile"):i("article").removeClass("full-width-mobile")}),i(".profile-options .options").click(function(){i(this).find(".drop-down").slideToggle(150)}),i(".diary .button").on("click",function(){i(".diary .diary-drop-down").slideToggle(230)})});