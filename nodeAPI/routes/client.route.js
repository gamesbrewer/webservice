var routes = express.Router(); //create instance of express routes
var clientController = require('./../controller/client.controller'); //path to the controller/client.controller.js

//create the routes
routes.post('/list',
    clientController.listClient
);

//export express routes
module.exports = routes;
