var routes = express.Router(); //create instance of express routes
var userValidator = require('./../validation/user.validation'); //path to the validation/user.validation.js
var userController = require('./../controller/user.controller'); //path to the controller/user.controller.js

//create the routes
routes.post('/list',
    userController.listUser
);

//create the routes
routes.post('/create',
    [
      userValidator.validateAddUser, //function that validate request using express-validator
      userValidator.checkValidationResult,
    ],
    userController.createUser
);

//export express routes
module.exports = routes;
