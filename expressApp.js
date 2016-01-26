var express = require('express');

var app = express();

app.use(express.static(__dirname + "/public"));

app.listen(3800, function(){
  console.log("Listening on port 3800");
});

exports.app = app;
