express           = module.exports = require('express');
bodyParser        = module.exports = require('body-parser');
expressValidator  = module.exports = require('express-validator');
fileUpload        = module.exports = require('express-fileupload');
jwt               = module.exports = require('jsonwebtoken');
fs                = module.exports = require('fs');

let serverRoutes  = require('./routes/server.route'); //path to the routes/server.routes.js
let userRoutes    = require('./routes/user.route'); //path to the routes/user.routes.js
//let clientRoutes  = require('./routes/client.route'); //path to the routes/client.routes.js
connection        = require('./config/database') //path to the config/database.js

var port = process.env.PORT || 8080;

var app = express();
app.use(bodyParser.urlencoded({extended: false}))
app.use(bodyParser.json());
app.use(expressValidator());

//public routes
app.use('/v1.0',serverRoutes);

// user routes
app.use('/v1.0/user',userRoutes);

// client routes
//app.use('/v1.0/client',clientRoutes);

//create app listener
app.listen(port, function () {
    console.log('RESTful API server started on : ' + port)
})

//export the instance of express
module.exports = app;
