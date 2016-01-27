var nodeHost = "http://localhost:3800";

$(document).ready(function (){
    $("#loading").remove();
    $("#title, .container, footer").css("visibility", "visible");
    $("#title, #search, footer").addClass('animated bounceInUp');
});

var ranges = ["0-10", "10-20", "20-30", "30-40", "40-50", "50-60", "60-70", "70-80", "80-90", "90-100"];

var options = {
  distributeSeries: true,
  height: 500,
};

var responsiveOptions = [
  ['screen and (min-width: 641px) and (max-width: 1024px)', {
    seriesBarDistance: 10,
    axisX: {
      labelInterpolationFnc: function (value) {
        return value;
      }
    }
  }],
  ['screen and (max-width: 640px)', {
    seriesBarDistance: 5,
    axisX: {
      labelInterpolationFnc: function (value) {
        return value[0];
      }
    }
  }]
];

$("#search").keyup(function (e){
  if(e.keyCode == "13"){

   $("#card-div").html("<center><div style=\"margin-bottom: 20px;\" class=\"loader-inner ball-grid-pulse\"><div></div><div></div><div></div><div></div><div></div><div></div><div></div><div></div><div></div></div><div style=\"margin-bottom: 60px;\"></div></center>");


    $.ajax({
      url: "./api",
      data: { q: $('#search').val() },
      dataType: 'json',
      cache: false,
    })
    .done(function (msg){
      $("#card-div").html("");

      if(msg.length == 0){
        $("#card-div").append("<div class=\"card-section\" id=\"info-card\"><div id=\"card-msg\">Sorry... Cannot Find "+$('#search').val()+"</div>");
      }else{
        for (var i = 0; i < msg.length; i++) {
          $("#card-div").append("<div class=\"card-section\" id=\"info-card\"><div id=\"card-msg\">"+ msg[i].name +"</div></div>");


          for(subject in msg[i].data){
            var subjectDiv = "card-"+ msg[i]._id +"-"+subject;



            $("#card-div").append("<div class=\"card-section "+subjectDiv+"\"><div id=\"card-msg\">"+subject+"<br>Number of students: "+msg[i].data[subject].student+"</div>");

            for(key in msg[i].data[subject]){
              if(key == "student")
                continue;

              var chartDiv = "ct-chart-" + subjectDiv + "-" + key;
              var data = {
                labels: [],
                series: [],
              };

              for(var j=0; j<10; j++){
                var range = ranges[j];

                data.labels.push(range);
                data.series.push(msg[i].data[subject][key][range]);
              }

              $("." + subjectDiv).append("<div class=\"graph-title\">"+key+"</div>");
              $("." + subjectDiv).append("<div class=\""+chartDiv+" chart\"></div>");
              var locChart = new Chartist.Bar('.'+chartDiv, data, options);

            }
          }
        }
      }
    });

  }
});
