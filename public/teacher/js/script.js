var nodeHost = "http://localhost:3800";

$(document).ready(function (){
    $("#loading").remove();
    $("#title, .container, footer").css("visibility", "visible");
    $("#title, #search, footer").addClass('animated bounceInUp');
});

$("#search").keyup(function (e){
  if(e.keyCode == "13"){

   $("#card-div").html("<center><div style=\"margin-bottom: 20px;\" class=\"loader-inner ball-grid-pulse\"><div></div><div></div><div></div><div></div><div></div><div></div><div></div><div></div><div></div></div><div style=\"margin-bottom: 60px;\"></div></center>");


    // $.ajax({
    //   url: nodeHost + "/query",
    //   data: { q: $('#search').val() },
    //   dataType: 'html',
    //   cache: false,
    // })
    // .done(function (msg){
    //   if(msg == "session expired")
    //     window.location = nodeHost + "/login";
    //   else
    //     $("#card-div").html(msg);
    // });
  }
});
