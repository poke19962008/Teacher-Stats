var app = require('./expressApp').app;
var mongoClient = require('mongodb').MongoClient;

var mongoURI = "mongodb://localhost:27017/teacher";
var limit = 5;

app.get('/teacher/api', function(req,res){
  var query = req.query.q;

  mongoClient.connect(mongoURI, function (err, db){
    if(err)
      console.log("[ERROR] Cannot connect Mongo");

    var cur = db.collection('main').find({
      'name': {
        $regex: query,
        $options: 'i'
      }
    }).limit(limit);

    cur.toArray(function (err, doc){
      res.send(doc);
    });

  });
});
